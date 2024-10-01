#!/usr/bin/env bash

gunicorn_args=(
    --bind=127.0.0.1:8000
    --worker-class=gevent
    --workers=2
    --worker-connections=50
    --max-requests=100
    --timeout=5
    --disable-redirect-access-to-syslog
    --access-logfile=-
    --access-logformat='%(t)s %(p)s %(m)s %(M)s'
)

exec gunicorn "${gunicorn_args[@]}" django_g.wsgi:application
