# To set up
```
python3 wsgi.py
```
Note that for some reason, running flask run does not change the "__name__" variable to "__main__", even after exporting wsgi.py
This only happens when i run wsgi directly, so for now we're keeping to this.

Currently backend have not been set up with Docker containers yet, so you'll have to install python modules locally first (sorry!)
The modules used are in setup/requirements.txt

