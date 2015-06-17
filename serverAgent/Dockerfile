FROM java:8
RUN curl -sL http://jmeter-plugins.org/downloads/file/ServerAgent-2.2.1.zip > /opt/ServerAgent-2.2.1.zip
WORKDIR /opt
RUN unzip ServerAgent-2.2.1.zip
WORKDIR /opt/ServerAgent-2.2.1
ENTRYPOINT "startAgent.sh"