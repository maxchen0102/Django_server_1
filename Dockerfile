# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
# 可以隨意定義 就像是建立新資料夾(in docker )
WORKDIR /code
#複製當前層級所有的資料 到docker
COPY . /code/

# Install pip
RUN apt-get update && apt-get install -y python3-pip

RUN pip install -r requirements.txt

# Expose the port the Django app runs on
EXPOSE 8000

# Run the Django development server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# 指定任何ip 都可以連接到docker 的8000 port
CMD python manage.py runserver 0.0.0.0:8000
