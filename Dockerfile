# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Copy project
COPY . /app/

# Install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev \
    && apt-get install -y libpq-dev 

# Add and install Python packages
COPY requirements.txt /app/
RUN pip install --upgrade pip

# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
