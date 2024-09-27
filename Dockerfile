FROM python:3.11
COPY blink.py ./
RUN pip install lgpio pigpio gpio gpiozero
CMD ["python", "blink.py"]