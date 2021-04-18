FROM python:3.7.10-alpine3.13
WORKDIR /bilibilijudge
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "Main.py"]