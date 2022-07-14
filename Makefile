app_name = comics_store_app

check:
	@git add .
	@pre-commit

test:
	@pytest -vv
