FROM alpine:3.10

COPY entrypoint.sh /entrypoint.sh

RUN apk --update add coreutils && \
    apk --update add jq && \
    apk --update add curl

ENTRYPOINT ["/entrypoint.sh"]
