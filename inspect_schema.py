import sqlite3

db_path = 'kbo_database.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

print("=== Tables and Columns ===")
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [r[0] for r in cur.fetchall()]

for table in tables:
    print(f"\nTable: {table}")
    cur.execute(f"PRAGMA table_info('{table}')")
    for col in cur.fetchall():
        print(f"  - {col[1]} ({col[2]})")  # col[1]=name, col[2]=type

print("\n=== Indices (PK/Unique/Other) ===")
cur.execute("SELECT name FROM sqlite_master WHERE type='index';")
indices = [r[0] for r in cur.fetchall()]

for idx in indices:
    print(f"\nIndex: {idx}")
    cur.execute(f"PRAGMA index_info('{idx}')")
    for info in cur.fetchall():
        print(f"  - column: {info[2]}")
    # Check if the index is unique
    cur.execute(f"PRAGMA index_list('{tables[0]}')")
    idx_list = cur.fetchall()
    for i in idx_list:
        if i[1] == idx:
            print(f"  - Unique: {'Yes' if i[2] else 'No'}")

conn.close()
