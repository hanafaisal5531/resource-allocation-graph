# 🧠 Resource Allocation Graph (RAG) & Deadlock Simulator

An interactive **Operating Systems simulator** to visualize **Resource Allocation Graphs (RAG)** and detect **deadlocks** using **DFS-based cycle detection**.
The system follows correct OS semantics by strictly enforcing **Process–Resource relationships** and provides real-time feedback through a graphical interface.

---

## 📌 Project Overview

Deadlock is a critical issue in operating systems where a set of processes are permanently blocked, each waiting for resources held by others.
This project simulates such scenarios using a **Resource Allocation Graph**, allowing users to:

* Add processes and resources
* Create request and allocation edges
* Visualize system state dynamically
* Detect deadlocks automatically

The frontend handles visualization and interaction, while the backend acts as the **authoritative system state manager** and performs deadlock detection.

---

## ✨ Features

* Interactive SVG-based graph visualization
* Processes (P) and Resources (R) as distinct node types
* Request edges (P → R)
* Allocation edges (R → P)
* DFS-based deadlock detection
* Backend-driven state management (FastAPI)
* Input validation for correct OS semantics
* Real-time status updates

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* Tailwind CSS
* Vanilla JavaScript
* SVG for graph rendering

### Backend

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic

---

## 📂 Project Structure

```
HANA'S PROJECT/
│
├── index.html        # Frontend UI
├── server.py         # FastAPI backend
├── graph.py          # RAG logic + deadlock detection
├── models.py         # API schemas
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## 🧪 Virtual Environment Setup (`.venv`) — Recommended

Using a virtual environment isolates project dependencies and avoids version conflicts.

### Prerequisites

* Python 3.10 or above
* pip installed

Check Python version:

```bash
python --version
```

---

### 1️⃣ Create Virtual Environment

From the project root directory:

```bash
python -m venv .venv
```

---

### 2️⃣ Activate Virtual Environment

#### Windows (PowerShell / CMD)

```bash
.venv\Scripts\activate
```

You should see:

```
(.venv)
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Deactivate (Optional)

```bash
deactivate
```

---

## ▶️ How to Run the Project

### 1️⃣ Start the Backend Server

Make sure `.venv` is activated, then run:

```bash
uvicorn server:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

You should see:

```json
{"message": "RAG Deadlock Simulator Backend Running"}
```

---

### 2️⃣ Open the Frontend (Important)

⚠️ **Do NOT open `index.html` by double-clicking**
This causes CORS and fetch errors.

#### Option A (Recommended – VS Code)

1. Install **Live Server** extension
2. Right-click `index.html`
3. Select **Open with Live Server**

Frontend opens at:

```
http://127.0.0.1:5500/index.html
```

---

#### Option B (Python HTTP Server)

```bash
python -m http.server 5500
```

Then open:

```
http://127.0.0.1:5500/index.html
```

---

## 🔗 Backend API Endpoints

* **Health Check**
  `GET /`
  `http://127.0.0.1:8000/`

* **Current System State**
  `GET /state`

* **Deadlock Detection**
  `GET /deadlock`

* **API Documentation (Swagger UI)**
  `http://127.0.0.1:8000/docs`

---

## 🧪 Example Deadlock Scenario

### Step-by-Step

1. Add processes:

   * `P1`, `P2`

2. Add resources:

   * `R1`, `R2`

3. Create edges:

   * Request: `P1 → R1`
   * Allocation: `R1 → P2`
   * Request: `P2 → R2`
   * Allocation: `R2 → P1`

### Resulting Cycle

```
P1 → R1 → P2 → R2 → P1
```

✔ The system detects a **deadlock**
✔ A red warning is displayed
✔ All involved nodes are highlighted

---

## ⚠️ Input Validation Rules

To maintain correct OS semantics:

| Operation  | Allowed Direction  |
| ---------- | ------------------ |
| Request    | Process → Resource |
| Allocation | Resource → Process |

Invalid actions (e.g., Process → Process) are automatically blocked.

---

## 🧠 Deadlock Detection Algorithm

* Graph is represented as an adjacency list
* DFS traversal is performed
* A recursion stack is maintained
* Presence of a cycle ⇒ **Deadlock**





