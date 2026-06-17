import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Packages Data with your specific links
PACKAGES = {
    "CHILD": {
        "name": "CHILD P@RN", 
        "price": "₹59", 
        "img": "https://telegra.ph/file/ed1b4760086c5f7808298.jpg" # Example Thumbnail
    },
    "mms": {
        "name": "MMS ONLY", 
        "price": "₹49", 
        "img": "https://files.catbox.moe/ht1t5c.mp4" 
    },
    "viral": {
        "name": "MMS + INSTA VIRAL", 
        "price": "₹99", 
        "img": "https://files.catbox.moe/agntne.mp4"
    }
}

QR_LINK = "https://pic-link-bot.lovable.app/i/telegram-1779456784703-bb360fdb.jpg"

HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .card { border: 2px solid #333; margin: 20px; padding: 15px; border-radius: 10px; }
        video, img { width: 150px; height: 150px; border-radius: 10px; }
        button { background: #28a745; color: white; padding: 12px 25px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
    </style>
</head>
<body style="text-align:center; font-family:sans-serif;">
    <h1>Premium Content Store</h1>
    {% for pkg, data in packages.items() %}
        <div class="card">
            {% if data.img.endswith('.mp4') %}
                <video src="{{ data.img }}" controls></video>
            {% else %}
                <img src="{{ data.img }}" alt="img">
            {% endif %}
            <h3>{{ data.name }}</h3>
            <p>Price: <b>{{ data.price }}</b></p>
            <form action="/pay" method="post">
                <input type="hidden" name="package" value="{{ pkg }}">
                <button type="submit">UNLOCK PREMIUM</button>
            </form>
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE, packages=PACKAGES)

@app.route('/pay', methods=['POST'])
def pay():
    pkg_key = request.form.get('package')
    data = PACKAGES[pkg_key]
    return f"""
    <body style="text-align:center; font-family:sans-serif; padding: 20px;">
        <h1>Payment Required</h1>
        <h3>Pay {data['price']} for {data['name']}</h3>
        <img src="{QR_LINK}" style="width:250px; border: 2px solid black;">
        <p>UPI: <b>Q691189350@ybl</b></p>
        <p style="color: red;">Screenshot bhejne ke baad admin se contact karein.</p>
        <br><a href="/">🔙 Back to Home</a>
    </body>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
