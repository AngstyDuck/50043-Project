from ubuntu:18.04

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y python3-pip git wget zip curl
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install -y git-lfs
RUN git lfs install


RUN git clone https://github.com/SolsticeDante/50043-Project-lfs.git ./50043-project-lfs
RUN git clone https://github.com/dinhtta/istd50043_project.git ./50043-prof

RUN chmod 777 ./50043-prof/scripts/get_data.sh
RUN ./50043-prof/scripts/get_data.sh

RUN mkdir ./setup

COPY ./setup/requirements.txt ./
RUN pip3 install --no-cache-dir -r ./requirements.txt

ENV FLASK_APP reviews/reviews.py

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY . .
EXPOSE 5000

CMD flask run
