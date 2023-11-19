setup:
	 python -m pip install poetry
	 poetry install --no-root

run:
	 poetry run streamlit run app.py