from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import uuid
import os
import psycopg2
from contextlib import contextmanager

from .auth import get_current_user
from .services.model_adapter import get_model_adapter

app = FastAPI(title="AI Prime API")

@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
        yield conn
    except psycopg2.OperationalError as e:
        raise HTTPException(status_code=500, detail="Could not connect to database")
    finally:
        if conn is not None:
            conn.close()

class Query(BaseModel):
    user_id: str
    prompt: str
    context_ids: list = []
    adapter: str = "openai"

@app.post("/v1/query")
async def query(q: Query, current_user: dict = Depends(get_current_user)):
    request_id = uuid.uuid4()
    try:
        model_adapter = get_model_adapter(q.adapter)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    answer, provenance = model_adapter.query(q.prompt, q.context_ids)

    # Persist provenance data
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            for p in provenance:
                cur.execute(
                    """
                    INSERT INTO provenance (id, request_id, source_id, type, cursor, confidence, snippet_hash)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (p['id'], request_id, p.get('source_id', ''), p.get('type'), p.get('cursor'), p.get('confidence'), p.get('snippet_hash'))
                )
        conn.commit()

    return {"answer": answer, "provenance": provenance, "request_id": request_id}

@app.post("/v1/feedback")
async def feedback(payload: dict, current_user: dict = Depends(get_current_user)):
    # collect feedback for continuous training
    return {"status":"received"}
