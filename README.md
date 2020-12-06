# CodeFrisk

<pre>Meet our Team</pre>
**Member Name** 	                 **Contribution to the Project**<br />
<pre>
Pokala Mohith 	                 Backend and Frontend contributions, contributions for core logic implementation<br />
Poluparthi Preetham 	         CoreLogic Contribution,Documentation<br />
Punna Hitesh Kumar 	         Front end implementation, Styling the website,Documentation <br />
Thivesh Chandra Mattti       	 Frontend implementations,Visualizaion,Core Logic Implementation<br />
</pre>
# Softwares Used and Prerequisites

First Install Python3 which comes along with pip.The website uses Angular10 for the frontend and Django for the backend. The website is compatible with all versions of Python from Python3.The backend must me hosted from a pc which uses linux with g++ installed or you need WSL if you are using Windows.You need to install django-corheaders and django-rest api after installing django and matplotlib and numpy after insatlling python,using the commands 

```diff
 python3 -m pip install django-cors-headers

 python3 -m pip install djangorestframework

 pip3 install numpy==1.19.3

 pip3 install matplotlib

```
### Refer to following links:
Angular:https://angular.io/guide/setup-local

Node JS:https://nodejs.org/en/download/

Django:https://docs.djangoproject.com/en/3.1/howto

Django-cors-headers:https://pypi.org/project/django-cors-headers/

Django-restapi:https://www.django-rest-framework.org/#installation

# Steps to run the code:
 ## Backend
 Clone the github repository using git clone https://github.com/mohithpokala/Project. 
 
 First Create a django-superuser.Go to the Directory containing manage.py("/Project/codefrisk/"), 
 now Run the following command in terminal " python manage.py createsuperuser ".<br />
 
 Follow the steps as prompted by the terminal.<br />
 
 After this step run the following three commands in the same sequence 
 ``` diff
  python manage.py makemigrations 
  python manage.py migrate 
  python manage.py runserver.
 ```
 Now You hosted the backend.
    
 # Frontend
 Migrate to the interface folder.

 Run 
 ``` diff 
 ng serve --open
 ```
 If you get a jquery error runn the followong commands on terminal.
    
       npm install jquery
       
       npm install bootstrap
 
 

What has been implemented so far

    A basic framework for the website has been created.

    The Website incorporates five features:Login,Logout,Register,Upload,Download

    Implemented uploading of files for a user who has logged in.

    Basic implementation for downloading a file has been done.

    Core logic-wise, a bag-of-words strategy has been used as placeholder logic, which will be replaced later. Rudimentary Latent Semantic Analysis has been implemented as well (debugging is required, some parts don't work as intended).

The Theoretical Aspect

The two strategies we have attempted to implement here are:

    Naïve Bag of Words strategy: For each document, a sorted vector of the word occurrences in the file are created. The cosine similarity between two vectors is returned as the degree of plagiarism.

    Latent Semantic Analysis: This is slightly more polished than the Bag of Words strategy. First, an array is created where the i,jth entry represents the occurrence of word j in the ith document. LSA essentially works by detecting the latent similarities between two documents. For example, if the word "dog" and "hound" are used similarly in different documents (say we have the sentence "The dog barked at the car" in one document and "The hound barked at the car" in another document), then it inherently identifies that the two words might mean the same thing. A low-rank approximation of the original array is found by performing Singular Value Decomposition and then taking the appropriate rows/columns. When we do this, it clumps together dimensions (which are words here) that mean similar things. So if we had the words {(dog),(hound),(bed)} in the original document, a low-rank approximation of this could correspond to something like {(1.43*dog + 0.39*hound),(bed)}. That is, when words are clumped together, an appropriate weight is given to each word such that it carries latent similarities. After these words are grouped together, the cosine similarity between two vectors (in the low-rank approximation) is returned as the degree of plagiarism between them.

For either method, we begin by creating the array used in LSA. In the first case, we just sort each column individually and find cosine similarity. For the second method, we perform the operations described above to get the degree of similarity.
Plans on what to implement in the future

    Create file segmentation in the upload and the output folder, which would let the code pick out the user's particular files.

    Implement sessions for logged in users, a prototype of the same is present as of now.

    As can be guessed from the group name, we plan to implement the algorithm used in the MOSS software (a modified simpler version in case it becomes too challenging to write the actual thing). We have started reading the paper that describes the ideas behind the MOSS algorithm and have also written a brief summary of what is be done as part of the algorithm here.
