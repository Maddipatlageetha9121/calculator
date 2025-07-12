from flask import Flask, render_template,request ,redirect,url_for,flash# type: ignore
app=Flask(__name__)

app.secret_key="your_secret_key"

users={}


@app.route('/')
def home():
    return render_template("login.html")

#app route for login page

@app.route('/login' ,methods=['post','get'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Validation logic
        if username in users:
            flash('Username already exists.', 'danger')
        #elif password != confirm_password:
        #    flash('Passwords do not match.', 'danger')
        else:
            # Register the user
            users[username] = {'email': email, 'password': password}
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('dashboard'))

    return render_template('login.html')

 #app route for dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#app route for calculator page
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

if __name__=='__main__':
    app.run(debug=True)