# FarmerBora
Welcome to FarmerBora Project. For this project project i used the Django Web Framework.To run this project using any terminal follow the following steps:
1. The first step is to create a Virtual Environment(Am assuminmg you are using version 3 of python)
        python3 -m venv (name of your virtual environment) for instance
        python3 -m venv env       The name of my virtual encironment is env
2. Activate the virtual environment
        . On Windows
        env\Scripts\activate

        .On MacOS nad Linux(for those who will choose to use the Ubuntu terminal)
        source env/bin/activate
3. Within the virtual environment clone my reposiotry
        i. Ensure git is activated within the virtual environment
                git init
        ii. Now clone repository 
                git clone https://github.com/mulimuoki001/FarmerBora.git
4. Install all the Dependencies(Run the following commands to run all the necessary requirements for the app to run)
        pip install -r requirements.txt

5. Create a Super user(This is optional, only if you want to access the database with super user privilleges)
        python 3manage.py createsuperuser
Run the Development server
        python3 manage.py runserver

To access the Application Open the browser and go to  http://127.0.0.1:8000 to see the running Django Application