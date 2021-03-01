from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
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
            'payoff': self.participant.payoff,
            'total_payoff': self.participant.payoff + c(500),
            'total_eur': self.participant.payoff_plus_participation_fee(),
            'is_dropout': self.participant.vars['is_dropout'],
            'is_dropout_mate': self.participant.vars['is_dropout_mate'],
            'is_dofus': self.participant.vars['is_dofus']
        }

page_sequence = [PaymentInfo]