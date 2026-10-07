install:
	pip install flake8
	pip install mypy
	pip install build

run:
	python3 a_maze_ing.py config.txt

debug:
	python3 -m pdb a_maze_ing.py config.txt

test:
	python3 -m unittest discover -s tests -v

lint:
	python3 -m flake8 .
	python3 -m mypy \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs .

lint-strict:
	python3 -m flake8 .
	python3 -m mypy --strict .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build
	rm -rf dist
	rm -f maze.txt
