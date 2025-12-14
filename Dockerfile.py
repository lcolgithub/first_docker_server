FROM debian:stable-slim
COPY main.py main.py
COPY books/ books/

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["python3", "main.py"]

