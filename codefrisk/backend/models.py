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
    def _str_(self):
        return self.data.name

def remove_redundant_functions(content):
    """
    Arguments:
        content: string storing the source code
    Return type: updated string
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
    t=""
    for type in type_list:
        L=re.findall(type+"\s*[a-z0-9_]\s\([a-z0-9_ \n\t,\r\f\v]\)\s\{",content)
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
    return content

def visualizer(list_of_files,similarity_matrix):
    """ 
    Arguments    :
        list_of_files    :list of source code files
        similarity_matrix:2-dimensional matrix representing mutual similarity between each pair of files
    Return type  :
        Path of the saved image
    Functionality:
        Plotting the output similarity_matrix and saving it as an image """
    x=range(len(list_of_files)) 
    y=range(len(list_of_files))
    xx,yy=np.meshgrid(x,y)
    z=similarity_matrix[xx,yy]
    cmap =cm.get_cmap("rainbow",100)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    im=ax.matshow(z,cmap=cmap,vmin=0,vmax=1.01,origin='lower')
    for i in range(len(list_of_files)):
        ax.text(i,i,"none",ha="center", va="center", color="k")
        for j in range(i+1,len(list_of_files)):
            ax.text(j, i, int(similarity_matrix[i,j]*100)/100,ha="center", va="center", color="k")
            ax.text(i,j, int(similarity_matrix[i,j]*100)/100,ha="center", va="center", color="k")
    fig.colorbar(im,shrink=0.5)
    ax.set_xticks(range(len(list_of_files)))
    ax.set_yticks(range(len(list_of_files)))
    ax.set_xticklabels(list_of_files,rotation=90)
    ax.set_yticklabels(list_of_files)
    ax.tick_params(labelsize=30/len(list_of_files))
    random=np.random.randint(1,100)
    path=str(random)+'.png'
    plt.savefig('media/'+path)
    return path

def remove_macros(file_content):

    """
    Arguments:
        file_content: string storing the source code
    Return type: updated string
    Functionality:
        All macros in the code are replaced.
    Logic Used:
        Using Regex detect the macros
        Replace them using replace() function
    """
    m=re.findall('#define .+ .+',file_content) 
    """finding macros"""
    
    content=re.sub('#define .+ .+','',file_content)  
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
    return content

def remove_comments(file_content):
    """
    Arguments:
        file_content: string storing the source code
    Return type: updated string
    Functionality:
        All commments in the code are replaced.
    Logic Used:
        Using Regex detect substrings starting with // and ending with \n 
        Similarly detect substrings starting with /* and ending with */
    """
    pattern=re.compile('//.*?$|/\*.*?\*/',re.DOTALL|re.MULTILINE) 
    """ pattern for comments """
    content=re.sub(pattern,'',file_content)  
    """remove comments"""
    return content

def remove_comments_pythonfile(file_content):
    """
    Arguments:
        file_content: string storing the source code in python
    Return type: updated string
    Functionality:
        All commments in the code are replaced.
    Logic Used:
        Using Regex detect substrings starting with # and ending with \n 
        Similarly detect substrings starting with ''' and ending with '''
    """
    pattern=re.compile('#.*?$|\'\'\'.*?\'\'\'|\"\"\".*?\"\"\"',re.DOTALL|re.MULTILINE)
    content=re.sub(pattern,'',file_content)
    return content

def preprocessing(list_of_files,usernames):
    """
    Core logic is based on the Bag_of_Words
    and TF-IDF Strategy( Term frequency and Inverse Document Frequency )
    
    Arguments    :
        list_of_files    :list of source code files
        usernames        :It consists data of all the Users who have been SignedUp
    Return type  :
        It returns "tf_idf()" function as Output
    Functionality:
        It finds the count of each word after removing comments and replacing macros and passes this vector to tf_idf function.
    
    """
    word_count_across_documents={}
    """ Maintains the word count of each element in a document """

    word_count_in_each_file=[]
   
    for files in list_of_files:

        filename='media/'+files
        temp={}
        myfile=open(filename,"r")
        content=myfile.read()
        myfile.close()
        
        if(files[-4:]=='.cpp'):
            content=remove_comments(content)
            content=remove_redundant_functions(content)
            content=remove_macros(content)
            
        elif(files[-3:]=='.py'):
            content=remove_comments_pythonfile(content)
      
        
        sym=[",",";","{","}",")","(","[","]","+","-","*","/","%","|","&","^","!","=","<",">","?","'",'"','#','.']
        for i in sym:
            content=content.replace(i," "+i+" ")
        
        if(files[-4:]=='.cpp'):
            content=content.replace("while","for")
            content=content.replace("switch","if")
            content=content.replace("case","else if")
            content=content.replace("default","else")
            content=content.replace("do","")
            content=content.replace(";","")
            content=content.replace(",","")
            content=content.replace("'","")
            content=content.replace('"',"")
            
        elif(files[-3:]=='.py'):
            content=content.replace('while','for')
            content=content.replace('switch','if')
            content=content.replace('case','elif')
            content=content.replace('default','else')
            content=content.replace('do','')
            content=re.sub(':|\'|\"','',content)
        while(content.find('/*')!=-1):
            i=content.find('/*')
            j=content.find('*/')
            content=content[0:i]+content[j+2:]
        List_of_words=content.split()

        for i in List_of_words:
            temp[i]=temp.get(i,0)+1 
            word_count_across_documents[i]=word_count_across_documents.get(i,0)+1
        
        word_count_in_each_file.append(temp)

    return tf_idf(word_count_in_each_file,word_count_across_documents,list_of_files,usernames)

def tf_idf(word_count_in_each_file,word_count_across_documents,list_of_files,usernames):
    """ Arguments    :
        list_of_files              :list of source code files
        usernames                  :It consists data of all the Users who have been SignedUp
        word_count_in_each_file    :Frequency of word corresponding to each file as an array of dictionary
        word_count_across_documents:Frequency of each word across as files corresponding to a particular assignment as dictionary
    Return type  :
        It returns "txt_file()" function as Output
    Functionality:
        It computes tf_idf vector corresponding to each file.
        The tf_idf function is somewhat different from the original one
        If we use the bag of words strategy then similarity is determined mostly by the variables which have maximum count in a file.
        But similarity should depend more on core logic loke number of functions,operators loops etc.
        The weight added for each word say 'x' in file 'f' is -0.01+log(freq of x across all files corresponding to assignment/(freq of x in f*number of files))
        -0.01 is added so that words which have equal distribution across all files are given negative weightage.
        Words which have low frequency in a file than average frequency across all files are given high weightage
        Words which have high frequency in a file than average frequency across all files are given low weightage
        Uniqueness is determined by high weightage words.
    """
    similarity_matrix=np.zeros((len(list_of_files),len(list_of_files)))
    tf_idf_vec=[]
    for i in range(len(list_of_files)):
        temp=[]
        for j in word_count_in_each_file[i]:
            temp.append(word_count_in_each_file[i].get(j)*(-0.01+(math.log(word_count_across_documents.get(j)/word_count_in_each_file[i].get(j)/len(list_of_files)))))
        temp.sort()
        tf_idf_vec.append(temp)

    for i in range(len(list_of_files)):
        similarity_matrix[i,i]=1;
        for j in range(i+1,len(list_of_files)):
            similarity_matrix[i,j]=similarity(np.array(tf_idf_vec[i]),np.array(tf_idf_vec[j]))
            similarity_matrix[j,i]=similarity_matrix[i,j]
    
    return txt_file(similarity_matrix,list_of_files,usernames)

def txt_file(similarity_matrix,list_of_files,usernames):
    """ 
    Arguments    :
        list_of_files    :list of source code files
        similarity_matrix:2-dimensional matrix representing mutual similarity between each pair of files
        usernames        :It consists data of all the Users who have been SignedUp
    Return type  :
        It returns "csv_file()" function as Output
    Functionality:
        Displaying the Percentage matching among files in text format and saving it as a csv file """   
    result=open("media/result.txt","w")
    res=""
    for i in range(len(list_of_files)):
        for j in range(i+1,len(list_of_files)):
            res+="similarity between "+ list_of_files[i]+" submitted by "+usernames[i]+" and "+list_of_files[j]+" submitted by "+usernames[j]+" = "+str(similarity_matrix[i][j])+"\n"
    result.write(res)
    return csv_file(list_of_files,similarity_matrix)

def csv_file(list_of_files,similarity_matrix):
    #""" Interpreting the Output data as a CSV file ,
    #where each element represent the percentage matching between the file 
    #corresponding to a row and column"""
    """ 
    Arguments    :
        list_of_files    :list of source code files
        similarity_matrix:2-dimensional matrix representing mutual similarity between each pair of files
    Return type  :
        It returns "visualizer()" function as Output
    Functionality:
        Plotting the output similarity_matrix and saving it as an csv file 
           
    """
    f=similarity_matrix.tolist()
    files=['']+list_of_files
    for x in range(len(list_of_files)):
        f[x]=[list_of_files[x]]+f[x]
    f=[files]+f
    with open("media/result.csv", "w+") as myCsv:
        csvWriter = csv.writer(myCsv, delimiter=',')
        csvWriter.writerows(f)
    return visualizer(list_of_files,similarity_matrix)
def similarity(s,t):
    
    """ 
    Arguments    :
        s   :(sorted)list of numbers
        t   :(sorted)list of numbers
    Return type  :
        returns a number in the range(0,1)
    Functionality:
        Evaluates the cosine product of the two vectors
    """
    x=min(s.size,t.size)
    s=s[-x:]
    t=t[-x:]
    return np.dot(s,t)/(np.linalg.norm(s)*np.linalg.norm(t))
