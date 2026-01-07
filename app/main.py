from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.scraper import scrape_zambia_constituencies
from app.cache import get_cache, set_cache
from app.schemas import ConstituencyResponse
from app.utils import find_province_by_constituency


app = FastAPI(title="Zambia Constituencies API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_data():
    cached = get_cache()
    if cached:
        return cached

    try:
        data = scrape_zambia_constituencies()
        set_cache(data)
        return data
    except Exception:
        if cached:
            return cached
        raise


@app.get("/api/provinces")
def get_provinces():
    data = load_data()
    return sorted(data.keys())


@app.get("/api/constituencies")
def get_all_constituencies():
    return load_data()


@app.get("/api/constituencies/{province}", response_model=ConstituencyResponse)
def get_constituencies_by_province(province: str):
    data = load_data()

    if province not in data:
        raise HTTPException(status_code=404, detail="Province not found")

    return {
        "province": province,
        "constituencies": data[province],
    }


@app.get("/api/constituency/{name}")
def get_province_by_constituency(name: str):
    data = load_data()

    province = find_province_by_constituency(data, name)

    if not province:
        raise HTTPException(status_code=404, detail="Constituency not found")

    return {
        "constituency": name,
        "province": province,
    }
