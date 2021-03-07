from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as cu,
    currency_range,
)


doc = """
Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.is_dofus = False
            p.participant.is_dropout = False
            p.participant.is_dropout_mate = False

            if self.session.config['communication'] == 1:
                p.participant.communication = 1
                p.communication = 1
            elif self.session.config['communication'] == 0:
                p.participant.communication = 0
                p.communication = 0
            else:
                if self.id_in_subsession % 2 == 0:
                    p.participant.communication = 1
                    p.communication = 1
                else:
                    p.participant.communication = 0
                    p.communication = 0
            if self.session.config['self_selection'] == 1:
                p.participant.self_selection = 1
                p.self_selection = 1
            elif self.session.config['self_selection'] == 0:
                p.participant.self_selection = 0
                p.self_selection = 0
            else:
                if self.id_in_subsession % 2 == 0:
                    p.participant.self_selection = 1
                    p.self_selection = 1
                else:
                    p.participant.self_selection = 0
                    p.self_selection = 0


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

    def dofus_trigger(self):
        self.payoff = -cu(500)