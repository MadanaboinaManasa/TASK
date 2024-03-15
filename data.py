from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Manasa123@#.'
app.config['MYSQL_DB'] = 'pr'

mysql = MySQL(app)

@app.route('/')
def index():
    # Fetch data from MySQL
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    
    # Render HTML template with users' information
    return render_template('users.html', users=data)

if __name__ == '__main__':
    app.run(debug=True)
