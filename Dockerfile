FROM python:3.8-slim-buster
RUN pip install --upgrade pip && pip install awscli
WORKDIR /app


COPY . /app
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip install uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python", "app.py"]
