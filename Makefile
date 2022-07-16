install: # установить зависимости
	poetry install

brain-games: #запустить скрипт
	poetry run brain-games

brain-even: #запустить скрипт
	poetry run brain-even	

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
	