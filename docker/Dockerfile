FROM python:3.9

RUN apt-get update && \
apt-get upgrade -y && \
python -m pip install --upgrade pip

WORKDIR /usr/src/my_service
COPY app app/
COPY server.py .
COPY .env .
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry==1.3 && \
poetry export -f requirements.txt --output requirements.txt && \
pip install -r requirements.txt

RUN groupadd -g 999 apiuser && \
useradd -r -u 999 -g apiuser apiuser
USER apiuser

EXPOSE 5001

CMD python server.py
