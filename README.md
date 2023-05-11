**REST API building using Django and PostgreSQL** 

## System Configuration

* Ubuntu `20.04` **(Recommended)**
* *OR* WSL for Windows `10` \(Follow the guide below\) :  
    [Windows Subsystem for Linux Installation Guide for Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
* *OR* Windows `7/8/8.1/10/11`

## Software Requirements

* Python `3.8`

* Git

* PostgreSQL `15.1`

* A web browser(Chrome, Edge)

## How to get started

* on **Ubuntu**:

    ```sh
    // Install the required packages using the following command:
    
    sudo apt install python3-pip python3-dev python3-venv libpq-dev build-essential git
    sudo -H pip3 install --upgrade pip
    ```

* on **Windows**:

  * Get Python 3.8 from [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe) for AMD64/x64 or [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe) for x86
  * Git from [here](https://git-scm.com/download/win)
  * Install both using the downloaded `exe` files   
  **Important:** Make sure to check the box that says **Add Python 3.x to PATH** to ensure that the interpreter will be placed in your execution path

### Setting up environment

* Create a virtual environment  
  * on **Ubuntu**: `python3 -m venv env`  
  * on **Windows PowerShell**: `python -m venv env`
* Activate the *env*    
  * on **Ubuntu**: `source env/bin/activate`
  * on **Windows PowerShell**: `.\env\Scripts\Activate.ps1`     
  **Note** : On Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following command: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
* Install the requirements: `pip install -r requirements.txt`

### Database integration 
* Create a PostgreSQL database and configure the settings in the backend/settings.py file in the DATABASES section.

### Migrating Changes (Database)

* Make migrations `$ python manage.py makemigrations`  
* Migrate the changes to the database `$ python manage.py migrate`

### Running server

* Change directory to **backend** `cd backend`
* Run the server `python manage.py runserver`

### Testing The API

* Open the crud.html file present in the frontend directory to perform the CRUD operations on the data present in the      
  database.
  


