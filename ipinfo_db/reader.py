import maxminddb

class Reader:

    def __init__(self, path):
        '''Initializes the Reader object with the given path.

        :param: path: Path to the mmdb file.
        '''
        self.db = maxminddb.open_database(path)

    def open(self, path):
        '''Opens an mmdb file located at the given path. Closes previously opened database.

        :param: path: Path to the mmdb file.
        '''
        self.close()
        self.db = maxminddb.open_database(path)

    def close(self):
        '''Closes the database.
        '''
        self.db.close()

    def metadata(self):
        '''Returns the metadata associated with the mmdb file.

        :return: metadata of the mmdb file.
        :rtype: Metadata
        '''
        return self.db.metadata()

    def get(self, ip):
        '''Returns the database record for the given IP address.

        :param: ip: An IP address in string format. Can be either IPv4 or IPv6.
        :return: Database record for the given IP.
        :rtype: Record
        '''
        return self.db.get(ip)

    def getWithPrefixLen(self, ip):
        '''Returns a tuple containing the database record and the associated (network) prefix length.

        :param: ip: An IP address in string format. Can be either IPv4 or IPv6.
        :return: A tuple containing the database record and the prefix length.
        :rtype: Tuple
        '''
        return self.db.get_with_prefix_len(ip)
