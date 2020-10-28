FROM python:3.9.0
FROM ubuntu:18.04
RUN apt-get update && apt-get install -y apt-transport-https
RUN apt-get -y install curl
RUN apt-get -y install wget

# Install any needed packages specified in requirements.txt
RUN curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver
RUN apt-get -y install chromium-browser

RUN apt install -f
WORKDIR /use/src/app



RUN set -xe \
    && apt-get update \
    && apt-get -y install python-pip


RUN pip install --upgrade pip

COPY requirements.txt .
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
ENV VAR1 =1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# Install pip requirements
ADD requirements.txt .
# RUN python -m pip install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /usr/local/bin/
ADD . /usr/local/bin/

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /usr/local/bin/
USER appuser
COPY Tweepy.py .
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug

CMD [ "python", "Tweepy.py" ]