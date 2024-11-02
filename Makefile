SHELL := $(shell which bash)


deps := llama-index gradio llama-index-llms-ollama llama-index-embeddings-huggingface openpyxl pandas xlrd

venv/init:
	python -m venv .

deps:
	pip install $(deps)

setup:
	mkdir -p resources


run/%:
	python scripts/$*.py


clean:
	rm -rf bin include lib pyenv.cfg
	find . -type d  -name '__pycache__' -exec rm -rf '{}' ';'

process: run/process

