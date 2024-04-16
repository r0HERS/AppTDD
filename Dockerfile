FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /APPTDD

COPY requirements.txt /APPTDD/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /APPTDD//

CMD python manage.py runserver 0.0.0.0:8000

