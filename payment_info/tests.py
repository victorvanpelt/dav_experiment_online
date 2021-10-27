from otree.api import Currency as c, currency_range
from . import views
from otree.api import Bot


class PlayerBot(Bot):

    def play_round(self):
        yield views.PaymentInfo, dict(saved_number=True)

