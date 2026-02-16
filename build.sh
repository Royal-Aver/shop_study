#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata fixtures/category.json || true
python manage.py loaddata fixtures/product.json || true