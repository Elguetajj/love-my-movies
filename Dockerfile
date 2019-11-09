FROM python:3-alpine
COPY myapp /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","./lmm.py"]
