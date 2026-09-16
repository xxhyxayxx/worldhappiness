# worldhappiness

A small data application built on the World Happiness Report (2015 to 2022): CSV ingestion into a normalised relational model, a REST API with JWT auth, and a React front-end that filters, sorts and charts the indicators by year.

Coursework for the BSc Computer Science (Data Science), University of London (Goldsmiths). Single developer.

## What it does

**Data pipeline**
- Eight yearly CSVs (`backend/data/happiness_2015.csv` to `happiness_2022.csv`) plus a country-to-region mapping
- `import_country` loads countries and regions with `get_or_create`, so it is safe to re-run
- `import_data` walks the data directory, extracts the year from each filename, matches rows to countries, and writes one record per indicator (GDP, social support, life expectancy, freedom, generosity, government trust, happiness score); rows for unknown countries are reported and skipped rather than failing the whole import

**Data model**
- `Country`, `Region`, `Year`, and a `CountryRegion` join table
- One table per indicator, all sharing an abstract `CommonFields` base (country-region and year foreign keys), so each metric can be queried and edited independently

**API (Django REST Framework)**
- JWT login and refresh (SimpleJWT), registration
- Full CRUD for every model behind `IsAuthenticated`
- Swagger docs via drf-yasg

**Front-end (React, Vite)**
- Per-indicator list pages with year filter and sort, and a bar chart (Chart.js via react-chartjs-2) of the selected year
- Add and edit forms for each indicator and for countries
- Custom hooks for fetching, filtering (`useMemo`), form state and submission; zustand for auth state; axios instance with automatic token refresh

## Tests

About 90 back-end tests (models, serializers, views, auth) in `backend/api/tests/`.

```bash
cd backend && python manage.py test
```

## Running locally

```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py import_country
python manage.py import_data
python manage.py runserver
```

```bash
cd frontend
npm install
npm run dev
```

The front-end reads the API base URL from `frontend/src/utils/constants.js`.

## Known issues

- `urls.py` declares each ViewSet route by hand; a DRF `DefaultRouter` would replace most of the file.
- `requirements.txt` was generated with `pip freeze` and includes unused packages (Flask, dash, plotly, pandas).
- Indicator tables are one-per-metric; a single long-format `Indicator` table with a `metric` column would be simpler to extend.
- No front-end tests.

## Notes

Coursework, kept as submitted apart from this README, moving the secret key to an environment variable and removing the committed SQLite database (regenerate it with the two import commands above). Data: World Happiness Report, via the Kaggle mirrors of the 2015 to 2022 editions.