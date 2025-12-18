from pydantic import BaseModel

class NodeCreate(BaseModel):
    id: str

class EdgeCreate(BaseModel):
    source: str
    target: str
    type: str  # "request" or "allocation"
