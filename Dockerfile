FROM python:3.14@sha256:a2f0ffaafb5db81c0583026054d9290ef210a6bd614acad35ea483fea0cbcab2
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY project.py .
COPY hivebox.py .
CMD ["python", "-m", "flask", "--app", "./hivebox.py", "run", "--host=0.0.0.0"]