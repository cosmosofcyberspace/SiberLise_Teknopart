# SSRF Lab - Internal Access

This lab demonstrates a Server-Side Request Forgery (SSRF) vulnerability that allows an attacker to access internal resources.

## Overview

The lab consists of two components:
1. A vulnerable web application that fetches images from URLs provided by users
2. An internal server running on localhost that contains a flag

The goal is to exploit the SSRF vulnerability in the web application to access the internal flag server.

## Setup

### Option 1: Standard Setup

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the lab:
```
python main.py
```

### Option 2: Docker Setup

1. Build the Docker image:
```
docker build -t ssrf-lab .
```

2. Run the container:
```
docker run -p 5000:5000 -p 5001:5001 ssrf-lab
```

Both setup options will start:
- The vulnerable web application on http://localhost:5000
- The internal flag server on http://127.0.0.1:5001 (not directly accessible)

## Objective

Your goal is to retrieve the flag from the internal server (http://127.0.0.1:5001/flag.txt) by exploiting the SSRF vulnerability in the web application.

## Exploitation

1. Visit http://localhost:5000 in your browser
2. In the "Image URL" field, enter: http://127.0.0.1:5001/flag.txt#.png
3. Click "Fetch Image"
4. The application will display the flag in the error message

## Security Notes

This vulnerability occurs because the application doesn't validate the user-supplied URL, allowing an attacker to make the server request internal resources that should not be accessible.

To prevent SSRF vulnerabilities:
- Validate and sanitize user input
- Use allowlists for domains and IP ranges
- Block requests to private IP ranges and localhost
- Implement additional access controls

## Learning Resources

- [OWASP SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)
- [PortSwigger SSRF](https://portswigger.net/web-security/ssrf) 
