
from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laddu Gopal Idol", "price": 499, "emoji": "🙏"},
    {"id": 2, "name": "Krishna Peacock Flute", "price": 299, "emoji": "🪈"},
    {"id": 3, "name": "Radha Krishna Showpiece", "price": 799, "emoji": "🦚"},
    {"id": 4, "name": "Tulsi Mala", "price": 199, "emoji": "📿"},
    {"id": 5, "name": "Krishna Wall Art", "price": 599, "emoji": "🖼️"},
    {"id": 6, "name": "Brass Pooja Diya", "price": 249, "emoji": "🪔"},
]

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Radhe Shyam | Divine Store</title>
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #fffaf0;
    color: #26364b;
}
header {
    background: #182b49;
    color: white;
    padding: 20px 7%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
}
.logo { color: #f4cf7b; font-size: 25px; font-weight: bold; }
nav a { color: white; text-decoration: none; margin-left: 18px; }
.hero {
    text-align: center;
    padding: 65px 20px;
    background: linear-gradient(135deg, #182b49, #674080);
    color: white;
}
.hero h1 { color: #f4cf7b; font-size: clamp(32px, 5vw, 48px); }
.hero p { font-size: 18px; line-height: 1.6; }
.hero a {
    display: inline-block;
    margin-top: 12px;
    padding: 13px 24px;
    background: #f4cf7b;
    color: #182b49;
    text-decoration: none;
    border-radius: 25px;
    font-weight: bold;
}
section { padding: 35px 7%; }
h2 { text-align: center; }
.products {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 22px;
}
.card {
    background: white;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 15px #182b4912;
}
.product-icon {
    background: #f8edda;
    border-radius: 12px;
    padding: 22px;
    font-size: 65px;
}
.price { font-size: 21px; font-weight: bold; color: #8b572a; }
button {
    border: 0;
    border-radius: 22px;
    padding: 11px 18px;
    background: #182b49;
    color: white;
    cursor: pointer;
}
button:hover { background: #674080; }
#cart {
    background: white;
    border-radius: 12px;
    padding: 20px;
    margin-top: 25px;
}
footer {
    text-align: center;
    padding: 25px;
    background: #182b49;
    color: white;
}
</style>
</head>
<body>
<header>
    <div class="logo">🦚 Radhe Shyam</div>
    <nav>
        <a href="#home">Home</a>
        <a href="#shop">Shop</a>
        <a href="#cart">Cart (<span id="count">0</span>)</a>
    </nav>
</header>

<div class="hero" id="home">
    <h1>Bring Home Divine Love</h1>
    <p>Discover beautiful treasures inspired by Shri Krishna and Radha Rani.</p>
    <a href="#shop">Explore Collection</a>
</div>

<section id="shop">
    <h2>✨ Our Divine Collection ✨</h2>
    <div class="products">
    {% for p in products %}
        <div class="card">
            <div class="product-icon">{{ p.emoji }}</div>
            <h3>{{ p.name }}</h3>
            <p class="price">₹{{ p.price }}</p>
            <button onclick="addToCart({{ p.id }}, '{{ p.name }}', {{ p.price }})">
                Add to Cart
            </button>
        </div>
    {% endfor %}
    </div>

    <div id="cart">
        <h2>🛍️ Your Shopping Cart</h2>
        <div id="items">Your cart is empty.</div>
        <h3 id="total">Total: ₹0</h3>
        <button onclick="checkout()">Place Demo Order</button>
        <p id="message"></p>
    </div>
</section>

<footer>
    <p>हरे कृष्ण हरे कृष्ण, कृष्ण कृष्ण हरे हरे 💙</p>
    <p>Radhe Shyam Divine Store · Demo Shopping Website</p>
</footer>

<script>
let cart = [];

function addToCart(id, name, price) {
    const item = cart.find(p => p.id === id);
    if (item) item.quantity++;
    else cart.push({id, name, price, quantity: 1});
    updateCart();
}

function updateCart() {
    document.getElementById("count").textContent =
        cart.reduce((sum, p) => sum + p.quantity, 0);

    document.getElementById("items").innerHTML = cart.length
        ? cart.map(p => `
            <p>${p.name} × ${p.quantity} — ₹${p.price * p.quantity}
            <button onclick="removeItem(${p.id})">Remove</button></p>
          `).join("")
        : "Your cart is empty.";

    document.getElementById("total").textContent =
        "Total: ₹" + cart.reduce((sum, p) => sum + p.price * p.quantity, 0);
}

function removeItem(id) {
    cart = cart.filter(p => p.id !== id);
    updateCart();
}

function checkout() {
    document.getElementById("message").textContent = cart.length
        ? "Demo only! No real order or payment has been placed."
        : "Please add a product to your cart first.";
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE, products=products)

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
