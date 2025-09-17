FROM python:3.8-slim-buster
RUN apt-get update && apt-get install -y build-essential
RUN pip install --upgrade pip && pip install awscli
WORKDIR /app


COPY . /app
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate
RUN apt-get remove -y build-essential && apt-get autoremove -y && apt-get clean

CMD ["python", "app.py"]
