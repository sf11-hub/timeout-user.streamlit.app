install: 
	 python -m pip install poetry
	 poetry install

run:
	 poetry run streamlit run app.py