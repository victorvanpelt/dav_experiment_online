import itertools
import random

from otree.api import *

from . import models


doc = """
Last page
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
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
