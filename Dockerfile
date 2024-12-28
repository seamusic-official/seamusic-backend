FROM python:3.11.11

COPY . /backend
WORKDIR /backend

ENV PYTHONDONTWRITEBYCODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

CMD ["make", "run-local"]
