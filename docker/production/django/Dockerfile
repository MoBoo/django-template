FROM python:3.8
ARG APP_DIR=/app
WORKDIR ${APP_DIR}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Add user
RUN addgroup --system django && adduser --system --ingroup django django

# Install system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Copy files
COPY --chown=django:django . ${APP_DIR}

# Install python dependencies
RUN pip install --no-cache-dir -r requirements/production.txt

COPY --chown=django:django ./docker/production/django/entrypoint.sh /entrypoint
RUN chmod +x /entrypoint

COPY --chown=django:django ./docker/production/django/start.sh /start
RUN chmod +x /start

USER django

ENTRYPOINT ["/entrypoint"]