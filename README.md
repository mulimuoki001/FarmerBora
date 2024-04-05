# FarmerBora
Welcome to FarmerBora Project. For this project project i used the Django Web Framework.To run this project using any terminal follow the following steps:
1. The first step is to create a Virtual Environment(Am assuminmg you are using version 3 of python) .The name of my virtual environment is env

   
        python3 -m venv <name_of_your_virtual_environment> 
        python3 -m venv env      
   ![Screenshot (231)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/0a6b6b1a-fa2c-4ec5-8c35-b57a8b575751)
   
2. Activate the virtual environment:
   
   On Windows
   
        	env\Scripts\activate

   On MacOS nad Linux(for those who will choose to use the Ubuntu terminal)

         source env/bin/activate
    ![Screenshot (232)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/bef83d93-24bf-4f45-b51d-f0765fd7598e)

4. Within the virtual environment clone my reposiotry
   
   Ensure git is activated within the virtual environment

         git init
    Now clone repository 

         git clone https://github.com/mulimuoki001/FarmerBora.git
        
   ![Screenshot (233)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/55939bbd-4181-4284-ad1c-6b79ce160c31)
6. Install all the Dependencies(Run the following commands to run all the necessary requirements for the app to run)

   
           pip install -r requirements.txt

If you encounter an error because the pg_config executable is not found, which is required to build psycopg2 from source, follow the following sub-process:
               Install the libpq-dev package (this contains pg_config):
   On Ubuntu:
               
               sudo apt-get install libpq-dev
               
   On CentOS: 
               
               sudo yum install libpq-devel
   On macOS:
               
               brew install libpq
Then, you can proceed to install psycopg2-binary using pip:
               
               pip install psycopg2-binary
By installing the libpq-dev package, you should have the necessary pg_config executable available for installing psycopg2-binary


![Screenshot (234)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/bd53f5a6-5b99-43e7-9e89-41319fe20a5a)
![Screenshot (235)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/03bb9c5c-55a2-4e80-b1bf-3a746c47d75b)
![Screenshot (236)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/c12e7ec4-aace-4361-99ff-809262e6477b)
![Screenshot (237)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/7d89b0f4-67bb-47e3-af0e-fdcf28b3b0c0)
5. Create a Super user(This is optional, only if you want to access the database with super user privilleges)

        python 3manage.py createsuperuser

  ![Screenshot (240)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/7dd0d6aa-0929-4bea-a488-7486d081f684)
6. Run the Development server
   
        python3 manage.py runserver
  ![Screenshot (241)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/62564062-0f0e-48bc-a975-c0629cc0e20f)

To access the Application Open the browser and go to  http://127.0.0.1:8000 to see the running Django Application

If you follow all the steps correctly, you should be able to run the application using your machine's local server. The application is also deployed on the Heroku. Heroku is a cloud platform that allows developers to build, deliver, monitor, and scale applications. It supports several programming languages, including Python, Ruby, Node.js, Java, PHP, and more. Heroku abstracts away infrastructure management tasks, making it easier for developers to focus on building and deploying their applications without worrying about server configuration, scaling, or monitoring.


FINALLY!!!!!!!
Here are the pages of my application.
1. The Landing page once you run the application
   ![Screenshot (242)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/69ba6f67-ffcb-4eb6-90ff-2dc1fc2c2f69)

2. At the Llanding Page you can Create a NEW  account or Login if you already have an account.
   
      Create an Account(Make sure you upload a profile picture, otherwise you will get error while trying to login)
         ![Screenshot (243)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/2262d8ac-f140-49ba-9d4b-b168b925b713)
         ![Screenshot (265)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/ebcc12c6-584e-4b91-b9f0-668f3496b6e8)
   
      Login
         ![Screenshot (244)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/840da794-5bfc-459b-8c60-484a75f8a251)
         ![Screenshot (245)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/4a448a45-77e4-4b42-aa02-54d801914f75)
   
4. After successful Login, you can Visit the Platform and this is the Homepage
      There is an alert on top of the screen which notifies the user that there is a latest post in PostForum and should probably look at it.
           ![Screenshot (267)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/1f9e5006-2a63-4b2e-85da-9027f13f94c9)
5. Still at the homepage you can read  about Farmerbora and you can also change the language of the content being displayed, i have used the google translator api for that purpose(You can choose either English or Kiswahili)
           ![Screenshot (270)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/98605665-f577-40db-b908-7cd65ee6af25)
           ![Screenshot (271)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/e4125f43-34d2-44b8-884f-cd7b56ba29c7)
 6. If you visit the Diseases page, you will see the following output
         ![Screenshot (248)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/d415bf06-ec8d-4459-8525-6178c0b667bd)
         ![Screenshot (249)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/9fe1d1c9-4dcc-49a2-b6fb-5f47b29f9483)
         ![Screenshot (250)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/71a28428-27b2-4ae6-9e69-45f67bcf6299)
         ![Screenshot (251)
         ![Screenshot (252)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/fd2e4c4e-d724-47e4-aecd-b2ea6c83b4d0)
          ![Screenshot (253)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/1ff10297-b480-4702-9edc-14bb82e41190)
7. The PostForum Page has the following subpages(As a new user, you will be prompted to sign up as an author)As you can see you can see the posts available, the views per each post and the number of comments per each post, you can aslo see who posted and when it was posted. You can also view the exact post and leave your comment(s) or reply to someone's else comment
            ![Screenshot (268)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/d20acce9-5a19-418f-be9e-17c2772701cc)
            ![Screenshot (254)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/48597670-9ac4-4319-a7b1-2b361ba3ff94)
            ![Screenshot (255)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/99a204b3-a9a3-4769-8944-00ebccc59756)
            ![Screenshot (256)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/98b3c116-fe5f-42a5-b8b7-9b231fab1649)
            ![Screenshot (257)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/3b035344-7cbe-4874-b881-3a2318900fcb)
            ![Screenshot (258)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/fa5c2f71-bee7-4626-939d-1fe1063ffa00)
            

8. Still under the PostForum page, you can add a Post by clicking on the plus sign at the top left corner near the menu bar, it will display the post form which you can fill. The tags is just a simple name, any name of your choice for instance, farmer, livestock, veterinary etc
                  For the post to be displayed in the postForum, an admin needs to approve it, the admins will be notified, they can go                    to the database and approve it.
            ![Screenshot (272)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/6447ba5f-b2af-4cf3-9cf5-102eac933545)
            ![Screenshot (273)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/2b44929e-6e24-4a78-9ce4-bc306b3b5c36)
   9. Lastly, while at the postForum, click the menubar and go back home, at the homepage, go to the contact us page, you should see the following pages. If you fill the form and submit it, the farmerBora - LH admis will receive an email and they will respond as soon as possible.
             ![Screenshot (259)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/23c3c065-69d0-4081-9fb1-2e6cfffc7fb9)
               ![Screenshot (260)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/eb4514f9-cc14-4e58-91d0-d060a50398b8)
               ![Screenshot (261)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/e85ffa3c-8d15-4b7d-bb73-e0f69f988020)
               
      
                       
