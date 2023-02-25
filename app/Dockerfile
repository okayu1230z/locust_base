FROM python:alpine

ENV PORT 3001

RUN pip install Flask

WORKDIR /app
COPY app.py /app

CMD ["python", "app.py"]