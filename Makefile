.DEFAULT_GOAL=default

.PHONY: default
default: 1_1

.PHONY: 1_1
1_1: ensure-poetry
	@poetry run python ./solutions/day_01/part_1.py

.PHONY: 1_2
1_2: ensure-poetry
	@poetry run python ./solutions/day_01/part_2.py

.PHONY: 2_1
2_1: ensure-poetry
	@poetry run python ./solutions/day_02/part_1.py

.PHONY: 2_2
2_2: ensure-poetry
	@poetry run python ./solutions/day_02/part_2.py

.PHONY: 3_1
3_1: ensure-poetry
	@poetry run python ./solutions/day_03/part_1.py

.PHONY: 3_2
3_2: ensure-poetry
	@poetry run python ./solutions/day_03/part_2.py

.PHONY: 4_1
4_1: ensure-poetry
	@poetry run python ./solutions/day_04/part_1.py

.PHONY: 4_2
4_2: ensure-poetry
	@poetry run python ./solutions/day_04/part_2.py

.PHONY: 5_1
5_1: ensure-poetry
	@poetry run python ./solutions/day_05/part_1.py

.PHONY: 5_2
5_2: ensure-poetry
	@poetry run python ./solutions/day_05/part_2.py

.PHONY: 6_1
6_1: ensure-poetry
	@poetry run python ./solutions/day_06/part_1.py

.PHONY: 6_2
6_2: ensure-poetry
	@poetry run python ./solutions/day_06/part_2.py

.PHONY: 7_1
7_1: ensure-poetry
	@poetry run python ./solutions/day_07/part_1.py

.PHONY: 7_2
7_2: ensure-poetry
	@poetry run python ./solutions/day_07/part_2.py

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

.PHONY: 15_1
15_1: ensure-poetry
	@poetry run python ./solutions/day_15/part_1.py

.PHONY: 15_2
15_2: ensure-poetry
	@poetry run python ./solutions/day_15/part_2.py

.PHONY: ensure-poetry
ensure-poetry:
	$(call check-command,docker,`poetry` is required. It can be installed using pip install poetry)
