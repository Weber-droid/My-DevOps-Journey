FROM python:3.9-slim

WORKDIR /my_flask_app

COPY ./my_flask_app /app

RUN pip install --no-cache-dir -r ./requirements.txt

EXPOSE 5000

ENV FlASK_APP = app.py

CMD ["flask", "run", "--host=0.0.0.0"]