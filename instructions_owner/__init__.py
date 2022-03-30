import time

from otree.api import *


doc = """
Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions_four'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    communication = models.IntegerField()
    self_selection = models.IntegerField()
    Instr1 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr2 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr3 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)


# FUNCTIONS
def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.participant.is_dofus = False
        p.participant.is_dropout = False
        p.participant.is_dropout_mate = False

# PAGES
class Instruct_one(Page):
    form_model = 'player'
    form_fields = ['Instr1']

class Instruct_two(Page):
    form_model = 'player'
    form_fields = ['Instr2']

class Instruct_three(Page):
    form_model = 'player'
    form_fields = ['Instr3']

page_sequence = [
    Instruct_one,
    Instruct_two,
    Instruct_three
]
