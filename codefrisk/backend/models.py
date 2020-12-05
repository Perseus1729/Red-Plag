from django.contrib.auth.models import User
from django.db import models
import subprocess
import os
import numpy as np
import re
import matplotlib.pyplot as plt
import sys
from matplotlib import cm
import matplotlib.colors as colors
import math
import csv
plt.switch_backend('Agg')
class add_data(models.Model):
    """
    """
    username = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    data = models.FileField()
    def __str__(self):
        return self.data.name

def remove_redundant_functions(content):
    """
    Arguments:
        content: string storing the source code
    Return type: this is void function.The string passed will be updated
    Functionality:
        redundant functions in a source code are removed
    Logic Used:
         Write a minimal parser that can identify functions.
         It just needs to detect the start and ending line of a function.
         Programmatically comment out the first function, save to a temp file.
         Try to compile the file by invoking the complier.
         Check if there are compile errors, if yes, the function is called, if not, it is unused.
         Continue with the next function. 
         Reference:https://stackoverflow.com/questions/33209302/removal-of-unused-or-redundant-code
    """
    type_list=['int','void','char','string']
    for type in type_list:
        L=re.findall(type+"\s*[a-z0-9_]*\s*\([a-z0-9_ \n\t,\r\f\v]*\)\s*\{",content)
        for y in L:
            y=y.replace("(","\(")
            y=y.replace(")","\)")
            x=re.search(y,content)
            first=x.span()[0]
            last=x.span()[1]
            count=1
            while(count!=0):
                if(content[last]=='{'):
                    count+=1
                if(content[last]=='}'):
                    count-=1
                last+=1
            t=content[0:first]+content[last:]
        temp = open("temp.cpp", "w")
        temp.write(t)
        temp.close()
        g = subprocess.getstatusoutput("g++ temp.cpp")
        if(g[1]==""):
            content=t

def visualizer(l,data):
    """ 
    Arguments:
        l:list of source code files
        data:2-dimensional matrix representing mutual similarity between each pair of files
    Return type:
        Path of the saved image
    Functionality:
    Plotting the output data and saving it as an image """
    x=range(len(l)) 
    y=range(len(l))
    xx,yy=np.meshgrid(x,y)
    z=data[xx,yy]
    cmap =cm.get_cmap("rainbow",100)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    im=ax.matshow(z,cmap=cmap,vmin=0,vmax=1.01,origin='lower')
    for i in range(len(l)):
        ax.text(i,i,1,ha="center", va="center", color="k")
        for j in range(i+1,len(l)):
            ax.text(j, i, int(data[i,j]*100)/100,ha="center", va="center", color="k")
            ax.text(i,j, int(data[i,j]*100)/100,ha="center", va="center", color="k")
    fig.colorbar(im,shrink=0.5)
    print(l)
    ax.set_xticks(range(len(l)))
    ax.set_yticks(range(len(l)))
    ax.set_xticklabels(l,rotation=90)
    ax.set_yticklabels(l)
    ax.tick_params(labelsize=len(l))
    random=np.random.randint(1,100)
    path=str(random)+'.png'
    plt.savefig('media/'+path)
    return path


def tf_idf(list_of_files,h):
    """Core logic is based on the Bag_of_Words
    and TF-IDF Strategy( Term frequency and Inverse Document Frequency )
    """
    word_count_across_documents={}
    """ Maintains the word count of each element in a document """
    word_count_each_file=[]
    file_names=[]
   
    for files in list_of_files:
        filename='media/'+files
        temp={}
        myfile=open(filename,"r")
        content=myfile.read()
        myfile.close()
        pattern=re.compile('//.*?$|/\*.*?\*/',re.DOTALL|re.MULTILINE) 
        """ pattern for comments """
        content=re.sub(pattern,'',content)  
        """remove comments"""
        remove_redundant_functions(content)

        m=re.findall('#define .+ .+',content) 
        """finding macros"""
        content=re.sub('#define .+ .+','',content)  
        """removing macros definitions"""
        for i in range(len(m)):     
            """replacing macros"""
            j=0
            n=0
            for k in range(8,len(m[i])):
                if(m[i][k]=='('):
                    j=k-8
                    break
                elif(m[i][k]==' '):
                    j=-1
                    n=k+1
                    break
            
            if(j!=-1):
                for k in range(j+9,len(m[i])):
                    if(m[i][k]==')'):
                        n=k+2
                        break
            
            if(j==-1 or m[i][j+9]==')'):
                content=content.replace(m[i][8:n-1],m[i][n:])
                continue
            else:
                y_param=m[i][j+9:n-2].split(',')
                
                pattern=m[i][8:j+8]+'\(.*?\)'
                m2=re.findall(pattern,content)
                
                for z in m2:
                    param=z[j+1:-1].split(',')
                    st=m[i][n:]
                    

                    for k in range(len(param)):
                        st=re.sub(y_param[k].strip(),param[k],st)
                    content=content.replace(z,st)

        sym=[",",";","{","}",")","(","[","]","+","-","*","/","%","|","&","^","!","=","<",">","?","'",'"','#','.']
        for i in sym:
            content=content.replace(i," "+i+" ")
        while(content.find('/*')!=-1):
            i=content.find('/*')
            j=content.find('*/')
            content=content[0:i]+content[j+2:]
        L=content.split()
        for i in L:
            temp[i]=temp.get(i,0)+1
            word_count_across_documents[i]=word_count_across_documents.get(i,0)+1
        
        word_count_each_file.append(temp)
        file_names.append(files)

    l=np.zeros((len(file_names),len(file_names)))
    return txt_file(file_names,word_count_each_file,word_count_across_documents,list_of_files,l,h)
def txt_file(file_names,word_count_each_file,word_count_across_documents,list_of_files,l,h):
    """ Displaying the Percentage matching among files in text format """
    tf_idf_vec=[]
    for i in range(len(file_names)):
        temp=[]
        for j in word_count_each_file[i]:
            temp.append(word_count_each_file[i].get(j)*(-0.01+(math.log(word_count_across_documents.get(j)/word_count_each_file[i].get(j)/len(file_names)))))
        temp.sort()
        tf_idf_vec.append(temp)
    result=open("media/result.txt","w")
    res=""
    for i in range(len(file_names)):
        for j in range(i+1,len(file_names)):
            l[i,j]=similarity(np.array(tf_idf_vec[i]),np.array(tf_idf_vec[j]))
            l[j,i]=l[i,j]
            res+="similarity between "+ file_names[i]+" submitted by "+h[i]+" and "+file_names[j]+" submitted by "+h[j]+" = "+str(l[i][j])+"\n"
    result.write(res)
    return csv_file(list_of_files,l)
def csv_file(list_of_files,l):
    """ Interpreting the Output data as a CSV file ,
    where each element represent the percentage matching between the file 
    corresponding to a row and column"""
    f=l.tolist()
    filess=['']+list_of_files
    for x in range(len(list_of_files)):
        f[x]=[list_of_files[x]]+f[x]
    f=[filess]+f
    with open("media/result.csv", "w+") as myCsv:
        csvWriter = csv.writer(myCsv, delimiter=',')
        csvWriter.writerows(f)
    return visualizer(list_of_files,l)
    
def similarity(s,t):
    
    """ This shows the fraction of matching among the files """
    x=min(s.size,t.size)
    s=s[-x:]
    t=t[-x:]
    return np.dot(s,t)/(np.linalg.norm(s)*np.linalg.norm(t))
