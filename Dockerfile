# Dockerfile
FROM python:3.12-slim

WORKDIR /app
RUN apt-get update && apt-get install -y curl

COPY . /app/
RUN sed '/-e/d' requirements.lock > requirements.txt
RUN pip install -r requirements.txt

# Run the bot
CMD ["python", "main.py"]

