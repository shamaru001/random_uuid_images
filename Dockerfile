FROM python:3.6-alpine
ENV PORT 8080
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT flask run --host=0.0.0.0 --port=$PORT