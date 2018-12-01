FROM python:3.6.5

RUN mkdir -p /home/project/nompass_app
WORKDIR /home/project/nompass_app
COPY requirements.txt /home/project/nompass_app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/nompass_app

