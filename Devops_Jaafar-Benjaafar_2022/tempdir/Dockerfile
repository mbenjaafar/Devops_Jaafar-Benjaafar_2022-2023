FROM python
RUN pip3 install flask
RUN pip3 install Flask-OAuthlib
RUN pip3 install ntplib
RUN pip3 install flask-ngrok
COPY ./templates /home/myapp/templates/
COPY flask_ngrok.py /home/myapp/
COPY flask_app.py /home/myapp/
COPY flask_app_test.py /home/myapp/
EXPOSE 5000
CMD python3 /home/myapp/flask_app.py
