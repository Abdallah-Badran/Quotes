from flask import jsonify
from models import QuoteModel, AuthorModel
from datetime import datetime


class QuoteView:
    SUCCESS_CALLS_COUNT = 0

    def __init__(self):
        self.quote = QuoteModel()
        self.author = AuthorModel(self.quote.id)
    
    def send(self):
        return jsonify({
            "quoteId": self.quote.id,
            "quote": self.quote.text,
            "author": self.author.name
        }), 200

    def register(self):
        QuoteView.SUCCESS_CALLS_COUNT += 1
        curr_date = datetime.now()
        QuoteModel.DATA.loc[self.quote.index, 'Count'] += 1
        if QuoteView.SUCCESS_CALLS_COUNT == 100:
            sheet_name = f"quotes_api_report_{curr_date.year}_{curr_date.month:02d}_{curr_date.day:02d}_" \
                         f"{curr_date.hour:02d}_{curr_date.minute:02d}_{curr_date.second:02d}.xlsx"
            QuoteModel.DATA.to_excel(
                f"./views/calls_reports/{sheet_name}", index=False, columns=['id', 'Count'],
                header=['Quote ID', 'Count'])
            QuoteView.SUCCESS_CALLS_COUNT = 0
