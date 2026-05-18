from flask import Flask, render_template, request, session, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "mysecretkey123"


# -----------------------
# Database Setup
# -----------------------
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT,
    course TEXT,
    message TEXT
)
''')

conn.commit()
conn.close()


# -----------------------
# Home Page
# -----------------------
@app.route('/')
def home():
    return render_template('index.html')


# -----------------------
# Register Form Submit
# -----------------------
@app.route('/register', methods=['POST'])
def register():

    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    course = request.form.get('course')
    message = request.form.get('message')

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (name, phone, email, course, message)
        VALUES (?, ?, ?, ?, ?)
    """, (name, phone, email, course, message))

    conn.commit()
    conn.close()

    flash("Admission Submitted Successfully!")
    return redirect('/')


# -----------------------
# Admin Login
# -----------------------
@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        # Change username/password here
        if username == "admin" and password == "pe74":

            session['admin_logged_in'] = True

            return redirect('/admin')

        else:
            return "Wrong Username or Password"

    return render_template('admin_login.html')


# -----------------------
# Admin Panel Protected
# -----------------------
@app.route('/admin')
def admin():

    # Login check
    if 'admin_logged_in' not in session:
        return redirect('/admin-login')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    conn.close()

    return render_template('admin.html', students=students)


# -----------------------
# Logout
# -----------------------
@app.route('/logout')
def logout():

    session.pop('admin_logged_in', None)

    return redirect('/admin-login')


# -----------------------
# Delete Student
# -----------------------
@app.route('/delete/<int:id>')
def delete_student(id):

    # Login check
    if 'admin_logged_in' not in session:
        return redirect('/admin-login')

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect('/admin')


# -----------------------
# Run App
# -----------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)