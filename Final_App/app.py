from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

DATABASE = 'pgatourstats.db'

def get_connection():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except:
        print("Error connecting to sqlite")
    return conn

def player_count_by_years():
    cn = get_connection()
    xs = []
    ys = []
    if cn:
        cur = cn.cursor()
        cur.execute('''
        SELECT 
            strftime("year") AS "year",
            COUNT("year") AS "Total"
        FROM 
            cleaned 
        GROUP BY 
            strftime("year");
        ''')
        rows = cur.fetchall()
        for row in rows:
            print(row)
            xs.append(row[0])
            ys.append(row[1])        
        cn.close() 
    
    return xs, ys

def scoring_avg_by_year():
    cn = get_connection()
    sc = []
    yr = []
    if cn:
        cur = cn.cursor()
        cur.execute('''
        SELECT 
            "year",
             ROUND(AVG("avg_score") ,2) AS "avg"
        FROM 
            cleaned 
        GROUP BY 
            "year";
        ''')
        rows = cur.fetchall()
        for row in rows:
            print(row)
            sc.append(row[0])
            yr.append(row[1])        
        cn.close() 
    
    return sc, yr


@app.route("/")
def index():
    xs, ys = player_count_by_years()
    sc, yr = scoring_avg_by_year()
    return render_template('index.html', data={'xs': xs, 'ys': ys, 'sc':sc, 'yr':yr})

if __name__ == "__main__":
    app.run(debug=True)