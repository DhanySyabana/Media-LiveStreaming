FROM python:3.10.11

ENV DEBIAN_FRONTEND=noninteractive
ARG ENGINE
WORKDIR /app

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# install apt-utils & pillow requirements
RUN apt-get install -y apt-utils libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5

# Magic happens
RUN apt-get install -y google-chrome-stable

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

# install FFMPEG
RUN apt-get install -y ffmpeg

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install cloudscraper
RUN pip install pusher
RUN pip install -U --pre "yt-dlp[default,deno]"

COPY . .

CMD [ "python", "${ENGINE}" ]