class APIClientError(Exception):
    def __init__(self, message):
        super().__init__(self)
        self.message = message

    def __repr__(self, message):
        return self.message
