# flask-website-analyser
Python-Flask-based application to conduct basic analysis on any given website. The application will accept a website URL as input and return the following information: 

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
	


Output Format:

 {
  "info": {
    "ip": "132.226.44.1",
    "isp": "Oracle Corporation",
    "organization": "Oracle Corporation",
    "asn": "AS31898",
    "location": "US"
  },
  "subdomains": [
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
  ],
  "asset_domains": {
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
