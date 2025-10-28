from database import get_connection

def insert_ap_data():
    conn = get_connection()
    cursor = conn.cursor()

    # 資格情報を登録
    cursor.execute('''
                   INSERT INTO qualifications VALUES(?,?,?,?,?)''',(None,'応用情報技術者試験','年2回(春期・秋期)',0.23,7500))
    qual_id = cursor.lastrowid

    # 勉強時間を登録
    cursor.execute('''
                   INSERT INTO study_hours VALUES(?,?,?,?,?)''',(None,qual_id,'初学者',200,300))
    
    cursor.execute('''
                   INSERT INTO study_hours VALUES(?,?,?,?,?)''',(None,qual_id,'基本情報合格者',150,200))
    
    # 科目を登録（一部）
    cursor.execute('''
                   INSERT INTO subjects VALUES(?,?,?,?,?)''',(None,qual_id,'情報セキュリティ', True,'必須問題。過去問を繰り返す。')
                   )
    cursor.execute('''
                   INSERT INTO subjects VALUES(?,?,?,?,?)''',(None,qual_id,'経営戦略', False,'事業の中長期的な戦略など。年によって簿記系問題あり。')
                   )
    cursor.execute('''
                   INSERT INTO subjects VALUES(?,?,?,?,?)''',(None,qual_id,'プロジェクトマネジメント', False,'EVMやクリティカルチェーン。文章の抜き出し。')
                   )
    cursor.execute('''
                   INSERT INTO subjects VALUES(?,?,?,?,?)''',(None,qual_id,'サービスマネジメント', False,'サービス運用の知識。文章の抜き出し。')
                   )
    cursor.execute('''
                   INSERT INTO subjects VALUES(?,?,?,?,?)''',(None,qual_id,'システム監査', False,'サービスの処理や運用を読み解く。文章の抜き出し。問題までの文章量多め。')


                   )
    # 教材を登録
    cursor.execute('''
                   INSERT INTO materials VALUES(?,?,?,?,?,?)''',
                   (None, qual_id,'website','応用情報技術者試験過去問道場','https://www.ap-siken.com/',0))
    
    cursor.execute('''
                   INSERT INTO materials VALUES(?,?,?,?,?,?)''',
                   (None, qual_id,'book','応用情報技術者 合格教本',None,3300))
    
    conn.commit()
    conn.close()
    print('データをいれました')

if __name__ == "__main__":
    insert_ap_data()


