# To run app
```
export FLASK_ENV=local
python3 wsgi.py
```
Note that for some reason, running flask run does not change the "__name__" variable to "__main__", even after exporting wsgi.py
This only happens when i run wsgi directly, so for now we're keeping to this.

Currently backend have not been set up with Docker containers yet, so you'll have to install python modules locally first (sorry!)
The modules used are in setup/requirements.txt


# Virtual environment
### To set up virtual environment
1. ```python3 -m venv venvBackend```
2. ```source venvBackend/bin/activate```
3. ```pip3 install -r requirements.txt```

### To update requirements.txt with newly installed modules
1. ```pip3 freeze > requirements.txt```

### To exit virtual environment
1. ```deactivate```
