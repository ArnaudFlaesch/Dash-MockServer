FROM python:3.12.7-alpine3.20
EXPOSE 5000

RUN adduser --system --no-create-home dockeruser
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
COPY static static

USER dockeruser
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
