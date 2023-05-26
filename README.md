# flask-website-analyser
Flask-based application to conduct basic analysis on any given website. The application will accept a website URL as input and return the following information: 

Domain Information
Server IP
Location (Country)
ASN
ISP
Organization
Subdomain Information
List of external domains from which 
Style sheets are being fetched
Javascripts are being fetched.
images are being fetched.
Iframe sources
Anchor tag references (a hrefs)
	
WebSocket endpoint at "/ws". JSON data will be utilized for communication between the WebSocket and the client. Once the WebSocket connection is established, the first message should contain a "url" attribute. Subsequent messages will include an "operation" attribute, indicating the desired action to perform, such as "get_info", "get_subdomains", or "get_asset_domains". Below are sample messages:

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

	
	
	
https://web-analyser-flask.herokuapp.com/
