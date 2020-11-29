import { Component, OnInit } from '@angular/core';
import { saveAs } from 'file-saver';
import { HttpClient, HttpHeaders } from '@angular/common/http';


import { UserService } from '../user.service';
import { FormGroup,FormControl,Validators } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  
  files:File[];
  percentDone: number;
  uploadSuccess: boolean;
  your_file:File;
  title:string;
  username:string;
  valid:boolean;
  constructor(private service:UserService,private http: HttpClient) { this.valid=false;}

  ngOnInit(): void {
    
    try{
      this.username=sessionStorage.getItem('username');
    }
    catch(err){
      location.replace("http://localhost:4200/login");
    }

    if(this.username==null){
      location.replace("http://localhost:4200/login");
    }
    this.valid=true;
  }

  onTitleChanged(event: any) {
    this.title = event.target.value;
  }

  onImageChanged(event: any) {
    this.your_file = event.target.files[0];
  }
  logout(){
    sessionStorage.setItem('token', '');
    sessionStorage.setItem('username', '');
    location.replace("http://localhost:4200/login");
  }
  uploadfile() {
    const uploadData = new FormData();
    uploadData.append('username',this.username);
    uploadData.append('label', this.title);
    uploadData.append('data', this.your_file,this.your_file.name);
    this.service.add_files(uploadData).subscribe(
      response => {
        alert(response);
      },
      error => {  
        alert("fail");
      }
    );
  }
  
  downloadfile(){

    const uploadData = new FormData();
    uploadData.append('username', this.username);
    this.service.view_files(uploadData).subscribe(
      response => {
              if(response=="You dont have any files"){
                alert(response);
              }
              else{
                var i;
                for(i=0;i<response.length;i++){
                  var x=response[i]['label']+'txt';
                  var y ='http://127.0.0.1:8000'+ response[i]['data'];
                  this.http.get(y,{responseType: 'arraybuffer'}).subscribe(
                    res => {
                      const blob = new Blob([res], { type : 'application/pdf' });
                      const file = new File([blob], x + '.pdf', { type: 'application/pdf' });
                      saveAs(file);
                    },
                    error => {
                      console.log("failed");
                    }
                  );
                }
              }           
      }),
      error => console.log('Error downloading the file'),
      () => console.info('File downloaded successfully');
  }


}
