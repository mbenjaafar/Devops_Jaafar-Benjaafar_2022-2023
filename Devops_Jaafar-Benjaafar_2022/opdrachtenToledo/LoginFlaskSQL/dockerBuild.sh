#!/bin/bash

mkdir tempdir
mkdir tempdir/templates

cp flask_app.py tempdir/.
cp flask_app_test.py tempdir/.
cp -r templates/* tempdir/templates/. 

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip3 install flask" >> tempdir/Dockerfile
echo "RUN pip3 install Flask-OAuthlib" >> tempdir/Dockerfile
echo "RUN pip3 install ntplib" >> tempdir/Dockerfile
echo "RUN pip3 install flask-ngrok" >> tempdir/Dockerfile




echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile 
echo "COPY flask_app.py /home/myapp/" >> tempdir/Dockerfile
echo "COPY flask_app_test.py /home/myapp/" >> tempdir/Dockerfile


echo "EXPOSE 5000" >> tempdir/Dockerfile

echo "CMD python3 /home/myapp/flask_app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t inloggenapp .
docker run -t -d -p 5000:5000 --name myinloggenapp inloggenapp
docker ps -a

curl http://localhost:4040/api/tunnels 