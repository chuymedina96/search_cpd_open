# Welcome to the source code for searchCPD
## Below you will find information and details on how to clone the repo and set it up on your own system
* Project production url: https://www.searchcpd.io
* This project uses Django 3.0.5.
* This project is mainly a grassroots social justice oriented data science project aimed at holding police officer accountable.
* This project is more for community members so they can determine the officers in their communites that are high risk of abusing their authority.
* It is recommended that you be knowledgeable of virtual environments with python and pip(python's package manager)
* This project does not come with the necessary settings.py file which is critical to starting the django project on your system.
* Contact me for the settings.py file and I will be glad to send over in order for the project to run.
* This project uses FOIA requested Data from the Chicago Police Department. You can request the same data from your own police department. Contact us and we can provide a template for requesting data from any police department.

## Requirements
1. Python 3 should be installed on your system.
2. PIP should be installed.
3. Python Virtualenv


## Below are detailed steps on how to set things up with django.
1. Download or clone repo.
2. Next, navigate to the project directory and create your virtual environment. Go ahead and activate the virtual environment. 
- For mac:
```bash
source <YOUR_VIRTUAL_ENV>/bin/activate  
```
- For Windows:
```bash
call <YOUR_VIRTUAL_ENV>/Scripts/activate  
```

- If you are unfamiliar with virtual environments, check out this awesome tutorial from Corey Schafer: https://www.youtube.com/watch?v=N5vscPTWKOk

3. Once you get your virtual environment activated, you can install all necessary software dependencies by running:
```bash
pip install -r requirements.txt
```

4. After that, you should have all software dependencies installed, all that is left is to place your settings.py file within your projects directory. If you are familiar with Django, then you should know where to place it. 

5. Once that is hooked up, you can try running migrations:
```bash
python manage.py migrate
```
### THEN:

```bash
python manage.py makemigrations
```
6. Finally, try starting the server!
```bash
python manage.py runserver
```

## NOTE:
* Within your views.py file within the search folder contained within the apps folder, you will have to modify the file system path to the csv file that contains all the officer data.
* Change the path to meet your system path, then when you hit the populate method/route, the database should populate with all the data.


