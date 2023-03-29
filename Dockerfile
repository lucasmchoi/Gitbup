FROM alpine:3.17
RUN apk add --no-cache git bash python3 py3-pip
RUN pip3 install pyyaml
COPY src /gitbup
RUN mkdir /gitbup/config
RUN mkdir /gitbup/repos
RUN chmod +x /gitbup/entrypoint.sh
ENTRYPOINT ["/gitbup/entrypoint.sh"] 