install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl
	
publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

