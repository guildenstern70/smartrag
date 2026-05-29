# SmartRAG

## Setup

### Prerequisites
- Python 3.14 or higher
- pip (Python package manager)

### Installation Steps

1. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   ```

2. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   python3 -m pip install --upgrade pip setuptools wheel
   python3 -m pip install -e .
   ```

   Or, if you prefer to install dependencies without the editable mode:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

### Verify Installation

To verify that all dependencies are installed correctly, run:
```bash
python3 -m pip list
```

### Deactivate Virtual Environment

When you're done working, deactivate the virtual environment:
```bash
deactivate
```

### Re-activate Later

To reactivate the virtual environment in a new terminal session:
```bash
source .venv/bin/activate
```

## Dependency Management with `uv`

This project uses [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver. Below are instructions on how to load, change, and verify dependencies using the `uv` tool:

### 1. Load & Sync Dependencies
To create a virtual environment (`.venv`) and install all dependencies defined in `pyproject.toml` and resolved in `uv.lock`, run:
```bash
uv sync
```

### 2. Change Dependencies
* **Add a new package:**
  ```bash
  uv add <package-name>
  ```
* **Remove a package:**
  ```bash
  uv remove <package-name>
  ```
* **Manual edits**: You can also modify the `dependencies` array inside [pyproject.toml](file:///Users/alessio/Documents/Codice/Python/SmartRag/pyproject.toml) directly, and then run `uv sync` to sync the environment and update `uv.lock`.

### 3. Verify Dependencies
* **List installed packages**:
  ```bash
  uv pip list
  ```
* **View dependency tree**:
  ```bash
  uv tree
  ```
* **Run application directly**: To run the script safely inside the virtual environment with verified dependencies, run:
  ```bash
  uv run python src/smart_rag.py
  ```

## Reference

This code has been created after the article at:
https://www.freecodecamp.org/news/rag-explained-simply-with-a-real-project/

