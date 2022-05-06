FROM python:3

COPY model.json .
COPY app.py .

RUN pip install Flask scikit-learn

CMD [ "python", "app.py" ]