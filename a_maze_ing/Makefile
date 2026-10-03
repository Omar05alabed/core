install:
	pip install mypy
	pip install flake8
	pip install build
run:
	python a_maze_ing.py config.txt

debug:
	python -m pdb a_maze_ing.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf build
	rm -f maze.txt
	
lint:
	python3 -m flake8 .
	python3 -m mypy \
	--warn-return-any \
	--warn-unused-ignores \
	--ignore-missing-imports \
	--disallow-untyped-defs \
	--check-untyped-defs

lint-strict:
	python3 -m flake8 .
	python3 -m mypy --strict .
