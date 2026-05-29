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

