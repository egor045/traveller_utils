init: venv
	( \
		source ./venv/bin/activate; \
    	pip install -r requirements.txt; \
	)

venv: 
	python3 -m venv ./venv

test:
	( \
		source ./venv/bin/activate; \
    	nosetests tests; \
	)

.PHONY: init test
