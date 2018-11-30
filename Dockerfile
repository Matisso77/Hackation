FROM ubuntu

RUN apt update
RUN apt -y upgrade
RUN apt -y install python3
RUN apt -y install python3-pip
RUN pip3 install --upgrade pip
RUN apt-get -y install python-virtualenv
RUN apt-get -y install build-essential libssl-dev libffi-dev python3-dev
RUN apt -y install git

RUN mkdir /hackathon
WORKDIR /hackathon

RUN pip3 install django \
                requests \
                psycopg2

RUN git clone "https://github.com/Matisso77/Hackation.git" .
EXPOSE 5000
RUN ls
# cloning git repo and starting flask server
ENTRYPOINT start.sh
