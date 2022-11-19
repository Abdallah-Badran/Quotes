from flask import jsonify


class QuoteView:
    def __init__(self):
        self.quote = {'id': 1, 'text': 'myQuote'}
        self.author = {'name': 'quoteAuthor'}
    
    def send(self):
        return jsonify({
            "quoteId": self.quote['id'],
            "quote": self.quote['text'],
            "author": self.author['name']
        }), 200
