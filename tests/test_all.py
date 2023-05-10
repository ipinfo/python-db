import pytest
import ipinfodb


client = ipinfodb.Client(path='./tests/tests_db.mmdb')


def test_get_country():
    assert(client.getCountry("8.8.8.8"), "US")

def test_get_country_name():
    assert(client.getCountryName('8.8.8.8'),"United States")

def test_get_continent():
    assert(client.getContinent('8.8.8.8'),"NA")

def test_get_continent_name():
    assert(client.getContinentName('8.8.8.8'),"North America")

def test_get_asn():
    assert(client.getASN('8.8.8.8'),"AS15169")

def test_get_asn_name():
    assert(client.getASNName('8.8.8.8'),"Google LLC")

def test_get_asn_domain():
    assert(client.getASNDomain('8.8.8.8'),"google.com")
