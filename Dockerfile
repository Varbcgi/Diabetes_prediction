FROM python:3.9

WORKDIR /API

RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP=homepage.py



COPY . .

EXPOSE 5000
EXPOSE 8000

CMD [ "bash", "-c", "flask run --host=0.0.0.0 --port=5000 & uvicorn appy:app --host=0.0.0.0 --port=8000 --reload" ]

