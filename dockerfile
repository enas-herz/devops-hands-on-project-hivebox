FROM python:3.14
WORKDIR /app
COPY project.py .
CMD ["python", "./project.py"]
