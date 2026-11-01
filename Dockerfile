FROM python:3.15.2-alpine3.23

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
RUN adduser --system --no-create-home dockeruser

COPY requirements.txt .
RUN pip3 install --no-cache-dir --require-hashes --only-binary :all: -r requirements.txt
COPY app.py .
COPY static static

USER dockeruser
EXPOSE 5000
CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]
