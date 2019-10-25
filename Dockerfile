# Use an official Python runtime as an image
FROM python:3.7

# The EXPOSE instruction indicates the ports on which a container # # will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 5000

WORKDIR /app/backend

# Install any needed packages specified in requirements.txt
COPY installation_files/requirements.txt /app/backend
RUN pip install -r requirements.txt
RUN pip install PyMySQL[rsa]

COPY backend /app/backend
COPY data_analytics /app/data_analytics
COPY installation_files /app/installation_files


COPY ./amazon.sql /app/backend/

CMD mysql -u user -ppassword -e "SET autocommit=0;" AMAZON < amazon.sql

#AS OF NOW 25-10-2019, MOST UPDATED
WORKDIR /app/backend/reviews
CMD export FLASK_APP=reviews
