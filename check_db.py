from database import get_connection

def check_data():
    conn = get_connection()

    print("===資格情報===")
    qualifications = conn.execute('SELECT * FROM qualifications').fetchall()
    print(qualifications)
    for row in qualifications:
        print(dict(row))

    print("\n===勉強時間===")
    study_hours = conn.execute('SELECT * FROM study_hours').fetchall()
    for row in study_hours:
        print(dict(row))

    print("\n===科目===")
    subjects = conn.execute('SELECT * FROM subjects').fetchall()
    for row in subjects:
        print(dict(row))

    print("\n===教材===")
    materials = conn.execute('SELECT * FROM materials').fetchall()
    for row in materials:
        print(dict(row))

    conn.close()

if __name__ == "__main__":
    check_data()
