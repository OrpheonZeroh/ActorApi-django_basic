FROM python:3.7-slim

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /appi

# Set the working directory to /music_service
WORKDIR /appi

# Copy the current directory contents into the container at /music_service
ADD . /appi/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt