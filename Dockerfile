FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
  pip install pytest pytest-cov

ENTRYPOINT ["/bin/bash"]
