import os
import base64
import requests
from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import urlparse
app = Flask(__name__)

# Allowed domains for secure fetching
ALLOWED_DOMAINS = [
    'example.com',
    'imgur.com',
    'ibb.co',
    'postimg.cc',
    'static.wikia.nocookie.net'
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    
    if not url:
        return render_template('index.html', error="Please provide a URL")
    
    if not url.lower().endswith('.png'):
        return render_template('index.html', error="Only PNG images are supported. URL must end with .png")
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.google.com/'
        }
        
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            
            if 'image' in content_type:
                image_data = base64.b64encode(response.content).decode('utf-8')
                return render_template('index.html', image_data=image_data, content_type=content_type)
            else:
                return render_template('index.html', error=f"Content fetched: {response.text}")
        else:
            return render_template('index.html', error=f"Failed to fetch: HTTP {response.status_code}")
            
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

@app.route('/secure-fetch')
def secure_fetch():
    url = request.args.get('url')
    
    if not url:
        return render_template('index.html', error="Please provide a URL")
    
    # Basic URL validation
    if not url.startswith(('http://', 'https://')):
        return render_template('index.html', error="Only HTTP/HTTPS protocols are allowed")
    
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Validate domain
    domain = parsed_url.netloc.lower()
    if ":" in domain:  # Remove port if present
        domain = domain.split(":")[0]
    
    # Check if domain is allowed
    allowed = False
    for allowed_domain in ALLOWED_DOMAINS:
        if domain == allowed_domain or domain.endswith('.' + allowed_domain):
            allowed = True
            break
    
    if not allowed:
        return render_template('index.html', error="Domain not in whitelist")
    
    # Check if URL points to image
    if not parsed_url.path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
        return render_template('index.html', error="URL must point to an image file")
    
    try:
        content_type = response.headers.get('Content-Type', '')
        
        # Verify content is an image
        if not content_type.startswith('image/'):
            return render_template('index.html', error=f"Not an image: Content-Type is {content_type}")
        
        # Limit response size to prevent DoS
        content = response.content[:5 * 1024 * 1024]  # Limit to 5MB
        
        image_data = base64.b64encode(content).decode('utf-8')
        return render_template('index.html', image_data=image_data, content_type=content_type)
            
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 
