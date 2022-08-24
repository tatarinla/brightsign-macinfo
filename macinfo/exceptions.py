class APIClientError(Exception):
    def __repr__(self, message):
        return self.message
