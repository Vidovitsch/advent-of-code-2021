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

.PHONY: day_08
day_08: ensure-poetry
	@poetry run python ./solutions/day_08/main.py

.PHONY: day_09
day_09: ensure-poetry
	@poetry run python ./solutions/day_09/main.py

.PHONY: day_10
day_10: ensure-poetry
	@poetry run python ./solutions/day_10/main.py

.PHONY: day_11
day_11: ensure-poetry
	@poetry run python ./solutions/day_11/main.py

.PHONY: day_12
day_12: ensure-poetry
	@poetry run python ./solutions/day_12/main.py

.PHONY: day_13
day_13: ensure-poetry
	@poetry run python ./solutions/day_13/main.py

.PHONY: day_14
day_14: ensure-poetry
	@poetry run python ./solutions/day_14/main.py

.PHONY: day_15
day_15: ensure-poetry
	@poetry run python ./solutions/day_15/main.py

.PHONY: ensure-poetry
ensure-poetry:
	$(call check-command,docker,`poetry` is required. It can be installed using pip install poetry)
