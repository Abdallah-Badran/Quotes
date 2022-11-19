from pandas import read_json


class AuthorModel:
    DATA = read_json('./models/authors/authors.json')

    def __init__(self, quote_id):
        self.name = AuthorModel.DATA[AuthorModel.DATA['quoteIds'].apply(
            lambda quote_ids: quote_id in quote_ids)].values[0][1]
