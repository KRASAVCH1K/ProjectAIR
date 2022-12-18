FROM python:3.9

#RUN apt update
# Allows docker to cache installed dependencies between builds
COPY djangoProject1/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY djangoProject1 djangoProject1
ADD .env /env_file/.env
WORKDIR /djangoProject1


RUN python ./manage.py migrate
RUN python manage.py collectstatic

#EXPOSE 8000