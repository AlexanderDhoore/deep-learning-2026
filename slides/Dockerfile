FROM python:3.12.10

ARG QUARTO_VERSION=1.7.31

WORKDIR /data

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install jupyter matplotlib plotly

RUN wget -q "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb" \
      -O /tmp/quarto.deb \
    && apt-get update \
    && apt-get install -y /tmp/quarto.deb \
    && rm /tmp/quarto.deb \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8080

CMD quarto preview /data/$QUARTO_FILE --port 8080 --host 0.0.0.0

