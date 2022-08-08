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
- Add the application created in  the Installed apps under the settings.py file
-run `python manage.py makemigrations bookstore` -> make the db migrations
- apply the migrations using : `python manage.py migrate`
- create admin super user `python manage.py createsuperuser`


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
- create models.py under the projects folder 
- inside the models.py
- run `python manage.py makemigrations bookstore`
- inside the project directory add `admin.py` file and register the added model
- Add the following file to be able to formart its id django admin 
```
    def __str__(self):
        return self.name +""
```

# Using the djangorestframework to attain our data
- Create  serializers.py ( aid in converting python object to json and back)
- define the BooksSerilizer class
```
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'description','bookimage', 'category','favorite', 'pages','authors']
```
- add the rest_framework to Installed Apps 
```
INSTALLED_APPS = [
    'bookstore',
    'rest_framework',
    ....
]
```
# Create your View.py
- Will host the functions/ methods that will run when certain endpoints are called from the urls.py 
- create views.py in the projects directory
- add the respective urls in the urls.py file





# NOTE: 
 - The REST Architecture is used here. 