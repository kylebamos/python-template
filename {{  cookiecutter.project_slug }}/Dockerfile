FROM alpine:3.7

RUN apk add --no-cache \
    bash \
    curl \
    python3 \
    python3-dev \
    make \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip

COPY . /app

WORKDIR /app

RUN make install
