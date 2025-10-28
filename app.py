from flask import Flask, render_template, jsonify, request
from database import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    qualifications = conn.execute('SELECT * FROM qualifications').fetchall()
    conn.close()

    return render_template('index.html', qualifications=qualifications)

@app.route('/api/qualification/<int:qual_id>')
def get_qualification(qual_id):
    """資格の詳細情報を取得するAPI"""
    conn = get_connection()
    
    # 資格基本情報
    qual = conn.execute('SELECT * FROM qualifications WHERE id = ?', (qual_id,)).fetchone()
    
    # 勉強時間
    study_hours = conn.execute(
        'SELECT * FROM study_hours WHERE qualification_id = ?', 
        (qual_id,)
    ).fetchall()
    
    # 科目
    subjects = conn.execute(
        'SELECT * FROM subjects WHERE qualification_id = ?', 
        (qual_id,)
    ).fetchall()
    
    # 教材
    materials = conn.execute(
        'SELECT * FROM materials WHERE qualification_id = ?', 
        (qual_id,)
    ).fetchall()
    
    conn.close()
    
    return jsonify({
        'qualification': dict(qual),
        'study_hours': [dict(row) for row in study_hours],
        'subjects': [dict(row) for row in subjects],
        'materials': [dict(row) for row in materials]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)