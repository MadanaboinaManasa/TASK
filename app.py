from flask import Flask, render_template, request
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
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Fetch form data
        details = request.form
        name = details['name']
        email = details['email']
        age = details['age']
        dob = details['dob']

        # Store data in MySQL
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, age, dob) VALUES(%s, %s, %s, %s)", (name, email, age, dob))
        mysql.connection.commit()
        cur.close()

        return 'Form submitted successfully!'
    

if __name__ == '__main__':
    app.run(debug=True)
