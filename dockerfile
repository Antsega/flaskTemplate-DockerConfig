# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /FLASK_APP

# Add the current dir contents into the container at /app
ADD . /FLASK_APP

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn separately
RUN pip install gunicorn

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["gunicorn", "-b", ":8080", "app:app"]