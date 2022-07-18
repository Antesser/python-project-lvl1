install: # установить зависимости
	poetry install

brain-games: #запустить скрипт
	poetry run brain-games

brain-even: #запустить скрипт
	poetry run brain-even

brain-calc: #запустить скрипт
	poetry run brain-calc

brain-gcd: #запустить скрипт
	poetry run brain-gcd	

brain-progression: #запустить скрипт
	poetry run brain-progression	

brain-prime: #запустить скрипт
	poetry run brain-prime	

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

make lint:
	poetry run flake8 brain_games
	