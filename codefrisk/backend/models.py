from django.contrib.auth.models import User
from django.db import models
import numpy as np
import re
import matplotlib.pyplot as plt
import sys
from matplotlib import cm
import matplotlib.colors as colors
import math

class add_data(models.Model):
    username = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    data = models.FileField()
    def __str__(self):
        return self.data.name


class add_data(models.Model):
    username = models.CharField(max_length=50)
    label = models.CharField(max_length=50)
    data = models.FileField()
    def _str_(self):
        return self.data.name

def visualizer(l,data):
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
    ax.set_xticklabels(l,rotation=90)
    ax.set_yticklabels(l)
    ax.tick_params(labelsize=len(l))
    random=np.random.randint(1,100)
    path=str(random)+'.png'
    plt.savefig('media/'+path)
    return path


def tf_idf(list_of_files,h):
   
    word_count_across_documents={}
    word_count_each_file=[]
    file_names=[]
   
    for files in list_of_files:
        filename='media/'+files
        temp={}
        myfile=open(filename,"r")
        content=""
        myline = myfile.readline()
        while myline:
            myline.strip()
            if(myline[0:2]=='//'):
                pass
            elif(myline.find('//')!=-1):
                content+=myline[0:myline.find('//')]
            else:
                content+=myline
            myline = myfile.readline()
        myfile.close() 
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
    return visualizer(list_of_files,l)

def similarity(s,t):
    #print(s,t)
    x=min(s.size,t.size)
    s=s[-x:]
    t=t[-x:]
    return np.dot(s,t)/(np.linalg.norm(s)*np.linalg.norm(t))