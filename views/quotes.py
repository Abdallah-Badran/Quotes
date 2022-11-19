from flask import jsonify
from models import QuoteModel, AuthorModel


class QuoteView:
    def __init__(self):
        self.quote = QuoteModel()
        self.author = AuthorModel(self.quote.id)
    
    def send(self):
        return jsonify({
            "quoteId": self.quote.id,
            "quote": self.quote.text,
            "author": self.author.name
        }), 200
