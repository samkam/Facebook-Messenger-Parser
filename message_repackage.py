#defines message objects to assist with parsing

class Message:
    # class attribute
    date_parser = None
    def __init__(self, timestamp, contents, author):
        self.timestamp = timestamp
        self.contents = contents
        self.author = author