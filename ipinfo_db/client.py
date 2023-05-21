import maxminddb
import urllib.request
import os
import appdirs

DB_DOWNLOAD_URL = "https://ipinfo.io/data/free/country_asn.mmdb?token="
DEFAULT_APP_PATH = appdirs.user_data_dir(appname='ipinfo_db', appauthor='ipinfo') 
DEFAULT_DB_PATH = os.path.join(DEFAULT_APP_PATH, 'files/country_asn.mmdb')

class Client:

    def __init__(self, access_token=None, path=None, replace=False):
        self.access_token = access_token
        self.path = path
        self.replace = replace

        if self.access_token is None and self.path is None:
            raise SyntaxError("Token or Path is required")
            
        if self.path is None:
            self.path = DEFAULT_DB_PATH

        # Check if file already exists to skip the download.
        if os.path.exists(self.path) and not self.replace:
            pass
        else:
            if self.access_token is None:
                raise SyntaxError("Token is required to download the file")
            
            # Create directory if doesn't exist and download file.
            directory = os.path.dirname(self.path)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                urllib.request.urlretrieve(DB_DOWNLOAD_URL+self.access_token, self.path)

        # Read the mmdb file.
        self.db = maxminddb.open_database(self.path)

    def getDetails(self, ip):
        return self.db.get(ip)

    def getCountry(self, ip):
        return self._get_data_field(ip, 'country')
    
    def getCountryName(self, ip):
        return self._get_data_field(ip, 'country_name')
    
    def getContinent(self, ip):
        return self._get_data_field(ip, 'continent')
    
    def getContinentName(self, ip):
        return self._get_data_field(ip, 'continent_name')
    
    def getASN(self, ip):
        return self._get_data_field(ip, 'asn')
    
    def getASNName(self, ip):
        return self._get_data_field(ip, 'as_name')
    
    def getASNDomain(self, ip):
        return self._get_data_field(ip, 'as_domain')

    def getCountryDetails(self, ip):
        fields = ["country", "country_name", "continent", "continent_name"]
        return self._get_data_dictionary(ip, fields)

    def getASNDetails(self, ip):
        fields = ["asn", "as_domain", "as_name"]
        return self._get_data_dictionary(ip, fields)
    
    def _get_data_field(self, ip, field):
        data = self.db.get(ip)
        return data[field] if data else None

    def _get_data_dictionary(self, ip, fields):
        data = self.db.get(ip)
        return {k:data[key] for key in fields if key in data}