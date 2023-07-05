import maxminddb

class Reader:

    def __init__(self):
        self.db = None

    def read(self, path):
        '''Opens the MMDB file located at the given path.

        :param: path: Path to MMDB file.
        :return: db reader.
        :rtype: Reader
        '''
        self.db = maxminddb.open_database(path)
        return self.db
    
    def getDetails(self, ip):
        '''Returns all the country and ASN level IP information available for the input IP address in a dictionary format.

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: All available country and ASN level information of the IP address.
        :rtype: dict
        '''
        return self.db.get(ip)

    def getCountry(self, ip):
        '''Returns the ISO 3166 country code of the input.

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Country code of the IP address.
        :rtype: str
        '''
        return self._get_data_field(ip, 'country')
    
    def getCountryName(self, ip):
        '''Returns the country name of the input IP address.

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Country name of the IP address.
        :rtype: str
        '''
        return self._get_data_field(ip, 'country_name')
    
    def getContinent(self, ip):
        '''Returns the continent shortcode of the input IP address.

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Continent code of the IP address.
        :rtype: str
        '''
        return self._get_data_field(ip, 'continent')
    
    def getContinentName(self, ip):
        '''Returns the name of the continent of the input IP address.

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Continent name of the IP address.
        :rtype: str
        '''
        return self._get_data_field(ip, 'continent_name')
    
    def getASN(self, ip):
        '''Returns the ASN (Autonomous System Number) of the input IP address.

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: ASN (i.e. 	AS2381) of the IP address.
        :rtype: str
        '''
        return self._get_data_field(ip, 'asn')
    
    def getASNName(self, ip):
        '''Returns the AS (Autonomous System) organization of the input ip address.

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: AS name of the IP address.
        :rtype: str
        '''
        return self._get_data_field(ip, 'as_name')
    
    def getASNDomain(self, ip):
        '''Returns the domain or the official website of the input IP address.

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Domain or website of the AS organization owning the IP address.
        :rtype: str
        '''
        return self._get_data_field(ip, 'as_domain')

    def getCountryDetails(self, ip):
        '''Returns the country level geolocation information of the input ip address.
        country, country_name, continent, and continent_name

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Country and continent information of the IP address.
        :rtype: dict
        '''
        fields = ["country", "country_name", "continent", "continent_name"]
        return self._get_data_dictionary(ip, fields)

    def getASNDetails(self, ip):
        '''Returns all the available ASN-level information of the input IP address.
        asn, as name, and as_domain

        :param: ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: ASN-level information of the IP address.
        :rtype: dict
        '''
        fields = ["asn", "as_domain", "as_name"]
        return self._get_data_dictionary(ip, fields)
    
    def _get_data_field(self, ip, field):
        data = self.db.get(ip)
        return data[field] if data else None

    def _get_data_dictionary(self, ip, fields):
        data = self.db.get(ip)
        return {key:data[key] for key in fields if key in data}
