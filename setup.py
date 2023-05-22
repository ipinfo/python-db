from setuptools import setup

from ipinfo_db.version import SDK_VERSION

long_description = """
The official Python free database library for IPinfo.

IPinfo prides itself on being the most reliable, accurate, and in-depth source of IP address data available anywhere.
We process terabytes of data to produce our custom IP geolocation, company, carrier and IP type data sets.
You can visit our developer docs at https://ipinfo.io/developers.
"""

setup(
    name="ipinfo_db",
    version=SDK_VERSION,
    description="Official Python free database library for IPinfo",
    long_description=long_description,
    url="https://github.com/ipinfo/python-db",
    author="IPinfo",
    author_email="support@ipinfo.io",
    license="Apache License 2.0",
    packages=["ipinfo_db"],
    install_requires=["maxminddb", "appdirs"],
    include_package_data=True,
    zip_safe=False,
)
