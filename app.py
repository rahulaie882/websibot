import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Updated Data with Full Captions
PACKAGES = {
    "CHILD": {
        "name": "CHILD P@RN",
        "price": "₹59",
        "videos": "4000 𝑽𝑰𝑫𝑬𝑶𝑺",
        "img": "https://files.catbox.moe/1b9zja.mp4",
        "caption": "💥 100k+ VIDEOS AVAILABLE\n✅ 100% TRUSTED SELLING\n👇 GET ACCESS NOW"
    },
    "mms": {
        "name": "MMS ONLY",
        "price": "₹49",
        "videos": "3000 𝑽𝑰𝑫𝑬𝑶𝑺",
        "img": "https://files.catbox.moe/ht1t5c.mp4",
        "caption": "💥 EXCLUSIVE MMS COLLECTION\n✅ HIGH QUALITY VIDEOS\n👇 GET ACCESS NOW"
    },
    "viral": {
        "name": "MMS + INSTA VIRAL",
        "price": "₹99",
        "videos": "8000 𝑽𝑰𝑫𝑬𝑶𝑺",
        "img": "https://files.catbox.moe/agntne.mp4",
        "caption": "💥 VIRAL + MMS COMBO\n✅ LATEST TRENDING CONTENT\n👇 GET ACCESS NOW"
    }
}

QR_LINK = "https://pic-link-bot.lovable.app/i/telegram-1779456784703-bb360fdb.jpg"

HTML_CODE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; text-align: center; background: #f4f4f4; padding: 20px; }
        .card { background: white; margin: 30px auto; padding: 25px; border-radius: 20px; max-width: 500px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        video { width: 100%; height: 250px; border-radius: 15px; margin-bottom: 20px; background: #000; }
        h3 { font-size: 28px; margin: 5px 0; }
        .price { font-size: 22px; color: #d9534f; font-weight: bold; }
        .caption { white-space: pre-line; font-size: 16px; color: #444; margin: 15px 0; }
        button { background: #28a745; color: white; padding: 18px; border: none; border-radius: 10px; font-size: 20px; width: 100%; cursor: pointer; }
    </style>
</head>
<body>
    <h1>🔥 PREMIUM CONTENT STORE 🔥</h1>
    {% for pkg, data in packages.items() %}
        <div class="card">
            <video src="{{ data.img }}" controls></video>
            <h3>{{ data.name }}</h3>
            <p class="price">{{ data.price }} | {{ data.videos }}</p>
            <div class="caption">{{ data.caption }}</div>
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
    <body style="text-align:center; font-family:sans-serif; padding: 30px;">
        <h1 style="color: #d9534f;">COMPLETE PAYMENT</h1>
        <h2 style="font-size: 24px;">{data['name']}</h2>
        <p style="font-size: 20px;">Pay: <b>{data['price']}</b></p>
        <img src="{QR_LINK}" style="width: 350px; height: 350px; border: 5px solid #333; border-radius: 15px;">
        <p style="font-size: 18px; margin-top: 20px;">UPI ID: <b>Q691189350@ybl</b></p>
        <p style="color: red; font-weight: bold;">Screenshot bhejne ke baad admin se contact karein.</p>
        <br><a href="/" style="font-size: 20px;">🔙 Back to Home</a>
    </body>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
