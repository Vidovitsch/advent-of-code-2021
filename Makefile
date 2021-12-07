.DEFAULT_GOAL=default

.PHONY: default
default: day_01

.PHONY: day_01
day_01: ensure-poetry
	@poetry run python ./solutions/day_01/main.py

.PHONY: day_02
day_02: ensure-poetry
	@poetry run python ./solutions/day_02/main.py

.PHONY: day_03
day_03: ensure-poetry
	@poetry run python ./solutions/day_03/main.py

.PHONY: day_04
day_04: ensure-poetry
	@poetry run python ./solutions/day_04/main.py

.PHONY: day_05
day_05: ensure-poetry
	@poetry run python ./solutions/day_05/main.py

.PHONY: day_06
day_06: ensure-poetry
	@poetry run python ./solutions/day_06/main.py

.PHONY: day_07
day_07: ensure-poetry
	@poetry run python ./solutions/day_07/main.py

.PHONY: ensure-poetry
ensure-poetry:
	$(call check-command,docker,`poetry` is required. It can be installed using pip install poetry)
