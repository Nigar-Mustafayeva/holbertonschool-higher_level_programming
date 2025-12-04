"""
task_01_jinja.py

Self-contained Flask app for Task 01: Jinja templating.

This script does two things to make local testing easy:
1. Ensures a `templates/` directory exists and writes the required HTML
   templates (index.html, about.html, contact.html, header.html, footer.html)
   if they are missing.
2. Starts a simple Flask app with routes for '/', '/about', and '/contact'
   that render the templates using Jinja's include for shared header/footer.

Run:
    python task_01_jinja.py

Then open http://127.0.0.1:5000 in your browser.
"""

import os
from flask import Flask, render_template

TEMPLATES = {
    'index.html': """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <main>
        <h1>Welcome to My Flask App</h1>
        <p>This is a simple Flask application.</p>
        <ul>
            <li>Flask</li>
            <li>HTML</li>
            <li>Templates</li>
        </ul>
    </main>

    {% include 'footer.html' %}
</body>
</html>
""",

    'about.html': """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>About - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <main>
        <h1>About Us</h1>
        <p>We build simple web apps to demonstrate Flask and Jinja templating.</p>
        <p>This page describes the purpose of the site and provides background information.</p>
    </main>

    {% include 'footer.html' %}
</body>
</html>
""",

    'contact.html': """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Contact - My Flask App</title>
</head>
<body>
    {% include 'header.html' %}

    <main>
        <h1>Contact Us</h1>
        <p>If you have questions, please reach out at <a href="mailto:info@example.com">info@example.com</a>.</p>
        <p>Alternatively, follow us on social media for updates.</p>
    </main>

    {% include 'footer.html' %}
</body>
</html>
""",

    'header.html': """<header>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a> |
        <a href="/contact">Contact</a>
    </nav>
    <h1>My Flask App</h1>
    <hr>
</header>
""",

    'footer.html': """<footer>
    <hr>
    <p>&copy; 2024 My Flask App</p>
</footer>
""",
}


def ensure_templates_folder(path: str = 'templates') -> None:
    """Create templates directory and files if they don't exist."""
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)

    for filename, content in TEMPLATES.items():
        fpath = os.path.join(path, filename)
        if not os.path.exists(fpath):
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    # Ensure templates are present for quick testing locally
    ensure_templates_folder()
    # Run Flask app on port 5000
    app.run(debug=True, port=5000)
