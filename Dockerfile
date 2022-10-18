FROM python:slim

COPY requirements.txt .
RUN pip install -r requirements.txt && rm requirements.txt

COPY app.py .

ENTRYPOINT ["uvicorn"]
CMD ["app:app", "--host", "0.0.0.0"]
