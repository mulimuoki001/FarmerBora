# FarmerBora
Welcome to FarmerBora Project. For this project project i used the Django Web Framework.To run this project using any terminal follow the following steps:
1. The first step is to create a Virtual Environment(Am assuminmg you are using version 3 of python)
        python3 -m venv <name of your virtual environment> for instance
        python3 -m venv env       The name of my virtual encironment is env
   ![Screenshot (231)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/0a6b6b1a-fa2c-4ec5-8c35-b57a8b575751)
   
3. Activate the virtual environment
        . On Windows
        	env\Scripts\activate

        .On MacOS nad Linux(for those who will choose to use the Ubuntu terminal)
        	source env/bin/activate
    ![Screenshot (232)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/bef83d93-24bf-4f45-b51d-f0765fd7598e)

5. Within the virtual environment clone my reposiotry
        i. Ensure git is activated within the virtual environment
   		 git init
        ii. Now clone repository 
                git clone https://github.com/mulimuoki001/FarmerBora.git
        
   ![Screenshot (233)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/55939bbd-4181-4284-ad1c-6b79ce160c31)
6. Install all the Dependencies(Run the following commands to run all the necessary requirements for the app to run)
           pip install -r requirements.txt


![Screenshot (234)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/bd53f5a6-5b99-43e7-9e89-41319fe20a5a)
![Screenshot (235)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/03bb9c5c-55a2-4e80-b1bf-3a746c47d75b)
![Screenshot (236)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/c12e7ec4-aace-4361-99ff-809262e6477b)
![Screenshot (237)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/7d89b0f4-67bb-47e3-af0e-fdcf28b3b0c0)
7. Create a Super user(This is optional, only if you want to access the database with super user privilleges)
        python 3manage.py createsuperuser

   ![Screenshot (238)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/948219fb-06b8-4b86-80c4-0872086b9e27)

8. Run the Development server
        python3 manage.py runserver
        ![Screenshot (239)](https://github.com/mulimuoki001/FarmerBora/assets/116681226/6828fc70-b6b6-41e6-abd6-5cb85b4e61d1)
To access the Application Open the browser and go to  http://127.0.0.1:8000 to see the running Django Application
