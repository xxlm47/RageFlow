import json, sqlite3
from datetime import datetime, timezone
from .config import Config
class DB:
    def __init__(self,path=None):
        self.cx=sqlite3.connect(path or Config.db)
        self.cx.execute("CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY,topic TEXT,created_at TEXT,result_json TEXT)")
        self.cx.execute("CREATE TABLE IF NOT EXISTS performance(id INTEGER PRIMARY KEY,post_id TEXT,metric TEXT,value REAL,created_at TEXT)")
        self.cx.commit()
    def save_run(self,topic,result):
        self.cx.execute("INSERT INTO runs(topic,created_at,result_json) VALUES(?,?,?)",(topic,datetime.now(timezone.utc).isoformat(),json.dumps(result)))
        self.cx.commit()
