import os
import socket
from datetime import datetime
from flask import Flask, render_template_string

app = Flask(__name__)

# Track views in memory for this demo
PAGE_VIEWS = 0

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>My Docker App</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f9; color: #333; text-align: center; padding: 50px; }
        .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); display: inline-block; }
        h1 { color: #007acc; }
        .stat { font-size: 1.2em; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 My Docker Program is Live!</h1>
        <p class="stat"><strong>Container Hostname:</strong> {{ hostname }}</p>
        <p class="stat"><strong>Server Time:</strong> {{ current_time }}</p>
        <p class="stat"><strong>Page Views this session:</strong> {{ views }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    global PAGE_VIEWS
    PAGE_VIEWS += 1
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML_TEMPLATE, hostname=hostname, current_time=current_time, views=PAGE_VIEWS)

if __name__ == '__main__':
    # Run on port 5000 inside the container
    app.run(host='0.0.0.0', port=5000)
