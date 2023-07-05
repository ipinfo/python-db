import urllib.request
import os
import appdirs
from ipinfo_db.reader import Reader

DB_DOWNLOAD_URL = "https://ipinfo.io/data/free/country_asn.mmdb?token="
DEFAULT_APP_PATH = appdirs.user_data_dir(appname='ipinfo_db', appauthor='ipinfo') 
DEFAULT_DB_PATH = os.path.join(DEFAULT_APP_PATH, 'files/country_asn.mmdb')

class Client:

    def __init__(self, access_token=None, path=None, replace=False):
        f'''ipinfo_db handler method.

        :param access_token: Optional. Type: str. IPinfo access token to download the IP to Country ASN database required in case of data download.
        :param path: Optional. Type: str. Download path for the database. Default is set to: {DEFAULT_DB_PATH}
        :param replace: Optional. Type: bool. Set it to True if you want to replace your older downloaded database.
        :return: Client handler object.
        '''
        self.access_token = access_token
        self.path = path
        self.replace = replace
        self.reader = Reader()

        if self.access_token is None and self.path is None:
            raise SyntaxError("Token or Path is required")
            
        if self.path is None:
            self.path = DEFAULT_DB_PATH

        # Check if file already exists to skip the download.
        if os.path.isfile(self.path) and not self.replace:
            pass
        else:
            if self.access_token is None:
                raise SyntaxError("Token is required to download the file")
            
            # Create directory if doesn't exist.
            directory = os.path.dirname(self.path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                
            # Download file.
            urllib.request.urlretrieve(DB_DOWNLOAD_URL+self.access_token, self.path)

        # Read the mmdb file.
        self.db = self.reader.read(self.path)

    def getDetails(self, ip):
        '''Returns all the country and ASN level IP information available for the input IP address in a dictionary format.

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: All available country and ASN level information of the IP address.
        :rtype: dict
        '''
        return self.reader.getDetails(ip)

    def getCountry(self, ip):
        '''Returns the ISO 3166 country code of the input.

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Country code of the IP address.
        :rtype: str
        '''
        return self.reader.getCountry(ip)
    
    def getCountryName(self, ip):
        '''Returns the country name of the input IP address.

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Country name of the IP address.
        :rtype: str
        '''
        return self.reader.getCountryName(ip)
    
    def getContinent(self, ip):
        '''Returns the continent shortcode of the input IP address.

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Continent code of the IP address.
        :rtype: str
        '''
        return self.reader.getContinent(ip)
    
    def getContinentName(self, ip):
        '''Returns the name of the continent of the input IP address.

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Continent name of the IP address.
        :rtype: str
        '''
        return self.reader.getContinentName(ip)
    
    def getASN(self, ip):
        '''Returns the ASN (Autonomous System Number) of the input IP address.

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: ASN (i.e. 	AS2381) of the IP address.
        :rtype: str
        '''
        return self.reader.getASN(ip)
    
    def getASNName(self, ip):
        '''Returns the AS (Autonomous System) organization of the input ip address.

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: AS name of the IP address.
        :rtype: str
        '''
        return self.reader.getASNName(ip)
    
    def getASNDomain(self, ip):
        '''Returns the domain or the official website of the input IP address.

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Domain or website of the AS organization owning the IP address.
        :rtype: str
        '''
        return self.reader.getASNDomain(ip)

    def getCountryDetails(self, ip):
        '''Returns the country level geolocation information of the input ip address.
        country, country_name, continent, and continent_name

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: Country and continent information of the IP address.
        :rtype: dict
        '''
        return self.reader.getCountryDetails(ip)

    def getASNDetails(self, ip):
        '''Returns all the available ASN-level information of the input IP address.
        asn, as name, and as_domain

        :param ip: Input IP address. Supports both IPv4 and IPv6 address.
        :return: ASN-level information of the IP address.
        :rtype: dict
        '''
        return self.reader.getASNDetails(ip)
    