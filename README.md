# [<img src="https://ipinfo.io/static/ipinfo-small.svg" alt="IPinfo" width="24"/>](https://ipinfo.io/) IPinfo Python Free Database Library

This is the official Python library for IPinfo.io's free [IP to Country ASN Database](https://ipinfo.io/products/free-ip-database), allowing you to lookup country and ASN details for IP addresses.

## Getting Started

You'll need an IPinfo API access token (which you can get by singing up for a free account at [https://ipinfo.io/signup](https://ipinfo.io/signup)) if you want to download the free database or you can provide the path to the mmdb file.

### Installation

This package works with Python 3.5 or greater. However, we only officially
support non-EOL Python versions.

```bash
pip install ipinfodb
```

### Quick Start

```python
>>> import ipinfodb
>>> access_token = '123456789abc'
>>> client = ipinfodb.Client(access_token)
>>> ip_address = '216.239.36.21'
>>> country = client.getCountry(ip_address)
>>> country
'US'
```
Client will download the free `country_asn` mmdb database if it doesn't exist or the path to the mmdb file is not provided. If the database exists in default path it'll skip the download but can be forced to replace the old file by providing `replace=True` while initializing client object.
```python
>>> client = ipinfodb.Client(access_token, replace=True)
```
### Available Methods

- getCountry(ip)
- getCountryName(ip)
- getContinent(ip)
- getContinentName(ip)
- getASN(ip)
- getASNName(ip)
- getASNDomain(ip)

## Other Libraries

There are official [IPinfo client libraries](https://ipinfo.io/developers/libraries) available for many languages including PHP, Go, Java, Ruby, and many popular frameworks such as Django, Rails and Laravel. There are also many third party libraries and integrations available for our API.

## About IPinfo

Founded in 2013, IPinfo prides itself on being the most reliable, accurate, and in-depth source of IP address data available anywhere. We process terabytes of data to produce our custom IP geolocation, company, carrier, VPN detection, hosted domains, and IP type data sets. Our API handles over 40 billion requests a month for 100,000 businesses and developers.

[![image](https://avatars3.githubusercontent.com/u/15721521?s=128&u=7bb7dde5c4991335fb234e68a30971944abc6bf3&v=4)](https://ipinfo.io/)
