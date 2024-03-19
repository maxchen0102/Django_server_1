# Use an official Python runtime as the base image
FROM python:3.12.0

# Set environment variables
#ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file from the current directory on your host machine
# to the /app directory inside the Docker container
COPY requirements.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port on which the Django app will run
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver"]
