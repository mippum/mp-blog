ifeq ($(OS),Windows_NT)
	SCRIPTS := .venv/Scripts
	ORIGIN_PYTHON := python
else
	SCRIPTS := .venv/bin
	ORIGIN_PYTHON := python3
endif

# 로컬 서버 실행 (실시간 미리보기)
serve:
	mkdocs serve

build:
	mkdocs build

deploy:
	$(SCRIPTS)/mkdocs gh-deploy
