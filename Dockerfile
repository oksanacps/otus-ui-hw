FROM python:3.10.0-alpine

USER root

WORKDIR /root/test

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/root/test \
    PYTHONUNBUFFERED=1

VOLUME /root/test/allure-results

ENTRYPOINT ["pytest", "-v", "--alluredir=/root/test/allure-results"]

CMD ["--vnc"]