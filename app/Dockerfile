FROM python:latest
WORKDIR /code
RUN pip install kubernetes
COPY app.py app.py
CMD ["python", "-u", "app.py"]