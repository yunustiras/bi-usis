FROM python:3.6
COPY . /code
WORKDIR /code
RUN pip install pipenv
RUN pipenv install --system
CMD ["python", "web/run.py"]
