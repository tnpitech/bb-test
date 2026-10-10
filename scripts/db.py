import sqlite3
from pathlib import Path
project_dir = Path(__file__).resolve().parent.parent
DB_FILE = project_dir / "output/data.db"

conn = sqlite3.connect(DB_FILE)
conn.row_factory = sqlite3.Row
