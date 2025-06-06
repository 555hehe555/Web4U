FROM python:3.11

SHELL ["/bin/bash", "-c"]

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install dependencies
RUN pip install --upgrade pip

RUN apt update && apt upgrade -y && \
    apt install -qy gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim && \
    apt clean && rm -rf /var/lib/apt/lists/*


# Set the locale
RUN useradd -rms /bin/bash yt && chmod 777 /opt /run

WORKDIR /yt

RUN mkdir /yt/static && mkdir /yt/media && chown -R yt:yt /yt && chmod -R 755 /yt

COPY --chown=yt:yt . .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y netcat-traditional

USER yt

CMD ["python", "manage.py", "runserver"]
