from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

# Function to fetch domain information
def get_domain_info(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    ip = socket.gethostbyname(domain)
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    info = {
        "ip": ip,
        "isp": data.get("org", ""),
        "organization": data.get("org", ""),
        "asn": data.get("asn", ""),
        "location": data.get("country", "")
    }
    return info

# Function to fetch subdomains
def get_subdomains(url):
    subdomains = set()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    anchors = soup.find_all('a')
    for anchor in anchors:
        subdomain = urlparse(anchor.get('href', '')).netloc
        if subdomain:
            subdomains.add(subdomain)
    return list(subdomains)

# Function to fetch asset domains (stylesheets, javascripts, images, iframes, anchors)
def get_asset_domains(url):
    asset_domains = {
        "javascripts": [],
        "stylesheets": [],
        "images": [],
        "iframes": [],
        "anchors": []
    }
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    scripts = soup.find_all('script')
    for script in scripts:
        src = script.get('src', '')
        if src:
            asset_domains['javascripts'].append(urlparse(src).netloc)
    styles = soup.find_all('link')
    for style in styles:
        href = style.get('href', '')
        if href:
            asset_domains['stylesheets'].append(urlparse(href).netloc)
    images = soup.find_all('img')
    for image in images:
        src = image.get('src', '')
        if src:
            asset_domains['images'].append(urlparse(src).netloc)
    iframes = soup.find_all('iframe')
    for iframe in iframes:
        src = iframe.get('src', '')
        if src:
            asset_domains['iframes'].append(urlparse(src).netloc)
    anchors = soup.find_all('a')
    for anchor in anchors:
        href = anchor.get('href', '')
        if href:
            asset_domains['anchors'].append(urlparse(href).netloc)
    return asset_domains

# Flask routes
@app.route('/')
def index():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is missing"}), 400
    domain_info = get_domain_info(url)
    subdomains = get_subdomains(url)
    asset_domains = get_asset_domains(url)
    output = {
        "info": domain_info,
        "subdomains": subdomains,
        "asset_domains": asset_domains
    }
    return jsonify(output)
        
@app.route('/ws')
def main():
    return jsonify({"message": "WebSocket server is running"})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('url_message')
def handle_url_message(data):
    url = data.get('url')
    if url:
        global input_url
        input_url = data['url'].strip()
        print('Received URL:', url)
        emit('message', {'data': f'Session created for {url}'})
    else:
        emit('message', {'error': 'Invalid URL'})

@socketio.on('operation_message')
def handle_operation_message(data):
    global input_url
    operation = data.get('operation')
    # url = request.args.get('url')
    if operation == 'get_info':
        domain_info = get_domain_info(input_url)
        emit('message', {'data': domain_info})
    elif operation == 'get_subdomains':
        subdomains = get_subdomains(input_url)
        emit('message', {'data': subdomains})
    elif operation == 'get_asset_domains':
        asset_domains = get_asset_domains(input_url)
        emit('message', {'data': asset_domains})
    else:
        emit('message', {'error': 'Invalid operation'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
