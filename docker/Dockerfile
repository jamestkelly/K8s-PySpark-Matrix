FROM python:3.8

RUN mkdir /app
WORKDIR /app
ADD app /app
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]