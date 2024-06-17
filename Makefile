.PHONY: install test run

install:
    pip install -r requirements.txt

test:
    python -m unittest discover

run:
    python api_test.py
