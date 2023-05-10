FROM python:3.10.11-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

# install pillow
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "Client.py" ]