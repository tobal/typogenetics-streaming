.PHONY: check
check:
	cd typogenetics; \
	python3 -m unittest discover tests

.PHONY: clean
clean:
	cd typogenetics; \
	rm -rf `find . | grep __pycache__`

