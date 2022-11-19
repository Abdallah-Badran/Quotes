from flask import jsonify
from models import QuoteModel


class QuoteView:
    def __init__(self):
        self.quote = QuoteModel()
        self.author = {'name': 'quoteAuthor'}
    
    def send(self):
        return jsonify({
            "quoteId": self.quote.id,
            "quote": self.quote.text,
            "author": self.author['name']
        }), 200
