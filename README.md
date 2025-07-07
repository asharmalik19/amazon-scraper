## How to run this project

### 1. Install UV
here is the link 
https://docs.astral.sh/uv/guides/install-python/

### 2. Clone the repository
```bash
git clone https://github.com/asharmalik19/amazon-scraper
cd amazon-scraper
```

### 3. Install dependencies
```bash
uv sync
```

### 4. Create an input json file named user_queries.json
```json
  [
    "laptop",
    "smartphone",
    "headphones",
    "...."
  ]
```

### 5. Run the scraper
```bash
uv run main.py
```