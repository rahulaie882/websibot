import os
import sqlite3
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
DB_FILE = "bot_database.db"

# Database Initialize
def init_db():
    with sqlite3.connect(DB_FILE) as db:
        db.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, package TEXT, status TEXT)")
        db.commit()

init_db()

# HTML Template
HTML_CODE = """
<!DOCTYPE html>
<html>
<body style="font-family:sans-serif; text-align:center;">
    <h1>Premium Content Store</h1>
    {% for pkg, details in packages.items() %}
        <div style="border:1px solid #ccc; padding:10px; margin:10px;">
            <h3>{{ details.name }} - {{ details.price }}</h3>
            <form action="/buy" method="post">
                <input type="hidden" name="package" value="{{ pkg }}">
                <button type="submit">Buy Now</button>
            </form>
        </div>
    {% endfor %}
    <hr>
    <h2>Admin Area (Check Orders)</h2>
    <a href="/admin">Click here to check payments</a>
</body>
</html>
"""

PACKAGES = {
    "CHILD": {"name": "CHILD P@RN", "price": "₹59"},
    "mms": {"name": "MMS ONLY", "price": "₹49"},
    "viral": {"name": "MMS + INSTA VIRAL", "price": "₹99"}
}

@app.route('/')
def home():
    return render_template_string(HTML_CODE, packages=PACKAGES)

@app.route('/buy', methods=['POST'])
def buy():
    pkg = request.form.get('package')
    with sqlite3.connect(DB_FILE) as db:
        db.execute("INSERT INTO orders (package, status) VALUES (?, ?)", (pkg, 'pending'))
        db.commit()
    return "<h3>Order Placed! Send payment to UPI: Q691189350@ybl. After payment, ask admin to check.</h3>"

@app.route('/admin')
def admin():
    with sqlite3.connect(DB_FILE) as db:
        orders = db.execute("SELECT * FROM orders").fetchall()
    return render_template_string("<h1>Orders</h1>{% for o in orders %}<p>{{ o }}</p>{% endfor %}", orders=orders)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
