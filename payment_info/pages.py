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
            'payoff_eur': self.participant.payoff.to_real_world_currency(self.session),
            'total_payoff': self.participant.payoff,
            'is_dropout': self.participant.vars['is_dropout'],
            'is_dropout_mate': self.participant.vars['is_dropout_mate'],
            'completion_code': self.session.config['completion_code']
        }

page_sequence = [PaymentInfo]