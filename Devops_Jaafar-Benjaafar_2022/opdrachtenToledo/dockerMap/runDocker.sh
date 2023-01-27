#!/bin/bash

echo "FROM python" >> Dockerfile
echo "RUN pip install flask" >> Dockerfile
echo "RUN pip install Faker" >> Dockerfile

echo "COPY Micro_Web.py /home/MicroWebFramework/Micro_Web.py" >> Dockerfile
echo "EXPOSE 8080" >> Dockerfile

echo "CMD python3 /home/MicroWebFramework/Micro_Web.py" >> Dockerfile
docker build -t mymicrowebframework .
docker images
docker run -t -d -p 8080:8080 --name myminiserver mymicrowebframework
docker ps -a

