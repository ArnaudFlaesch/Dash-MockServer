FROM python:3.12-rc-slim
EXPOSE 5000

RUN groupadd -g 999 dockerfileUser && \
    useradd -r -u 999 -g dockerfileUser dockerfileUser
USER dockerfileUser

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
COPY static static
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]