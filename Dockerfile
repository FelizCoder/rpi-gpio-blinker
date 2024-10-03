FROM python:3.11
COPY blink.py ./
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "blink.py"]