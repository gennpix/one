FROM python:3.9.6-alpine3.14

COPY pip.conf /root/.pip/pip.conf
COPY . /root/python_django_demo
WORKDIR /root/python_django_demo
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
