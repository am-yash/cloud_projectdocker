from flask import Flask, render_template_string

app = Flask(_name_)

# Define your HTML template
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>UFL Inspired Website</title>
  <style>
    /* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  background: #1a1a1a;
  color: #fff;
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: #000;
  position: fixed;
  width: 100%;
  z-index: 1000;
}

.header .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav ul {
  list-style: none;
  display: flex;
}

.nav ul li {
  margin-left: 1.5rem;
}

.nav ul li a {
  text-decoration: none;
  color: #fff;
  font-size: 1rem;
}

.preorder-btn {
  background: #ff4757;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.preorder-btn:hover {
  background: #ff6b81;
}

/* Hero Section */
.hero {
  position: relative;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: #fff;
  background: linear-gradient(90deg, #ff6b81, #1a1a1a), url('https://wallpapercave.com/wp/wp14429411.jpg') no-repeat center/cover;
}

.hero-content h1 {
  font-size: 4rem;
}

.hero-content h2 {
  font-size: 2.5rem;
  margin-top: 1rem;
}

.hero-content p {
  margin: 1rem 0;
}

.arrow-down {
  margin-top: 2rem;
  font-size: 2rem;
}

/* Features Section */
.features {
  padding: 2rem;
  background: #2c2c2c;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

.feature-item {
  background: #333;
  padding: 1rem;
  border-radius: 10px;
  text-align: center;
}

.feature-item img {
  max-width: 100%;
  border-radius: 10px;
  margin-bottom: 1rem;
}

/* Video Section */
.video-section {
  padding: 2rem;
  text-align: center;
  background: #1a1a1a;
}

.video-container {
  max-width: 800px;
  margin: 0 auto;
}

iframe {
  width: 100%;
  border-radius: 10px;
}

/* Footer */
.footer {
  background: #000;
  text-align: center;
  padding: 1rem;
}

.footer a {
  color: #fff;
  text-decoration: none;
  margin: 0 1rem;
}

  </style>
</head>
<body>
  <!-- Header -->
  <header class="header">
    <div class="container">
      <div class="logo">UFL</div>
      <nav class="nav">
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#news">News</a></li>
          <li><a href="#trailer">Trailer</a></li>
          <li><a href="#support">Support</a></li>
        </ul>
      </nav>
      <button class="preorder-btn">Pre-Order Now</button>
    </div>
  </header>

  <!-- Hero Section -->
  <section id="home" class="hero">
    <div class="hero-content">
      <h1>PRE-ORDER</h1>
      <h2>UFL Bundles</h2>
      <p>Start playing November 28 with the UFL pre-order Bundle!</p>
      <p>UFL will be released for everyone to play on December 5, 2024</p>
      <div class="arrow-down">&#x2193;</div>
    </div>
  </section>

  <!-- Features Section -->
  <section id="news" class="features">
    <div class="container">
      <h2>Latest News</h2>
      <div class="features-grid">
        <div class="feature-item">
          <img src="https://images8.alphacoders.com/138/thumbbig-1384257.webp" alt="Feature Image 1">
          <h3>Game Updates</h3>
          <p>Stay updated with the latest news and announcements.</p>
        </div>
        <div class="feature-item">
          <img src="https://images2.alphacoders.com/138/thumbbig-1384256.webp" alt="Feature Image 2">
          <h3>Exclusive Bundles</h3>
          <p>Explore exclusive pre-order bundles and rewards.</p>
        </div>
        <div class="feature-item">
          <img src="https://images2.alphacoders.com/138/thumbbig-1384258.webp" alt="Feature Image 3">
          <h3>Community Events</h3>
          <p>Join events and engage with the UFL community.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Video Section -->
  <section id="trailer" class="video-section">
    <h2>Watch the Official Trailer</h2>
    <div class="video-container">
      <iframe
        width="100%"
        height="500"
        src="https://www.youtube.com/embed/-k2Vz0KEmnQ?si=26O_mplrrVxjfqlR"
        title="UFL Trailer"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-links">
      <a href="#policies">Game Policies</a>
      <a href="#web-policies">Web Policies</a>
    </div>
  </footer>

  <script>
    document.querySelector('.preorder-btn').addEventListener('click', () => {
      alert('Pre-order feature coming soon!');
    });
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if _name_ == '_main_':
    app.run(debug=True)
