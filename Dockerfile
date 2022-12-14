FROM python:3.12-rc-slim
EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
COPY static static
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]