from pydantic import BaseModel
from typing import List


class ConstituencyResponse(BaseModel):
    province: str
    constituencies: List[str]
