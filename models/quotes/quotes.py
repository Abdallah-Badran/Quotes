from pandas import read_json


class QuoteModel:
    DATA = read_json('./models/quotes/quotes.json') 
    DATA.insert(1, 'Count', 0)

    def __init__(self):
        random_quote = QuoteModel.DATA.sample()
        random_quote_values = random_quote.values[0] 
        self.id = random_quote_values[0]
        self.text = random_quote_values[2]
        self.index = random_quote.index
