

 The app allows you to add blogs after signup from frontend ,users can add comments to a specific blog  .It has a login feature.

##  Starting the Project


1. Create a **virtual environment** with venv (install virtualenv, if its not installed).

    ```
    venv blogapp

    ```

2. Clone the project in the virtual environment directory.

    ```
    cd blogapp
    git clone https://github.com/kgulshan827/Blogapp11.git

    ```

3. Activate the virtual environemnt.

    #### For Linux/Mac OSX   
    ```
    source bin/activate

    ```

    #### For Windows
    ```
    .\Scripts\activate

    ```

4. Install the requirements.

    ```
    cd bloagpp
    pip install -r requirements.txt

    ```


5. Run the Migrations
    ```
    python manage.py makemigrations

    python manage.py migrate

    ```
6. Run the development server
    ```
    python manage.py runserver

    ```
7. Head to server http://localhost:8000

8. Add blogs after signup 

## For contributors

Blogapp uses the following technologies:

+ HTML/CSS
+ Pyhton(Django)



