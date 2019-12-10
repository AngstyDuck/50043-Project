# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /backapp
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 3306 5000 27017

# Set flask env
ENV FLASK_ENV="remoteDev"

# Run app.py when the container launches
CMD python3 -m flask run
