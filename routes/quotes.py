from flask import Blueprint
from views import QuoteView
from flask_cors import cross_origin

quotes_routes = Blueprint("quotes_routes", __name__)


@quotes_routes.get('/quote/random')
@cross_origin()
def get_quote():
    quote = QuoteView()
    quote.register()
    return quote.send()
