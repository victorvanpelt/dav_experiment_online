from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as cu, currency_range
)
import random
import itertools


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
        label="Do you have any feedback for us or anything you would like to say to us?",
        blank=True
    )