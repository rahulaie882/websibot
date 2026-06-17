import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Premium Packages Data
PACKAGES = {
    "CHILD": {
        "name": "CHILD P@RN",
        "price": "₹59",
        "videos": "4000 𝑽𝑰𝑫𝑬𝑶𝑺",
        "img": "https://files.catbox.moe/1b9zja.mp4",
        "caption": "💥 100k+ VIDEOS AVAILABLE\n✅ 100% TRUSTED SELLING"
    },
    "mms": {
        "name": "MMS ONLY",
        "price": "₹49",
        "videos": "3000 𝑽𝑰𝑫𝑬𝑶𝑺",
        "img": "https://files.catbox.moe/ht1t5c.mp4",
        "caption": "💥 EXCLUSIVE MMS COLLECTION\n✅ HIGH QUALITY VIDEOS"
    },
    "viral": {
        "name": "MMS + INSTA VIRAL",
        "price": "₹99",
        "videos": "8000 𝑽𝑰𝑫𝑬𝑶𝑺",
        "img": "https://files.catbox.moe/agntne.mp4",
        "caption": "💥 VIRAL + MMS COMBO\n✅ LATEST TRENDING CONTENT"
    }
}

QR_LINK = "https://pic-link-bot.lovable.app/i/telegram-1779456784703-bb360fdb.jpg"

HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premium Store</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0f0f0f; color: white; margin: 0; padding: 0; }
        .marquee { background: #d9534f; padding: 12px 0; font-weight: bold; font-size: 18px; overflow: hidden; position: sticky; top: 0; z-index: 1000; }
        .marquee-content { display: inline-block; white-space: nowrap; animation: marquee 15s linear infinite; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }
        
        #notify { position: fixed; bottom: 20px; left: 20px; background: #fff; color: #333; padding: 10px 20px; border-radius: 30px; display: none; z-index: 9999; border-left: 5px solid #28a745; font-size: 14px; }
        .container { padding: 20px; text-align: center; }
        .card { background: #1a1a1a; margin: 25px auto; padding: 20px; border-radius: 20px; max-width: 450px; border: 1px solid #333; box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
        video { width: 100%; height: 250px; border-radius: 15px; border: 1px solid #444; }
        h3 { color: #d9534f; font-size: 24px; margin: 15px 0 5px; }
        .price { font-size: 20px; font-weight: bold; color: #28a745; margin-bottom: 10px; }
        .caption { font-size: 15px; color: #bbb; white-space: pre-line; margin-bottom: 15px; }
        .btn-buy { background: #28a745; color: white; border: none; padding: 15px; width: 100%; border-radius: 10px; font-size: 18px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="marquee"><div class="marquee-content">🔥 WELCOME TO PREMIUM STORE - FAST DELIVERY - 100% TRUSTED - HIGH QUALITY 🔥</div></div>
    <div id="notify"></div>
    <div class="container">
        {% for pkg, data in packages.items() %}
            <div class="card">
                <video src="{{ data.img }}" controls></video>
                <h3>{{ data.name }}</h3>
                <p class="price">{{ data.price }} | {{ data.videos }}</p>
                <div class="caption">{{ data.caption }}</div>
                <form action="/pay" method="post">
                    <input type="hidden" name="package" value="{{ pkg }}">
                    <button class="btn-buy" type="submit">UNLOCK PREMIUM</button>
                </form>
            </div>
        {% endfor %}
    </div>
    <script>
        const names = ["Rahul", "Aryan", "Vikram", "Sneha", "Priya", "Amit"];
        const cats = ["CHILD P@RN", "MMS ONLY", "MMS+VIRAL"];
        function showNotify() {
            const box = document.getElementById('notify');
            box.innerHTML = `✅ <b>${names[Math.floor(Math.random()*names.length)]}</b> just bought <b>${cats[Math.floor(Math.random()*cats.length)]}</b> 1m ago`;
            box.style.display = 'block';
            setTimeout(() => { box.style.display = 'none'; }, 4000);
        }
        setInterval(showNotify, 7000);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE, packages=PACKAGES)

@app.route('/pay', methods=['POST'])
def pay():
    pkg = request.form.get('package')
    data = PACKAGES[pkg]
    return f"""
    <body style="text-align:center; font-family:sans-serif; background:#0f0f0f; color:white; padding:20px; display:flex; flex-direction:column; justify-content:center; align-items:center; min-height:100vh; margin:0;">
        <h1 style="color
    
