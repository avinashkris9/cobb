all: help
default: help
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))

help: ## Show help messages for make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}'

setup: ## Install dependencies via UV
	uv install

fmt: ## Format code using ruff
	uv run ruff Format

lint: ## Lint code using ruff
	uv run ruff check

run: ## Run Cobb CLI
	uv run cobb

run_slack: ## Run Cobb Slack bot
	uv run cobb-slack

test: ## Run tests
	uv run pytest tests


deploy:
	uv build