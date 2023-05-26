# flask-website-analyser
**TLDR: run ```python3 app.py``` (server) & ```python3 client.py``` (client)**
<br></br>


Flask-based application to conduct basic analysis on any given website. The application will accept a website URL as input and return the following information: 

Domain Information
<br></br>
Server IP
<br></br>
Location (Country)
<br></br>
ASN
<br></br>
ISP
<br></br>
Organization
<br></br>
Subdomain Information
<br></br>
List of external domains from which 
Style sheets are being fetched
Javascripts are being fetched.
<br></br>
images are being fetched.
<br></br>
Iframe sources
<br></br>
Anchor tag references (a hrefs)
<br></br>
example
**http://app-endpoint/?url=https://www.pentesteracademy.com**
<br></br>
<br></br>
WebSocket endpoint at "/ws". JSON data will be utilized for communication between the WebSocket and the client. Once the WebSocket connection is established, the first message should contain a "url" attribute. Subsequent messages will include an "operation" attribute, indicating the desired action to perform, such as "get_info", "get_subdomains", or "get_asset_domains". Below are sample messages:

```javascript

Input: {"url":"www.pentesteracademy.com"}
Output: {"data":"session created for www.pentesteracademy.com"}

Input: {"operation":"get_info"}

Output:
{"data": {
    "ip": "132.226.44.1",
    "isp": "Oracle Corporation",
    "organization": "Oracle Corporation",
    "asn": "AS31898",
    "location": "US"
  }
}

Input: {"operation":"get_subdomains"}

Output:
{ "data": [
    "blackhat.pentesteracademy.com",
    "www.promos.pentesteracademy.com",
    "promo.pentesteracademy.com",
    "attackdefense.pentesteracademy.com",
    "www.attackdefense.pentesteracademy.com",
    "bootcamps.pentesteracademy.com",
    "www.blog.pentesteracademy.com",
    "blog.pentesteracademy.com",
    "promos.pentesteracademy.com",
    "www.custompay.pentesteracademy.com",
    "www.pentesteracademy.com",
    "custompay.pentesteracademy.com",
    "community.pentesteracademy.com"
   ]}


Input: {"operation":"get_asset_domains"}

Output:
{"data": {
    "javascripts": [],
    "stylesheets": [
      "fonts.googleapis.com"
    ],
    "images": [
      "s3.amazonaws.com"
    ],
    "iframes": [
      "www.googletagmanager.com"
    ],
    "anchors": [
      "twitter.com",
      "bootcamps.pentesteracademy.com"
    ]
  }
}
```
	
App without websocket @
https://web-analyser-flask.herokuapp.com/
