# TaskApp
Allows the user to add a picture along with a name, address, city and a selected point on a map, this information is then displayed on a map along with the picture. The information is also displayed in a list under the map and the user can filter the results by using the provided search functionality.


# Technologies used
Django web framework
GeoDjango
Postgres database
Psycopg2
Python
HTML/CSS
Javascript
Bootstrap
Leaflet


# Requirements
After cloning this project the following must be installed:
Django
psycopg2
Python
PostgreSQL (remember the password you used while setting this up)
PostGIS (select this spatial extension during the installation of PostgreSQL)
GeoDjango requires a set of open-source geospatial libraries:

GEOS is an open-source geometry engine and a C++ port of the JTS (Java Topology Suite). It’s required by GeoDjango for performing geometric operations.

PROJ.4 is an open-source GIS library for easily working with spatial reference systems and projections. You need it because you’ll be using PostGIS as the spatial database.

GDAL is an open-source geospatial data abstraction library for working with raster and vector data formats. It’s needed for many utilities used by GeoDjango.

# Configuring Database
Once PostgreSQL is downloaded and you installed PostGIS during the install. Open the pgAdmin user interface and create a new database called 'Lost_Pets', once this is created, click on the arrow to the left of the Lost_Pets database and then right click on extensions and create a new extension called postgis.

Please open settings.py and enter your PostgreSQL password in to the databases section which looks like the following:

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'Lost_Pets',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

Now cd into the taskapp folder and run the following commands in the terminal to create the database tables:

$ python manage.py makemigrations
$ python manage.py migrate

$ python manage.py createsuperuser (this will ask you to create an admin account)

# Run Application
You should now be able to run the server and start using the app, use the following command in order to run the server:

$ python manage.py runserver

You should then be able to access the application in your browser at http://localhost:8000/.





