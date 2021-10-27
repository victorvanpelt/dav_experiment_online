from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as cu, currency_range
from .models import Constants

class PaymentInfo(Page):
    form_model = 'player'
    form_fields = [
        'mturk_feedback'
    ]

    def vars_for_template(self):
        return {
            #'redemption_code': self.participant.label or self.participant.code,
            'participation_fee': self.session.config['participation_fee'],
            'payoff': self.player.participant.payoff,
            'total_payoff': self.player.participant.payoff + cu(500),
            'total_eur_main': (self.player.participant.payoff + cu(500)).to_real_world_currency(self.player.session),
            'total_eur': self.player.participant.payoff_plus_participation_fee(),
            'is_dropout': self.player.participant.is_dropout,
            'is_dropout_mate': self.player.participant.is_dropout_mate,
            'is_dofus': self.player.participant.is_dofus
        }

page_sequence = [PaymentInfo]