# Use an official Python runtime as a parent image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt update && apt update

#install luminati on localhost
#RUN curl -L https://luminati.io/static/lpm/luminati-proxy-latest-setup.sh | bash
#RUN apt-get install nodejs
#RUN luminati --www_whitelist_ips "172.17.0.1" --ssl true --deamon

ADD . .
# Make port 80 available to the world outside this container
ENV LISTEN_PORT 80 443 22225 22999
EXPOSE 80 443 5432 27017 4444 22225 22999

ENV DISPLAY=:99

ENV PYTHONPATH "${PYTHONPATH}:/app:/app/app"
# Set the default command to run when starting the container
CMD ["python", "app/main.py"]
