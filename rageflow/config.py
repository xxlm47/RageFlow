import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    provider=os.getenv("RAGEFLOW_PROVIDER","offline")
    api_base=os.getenv("RAGEFLOW_API_BASE","").rstrip("/")
    api_key=os.getenv("RAGEFLOW_API_KEY","")
    model=os.getenv("RAGEFLOW_MODEL","")
    db=os.getenv("RAGEFLOW_DB","rageflow.db")
    max_sources=int(os.getenv("RAGEFLOW_MAX_SOURCES","20"))
