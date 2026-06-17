import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# Packages Data
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
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f0f0f; color: white; margin: 0; padding: 0; overflow-x: hidden; }
        
        /* Sliding Store Name */
        .marquee { background: #d9534f; color: white; padding: 10px 0; font-weight: bold; font-size: 20px; overflow: hidden; position: sticky; top: 0; z-index: 1000; }
        .marquee-content { display: inline-block; white-space: nowrap; animation: marquee 15s linear infinite; }
        @keyframes marquee { 0% { transform: translateX(100%); } 100% { transform: translateX(-100%); } }

        /* Notification Styling */
        #notification-box { position: fixed; bottom: 20px; left: 20px; background: rgba(255, 255, 255, 0.95); color: #333; padding: 12px 20px; border-radius: 50px; box-shadow: 0 5px 15px rgba(0,0,0,0.3); display: none; z-index: 9999; animation: slideIn 0.5s ease-out; font-size: 14px; border-left: 5px solid #28a745; }
        @keyframes slideIn { from { transform: translateX(-120%); } to { transform: translateX(0); } }

        .container { padding: 20px; text-align: center; }
        .card { background: #1a1a1a; margin: 20px auto; padding: 20px; border-radius: 15px; max-width: 450px; border: 1px solid #333; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        video { width: 100%; border-radius: 10px; border: 1px solid #444; }
        h3 { color: #d9534f; font-size: 26px; margin: 15px 0 5px; }
        .price { font-size: 20px; font-weight: bold; color: #28a745; }
        .caption { font-size: 14px; color: #bbb; white-space: pre-line; margin: 10px 0; }
        .btn-buy { background: #28a745; color: white; border: none; padding: 15px; width: 100%; border-radius: 10px; font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.3s; margin-top: 10px; }
        .btn-buy:hover { background: #218838; }
    </style>
</head>
<body>

    <div class="marquee">
        <div class="marquee-content">🔥 WELCOME TO PREMIUM MMS STORE - 100% TRUSTED - FAST DELIVERY - HIGH QUALITY 🔥</div>
    </div>

    <div id="notification-box"></div>

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
        const names = ["Rahul", "Aryan", "Vikram", "Sneha", "Priya", "Amit", "Sumit", "Karan", "Nitin", "Deepak"];
        const cats = ["CHILD P@RN", "MMS ONLY", "MMS + INSTA VIRAL"];
        
        function showNotification() {
            const box = document.getElementById('notification-box');
            const name = names[Math.floor(Math.random() * names.length)];
            const cat = cats[Math.floor(Math.random() * cats.length)];
            
            box.innerHTML = `✅ <b>${name}</b> just bought <b>${cat}</b> 1m ago`;
            box.style.display = 'block';

            setTimeout(() => {
                box.style.display = 'none';
            }, 4000);
        }

        setInterval(showNotification, 8000); // Har 8 second mein notification
    </script>
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
    <body style="text-align:center; font-family:sans-serif; background:#0f0f0f; color:white; padding: 40px;">
        <h1 style="color: #d9534f;">FINAL STEP: PAYMENT</h1>
        <h2 style="font-size: 24px;">Package: {data['name']}</h2>
        <p style="font-size: 20px; color: #28a745;">Amount: {data['price']}</p>
        <img src="{QR_LINK}" style="width: 320px; border: 5px solid white; border-radius: 15px; margin: 20px 0;">
        <p style="font-size: 18px;">UPI ID: <b>Q691189350@ybl</b></p>
        <p style="color: yellow; font-weight: bold;">Step 2: Send screenshot to Admin after payment.</p>
        <br><a href="/" style="color: #bbb; font-size: 18px; text-decoration: none;">🔙 Cancel & Go Back</a>
    </body>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    
