FROM python:3.8-slim-buster
EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
COPY static static
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]