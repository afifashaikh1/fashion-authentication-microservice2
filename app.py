from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------------------
# LOGIN PAGE
# ---------------------------
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(f"Login attempt: {email}")
        return redirect(url_for('register_brand'))
    return render_template('login.html')

# ---------------------------
# SIGNUP PAGE
# ---------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        print(f"Signup: {name}, {email}")
        return redirect(url_for('login'))
    return render_template('signup.html')

# ---------------------------
# REGISTER BRAND PAGE
# ---------------------------
@app.route('/register_brand', methods=['GET', 'POST'])
def register_brand():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form.get('description', '')
        print(f"Brand registered: {name} - {description}")
        return redirect(url_for('verify_brand'))
    return render_template('register_brand.html')

# ---------------------------
# VERIFY BRAND PAGE
# ---------------------------
@app.route('/verify_brand', methods=['GET', 'POST'])
def verify_brand():
    if request.method == 'POST':
        brand_name = request.form.get('brand_name')
        if not brand_name:
            return "Brand name missing in form", 400
        print(f"Verifying brand: {brand_name}")
        return render_template('verify_result.html', brand_name=brand_name, verified=True)
    return render_template('verify_brand.html')


# ---------------------------
# RESULT PAGE
# ---------------------------
@app.route('/verify_result')
def verify_result():
    return render_template('verify_result.html', brand_name="Sample Brand", verified=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
