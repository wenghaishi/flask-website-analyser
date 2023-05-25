from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    url = request.form['input']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Domain Information
    domain = response.url
    server_ip = response.headers.get('X-Real-IP')
    location = response.headers.get('Location')
    asn = response.headers.get('ASN')
    isp = response.headers.get('ISP')
    organization = response.headers.get('Organization')

    # Subdomain Information
    subdomains = set()
    external_domains = {
        'style_sheets': set(),
        'javascripts': set(),
        'images': set(),
        'iframes': set(),
        'anchor_tags': set()
    }

    for tag in soup.find_all(True):
        if tag.has_attr('src'):
            src = tag['src']
            if src.startswith('//'):
                src = 'https:' + src
            elif src.startswith('/'):
                src = url + src
            if src.startswith('http'):
                external_domains['images'].add(src)
        if tag.name == 'link' and tag.has_attr('href') and tag['rel'] == ['stylesheet']:
            href = tag['href']
            if href.startswith('//'):
                href = 'https:' + href
            elif href.startswith('/'):
                href = url + href
            if href.startswith('http'):
                external_domains['style_sheets'].add(href)
        if tag.name == 'script' and tag.has_attr('src'):
            src = tag['src']
            if src.startswith('//'):
                src = 'https:' + src
            elif src.startswith('/'):
                src = url + src
            if src.startswith('http'):
                external_domains['javascripts'].add(src)
        if tag.name == 'iframe' and tag.has_attr('src'):
            src = tag['src']
            if src.startswith('//'):
                src = 'https:' + src
            elif src.startswith('/'):
                src = url + src
            if src.startswith('http'):
                external_domains['iframes'].add(src)
        if tag.name == 'a' and tag.has_attr('href'):
            href = tag['href']
            if href.startswith('//'):
                href = 'https:' + href
            elif href.startswith('/'):
                href = url + href
            if href.startswith('http'):
                external_domains['anchor_tags'].add(href)
            if href.startswith('#'):
                external_domains['anchor_tags'].add(url + href)

        if tag.has_attr('src') or tag.name == 'link' or tag.name == 'script' or tag.name == 'iframe' or tag.name == 'a':
            if '://' in tag.get('src', ''):
                subdomains.add(tag.get('src').split('://')[1].split('/')[0])
            if '://' in tag.get('href', ''):
                subdomains.add(tag.get('href').split('://')[1].split('/')[0])
    
    return render_template('result.html', domain=domain, server_ip=server_ip, location=location, asn=asn, isp=isp,
                           organization=organization, subdomains=subdomains, external_domains=external_domains)

if __name__ == '__main__':
    app.run()