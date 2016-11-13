FROM fedora:23

ADD . /opt/spy-007
WORKDIR /opt/spy-007
RUN pip3 install --requirement requirements.txt \
    && python3 server.py
