import sqlite3

DATABASE = 'qualifications.db'
"""
テーブル作成モジュール
"""
def get_connection():
    conn = sqlite3.connect(DATABASE)
    # 辞書形式で取得できるようにする
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    # 資格テーブル
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qualifications(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   frequency TEXT,
                   passing_rate REAL,
                   exam_fee INTEGER
                   )
                   ''')
    
    # 勉強時間テーブル
    cursor.execute('''
                   
                   CREATE TABLE IF NOT EXISTS study_hours(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   qualification_id INTEGER NOT NULL,
                   level TEXT NOT NULL,
                   min_hours INTEGER,
                   max_hours INTEGER,
            FOREIGN KEY (qualification_id) REFERENCES qualifications (id)
        )
    ''')

    # 科目テーブル
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS subjects(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   qualification_id INTEGER NOT NULL,
                   name TEXT NOT NULL,
                   is_required BOOLEAN NOT NULL,
                   recommendation TEXT,
                   FOREIGN KEY(qualification_id) REFERENCES qualifications(id)
                                      )
                   ''')
    
    # 教材テーブル
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS materials(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   qualification_id INTEGER NOT NULL,
                   type TEXT NOT NULL,
                   title TEXT NOT NULL,
                   url TEXT,
                   price INTEGER,
                   FOREIGN KEY(qualification_id) REFERENCES qualifications(id)
                                      )
                   ''')
    
    conn.commit()
    conn.close()
    print("データベースを作成しました")

if __name__== "__main__":
    init_database()
