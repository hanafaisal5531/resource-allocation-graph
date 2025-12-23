from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from graph import ResourceAllocationGraph
from models import NodeCreate, EdgeCreate

app = FastAPI(
    title="Resource Allocation Graph Deadlock Simulator Backend",
    version="1.0"
)

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

rag = ResourceAllocationGraph()

# ---------- ROOT ----------

@app.get("/")
def root():
    return {
        "message": "RAG Deadlock Simulator Backend Running"
    }

# ---------- STATE ----------

@app.get("/state")
def get_state():
    return rag.snapshot()

# ---------- NODES ----------

@app.post("/process")
def add_process(data: NodeCreate):
    rag.add_process(data.id)
    return rag.snapshot()

@app.post("/resource")
def add_resource(data: NodeCreate):
    rag.add_resource(data.id)
    return rag.snapshot()

@app.delete("/node/{node_id}")
def remove_node(node_id: str):
    rag.remove_node(node_id)
    return rag.snapshot()

# ---------- EDGES ----------

@app.post("/edge")
def add_edge(data: EdgeCreate):
    rag.add_edge(data.source, data.target, data.type)
    return rag.snapshot()

@app.delete("/edge")
def remove_edge(source: str, target: str):
    rag.remove_edge(source, target)
    return rag.snapshot()

# --------- DEADLOCK ---------

@app.get("/deadlock")
def detect_deadlock():
    return {
        "deadlock_detected": len(rag.detect_deadlock()) > 0,
        "nodes": rag.detect_deadlock()
    }

