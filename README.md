# course-reg

# install all packages

pip install -r requiments.txt 

# create db schema in django
python manage.py makemigrations

# migrate the schema to postgres
python manage.py migrate

# run the server
python manage.py runserver