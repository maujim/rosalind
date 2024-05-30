test:
	python3 -m unittest --failfast --verbose main.py

format:
	black main.py
