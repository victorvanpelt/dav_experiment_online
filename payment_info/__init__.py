import itertools
import random

from otree.api import *

from . import models


doc = """
Last page
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # #Dropout indicator
    # is_dropout = models.BooleanField(initial=False)
    # is_dropout_mate = models.BooleanField(initial=False)
    # def start(self):
    #     self.is_dropout = self.participant.is_dropout
    #     self.is_dropout_mate = self.participant.is_dropout_mate
    #     if self.is_dropout == True:
    #         self.payoff = cu(0)
    #     elif self.is_dropout_mate == True and self.is_dropout == False:
    #         self.payoff = cu(185)
    mturk_feedback = models.TextField(
        label="Do you have any feedback for us or anything you would like to say to us?", blank=True
    )


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    form_model = 'player'
    form_fields = ['mturk_feedback']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'participation_fee': player.session.config['participation_fee'],
            'payoff': player.participant.payoff,
            'total_payoff': player.participant.payoff,
            'total_eur_main': (player.participant.payoff).to_real_world_currency(
                player.session
            ),
            'total_eur': player.participant.payoff_plus_participation_fee(),
            'is_dropout': player.participant.is_dropout,
            'is_dropout_mate': player.participant.is_dropout_mate,
            'is_dofus': player.participant.is_dofus,
        }


page_sequence = [PaymentInfo]
