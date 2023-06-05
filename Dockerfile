FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

CMD [ "python3", "SE_Sample_File.py" ]
