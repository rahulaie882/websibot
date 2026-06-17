import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Basic layout for browser
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Premium Access</title>
    <style>body { text-align: center; font-family: sans-serif; }</style>
</head>
<body>
    <h1>Premium Content Store</h1>
    <p>Select a category to pay:</p>
    <button onclick="alert('Proceed to QR Payment')">Pay ₹69</button>
    <br><br>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload Payment Proof</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/upload', methods=['POST'])
def upload():
    return "Proof received! Admin will check."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
  
