install:
	uv snc

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl