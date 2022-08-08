# Set up 
- mkdire BookStore && cd BookStore
- pipenv install django
- activate python env `pipenv shell`
- django-admin startproject bookstore
- Test the fella 🤘🏻, `python manage.py runserver`
- set up youproject environment to runb when you launch the vscode terminal : 
 launch vscode (if you are usaing vscode) the  :
    *  ctrl + P ( opens a search section on vscode )
    *  search >python intepreter then select it then select '*Enter path option*'
    * on terminal window - open via vscode run `pipenv --venv` it will print out a path, copy it and paste it at the search section open on your- run `python manage.py migrate` : applies all table migrations

- Install djangorestframework ( will help build and design the rest api)  : `pip install djangorestframework`

## Simple API CheckList : 
  - [x] Models ( help organmize and create our data model)
  - [x] Views ( create methods /funtions attached to the target HTTP CRUD verbs/ related endpoints)
  - [x] Urls (create End points)
  - [x] Serializers ( Allow serialization of data from python object to json format anbd back)
  - [x] Admin Panel Setup & Update  ( our "god"-like of medium to see everything)
  - [x] Addition of capability to attain json query using
   ```urlpatterns = format_suffix_patterns(urlpatterns) # Allows you to query wit the .json line
   ```


# Part Create the Book Models : 


# NOTE: 
 - The REST Architecture is used here. 