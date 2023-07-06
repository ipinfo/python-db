import maxminddb

class Reader:

    def __init__(self, path):
        self.db = maxminddb.open_database(path)

    def open(self, path):
        self.close()
        self.db = maxminddb.open_database(path)

    def close(self):
        self.db.close()

    def get(self, ip):
        return self.db.get(ip)
    
    def metadata(self):
        return self.db.metadata()
