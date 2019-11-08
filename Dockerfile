FROM python:3-alpine

COPY myapp /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python","lmm.py"]
