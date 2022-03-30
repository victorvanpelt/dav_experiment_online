import time
from otree.api import *


doc = """
Instructions
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions_three'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    dofus = models.BooleanField(initial=False)
    # drop_out = models.BooleanField(initial=False)
    communication = models.IntegerField()
    self_selection = models.IntegerField()
    # Control questions for instructions (removed blank=False)
    Instr1 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr2 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr3 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr4 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)


# FUNCTIONS
def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.participant.is_dofus = False
        p.participant.is_dropout = False
        p.participant.is_dropout_mate = False
        if subsession.session.config['communication'] == 1:
            p.participant.communication = 1
            p.communication = 1
        elif subsession.session.config['communication'] == 0:
            p.participant.communication = 0
            p.communication = 0
        else:
            if subsession.id_in_subsession % 2 == 0:
                p.participant.communication = 1
                p.communication = 1
            else:
                p.participant.communication = 0
                p.communication = 0
        if subsession.session.config['self_selection'] == 1:
            p.participant.self_selection = 1
            p.self_selection = 1
        elif subsession.session.config['self_selection'] == 0:
            p.participant.self_selection = 0
            p.self_selection = 0
        else:
            if subsession.id_in_subsession % 2 == 0:
                p.participant.self_selection = 1
                p.self_selection = 1
            else:
                p.participant.self_selection = 0
                p.self_selection = 0


def dofus_trigger(player: Player):
    player.payoff = cu(0)


# PAGES
class Instruct_one(Page):
    form_model = 'player'
    form_fields = ['Instr1']

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 180

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.Instr1 != 2 or timeout_happened:
            player.participant.is_dofus = True
            player.dofus = True
            dofus_trigger(player)

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.dofus:
            return upcoming_apps[-1]


class Instruct_two(Page):
    form_model = 'player'
    form_fields = ['Instr2']

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 180

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.Instr2 != 1 or timeout_happened:
            player.participant.is_dofus = True
            player.dofus = True
            dofus_trigger(player)

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        # if player.Instr1 != 2 or timeout_happened:
        if player.dofus:
            return upcoming_apps[-1]


class Instruct_three(Page):
    form_model = 'player'
    form_fields = ['Instr3']

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 180

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.Instr3 != 1 or timeout_happened:
            player.participant.is_dofus = True
            player.dofus = True
            dofus_trigger(player)

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.dofus:
            return upcoming_apps[-1]


class Instruct_four(Page):
    form_model = 'player'
    form_fields = ['Instr4']

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 180

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.wait_page_arrival = time.time()
        if player.Instr4 != 1 or timeout_happened:
            player.participant.is_dofus = True
            player.dofus = True
            dofus_trigger(player)

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if player.dofus:
            return upcoming_apps[-1]


page_sequence = [
    Instruct_one,
    Instruct_two,
    Instruct_three,
    Instruct_four,
]
