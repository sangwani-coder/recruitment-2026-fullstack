# 🇿🇲 Zambia Constituencies Explorer

A full‑stack junior engineer take‑home assignment that tests **web scraping, API design, frontend fundamentals, testing, and deployment** using real public data from the National Assembly of Zambia.

---

## Project Objective

Build and deploy a small full‑stack application that:

1. Scrapes **Zambian provinces and constituencies** from the National Assembly website
2. Exposes the data via a **REST API**
3. Displays the data using a **minimal frontend (HTML/CSS/JS)**
4. Includes **automated tests**
5. Is **publicly deployed**

This assignment is designed to simulate a **real‑world junior engineering task** rather than a purely academic exercise.

---

## Tech Stack (Required)

### Backend

* Python 3.10+
* FastAPI
* Requests
* BeautifulSoup4
* Pytest

### Frontend

* HTML
* CSS
* Vanilla JavaScript (no frameworks)

### Deployment

* Backend: Render / Railway / Fly.io (any one)
* Frontend: GitHub Pages / Netlify / Render static

---

## Project Structure

```
zambia-constituencies/
├── app/
│   ├── main.py            # FastAPI app & routes
│   ├── scraper.py         # Web scraping logic
│   ├── cache.py           # Simple in-memory cache
│   └── schemas.py         # API response schemas
├── tests/
│   ├── conftest.py
│   ├── test_scraper.py
│   ├── test_api.py
│   └── test_frontend_contract.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── requirements.txt
├── pytest.ini
└── README.md
```

---

##  Getting Started (Local Setup)

### Clone the Repository

```bash
git clone git@github.com:sangwani-coder/recruitment-2026-fullstack.git
cd zambia-constituencies
```

---

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run the Backend API

```bash
uvicorn app.main:app --reload
```

API will be available at:

```
http://localhost:8000
```

Interactive API docs:

```
http://localhost:8000/docs
```

---

### Run the Frontend

Simply open:

```
frontend/index.html
```

> ⚠️ Make sure the API is running before using the frontend.

---

## API Endpoints

### `GET /api/provinces`

Returns a list of province names.

**Response**

```json
[
  "Central",
  "Copperbelt",
  "Eastern",
  "Luapula",
  "Lusaka",
  "Muchinga",
  "Northern",
  "North-Western",
  "Southern",
  "Western"
]
```

---

### `GET /api/constituencies`

Returns all provinces and their constituencies.

**Response**

```json
{
  "Central": ["Bwacha", "Chisamba"],
  "Lusaka": ["Kanyama", "Matero", "Munali"]
}
```

---

### `GET /api/constituencies/{province}`

Returns constituencies for a single province.

**Example**

```
GET /api/constituencies/Lusaka
```

**Response**

```json
{
  "province": "Lusaka",
  "constituencies": [
    "Chilanga",
    "Chawama",
    "Kabwata",
    "Kanyama",
    "Matero",
    "Munali"
  ]
}
```

**Error (404)**

```json
{
  "detail": "Province not found"
}
```

---

---

### `GET /api/constituency/{name}`

Returns the province for a given constituency (case-insensitive).

**Example**

```
GET /api/constituency/Matero
```

**Response**

```json
{
  "constituency": "Matero",
  "province": "Lusaka"
}
```

**Error (404)**

```json
{
  "detail": "Constituency not found"
}
```

---


## Running Tests

All tests **must pass** before submission.

```bash
pytest
```

Test coverage includes:

* Scraper correctness
* API behaviour
* Frontend ↔ API contract

---

## Deployment Requirements

You must deploy **both backend and frontend**.

### Backend

* Deployed API must be publicly accessible
* Example platforms: Render, Railway, Fly.io

### Frontend

* Must consume the **live API**, not localhost
* Example platforms: GitHub Pages, Netlify

---

## Submission Checklist

Before submitting, ensure:

* [ ] All tests pass locally
* [ ] Backend is deployed
* [ ] Frontend is deployed
* [ ] Frontend uses deployed API URL
* [ ] README updated with live URLs

---

## Add Your Deployment URLs Here

```text
Backend API URL: https://your-api-url
Frontend URL: https://your-frontend-url
```

---

## Bonus (Optional)

You may optionally add:

* Frontend search/filter
* Rate limiting
* CI pipeline (GitHub Actions)

Bonus features are **not required** but may improve your evaluation.

---

## Anti-Cheating & Integrity Checks

To ensure this assignment reflects your own work and real problem-solving ability, the following rules apply:

**❌ Hardcoding Is Not Allowed**

- Constituency or province data must not be hardcoded in the API, utilities, or tests
- Data must come from the scraper at runtime (or its cache fallback)

**❌ External APIs or Data Files**

- Do not use third-party APIs, static JSON files, or copied datasets
- The National Assembly website is the single source of truth

**❌ Bypassing or Weakening Tests**

- Do not modify existing tests to make them pass
- Do not mock scraper results in production code

**❌ One-off Special Cases**

- Solutions that only work for one province or known constituency will fail evaluation

**⚠️ Plagiarism**

- Submissions may be checked for similarity against other candidates
- You can only source code from offical **Documentations** or **tutorials**.
- Make sure you understand every code you write.


## Evaluation Criteria

| Area                   | Weight 	| Description |
| ---------------------- | -------- | ------------ |
| API correctness        | ⭐⭐⭐⭐ | Endpoints behave as specified, return correct data, handle errors properly (404s, failures), and follow the documented contract.|
| Code clarity           | ⭐⭐⭐  	| Code is readable, well-structured, logically organized, and appropriately commented without over-engineering.|
| Testing                | ⭐⭐⭐⭐	| All provided tests pass; candidate demonstrates understanding of test intent and does not bypass or weaken tests.|
| Frontend functionality | ⭐⭐    	| Frontend successfully consumes the API, updates UI dynamically, and handles loading/error states gracefully.|
| Deployment             | ⭐⭐     | Backend and frontend are deployed, publicly accessible, and correctly wired together using live URLs.|

---

## Notes

* Focus on **clarity and correctness**, not over‑engineering
* Write readable code
* Handle errors gracefully
* Commit regularly with meaningful messages

Good luck 🚀
