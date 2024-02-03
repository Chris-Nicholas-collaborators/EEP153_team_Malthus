install:
	python3 -m venv ./venv2; source ./venv2/bin/activate; pip install -r requirements.txt

test:
	source ./venv2/bin/activate; cd test; python3 test_pop.py

lint:
	source ./venv2/bin/activate; flake8 src/team_malthus/pop.py; flake8 test/test_pop.py

