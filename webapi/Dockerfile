# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Copy local code to the container image.

# Install production dependencies.
RUN pip install Flask gunicorn

RUN yes | pip install --upgrade pip
RUN yes | pip install --quiet --no-cache-dir \
    pandas \
    matplotlib \
    mecab-python3 \
    sklearn \
    gensim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
CMD python app.py