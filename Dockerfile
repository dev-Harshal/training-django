FROM python:3.8.10
ENV ENV=prod
COPY atomicloops_django-1.0-py3-none-any.whl .
RUN pip install atomicloops_django-1.0-py3-none-any.whl 
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install "drf-yasg[validation]"
RUN pip install git+https://github.com/atomic-loops/atomicloops-django-logger
WORKDIR /opt/
