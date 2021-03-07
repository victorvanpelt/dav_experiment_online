import random
import itertools
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


author = 'Victor'

doc = """
DAV Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'dav_game'
    players_per_group = 2
    num_rounds = 1

    #Maximum cost realization and report
    max_cost = cu(6000)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    cost_realization = models.CurrencyField()
    communication = models.IntegerField()
    self_selection = models.IntegerField()

    def assign_stuff(self):
        # Assign cost realization and base dropout variables
        self.cost_realization = cu(random.randint(4000,6000))

        # Load dropout variables
        for p in self.get_players():
            p.drop_out = p.participant.is_dropout
            p.drop_out_mate = p.participant.is_dropout_mate
            p.dofus = p.participant.is_dofus

        # Load conditions based on session config else randomize per dyad
            if p.participant.communication == 1:
                self.communication = 1
            elif p.participant.communication == 0:
                self.communication = 0
            if p.participant.self_selection == 1:
                self.self_selection = 1
            elif p.participant.self_selection == 0:
                self.self_selection = 0

    # This method triggers when a participant drop out due to time-out
    def drop_out_trigger_one(self):
        for p in self.get_players():
            if p.id_in_group == 1:
                p.participant.is_dropout = True
                p.drop_out = True
                p.payoff = -cu(500)
            elif p.id_in_group == 2:
                p.participant.is_dropout_mate = True
                p.drop_out_mate = True
                if p.participant.is_dropout == False:
                    p.payoff = cu(0)

    def drop_out_trigger_two(self):
        for p in self.get_players():
            if p.id_in_group == 2:
                p.participant.is_dropout = True
                p.drop_out = True
                p.payoff = -cu(500)
            elif p.id_in_group == 1:
                p.participant.is_dropout_mate = True
                p.drop_out_mate = True
                if p.participant.is_dropout == False:
                    p.payoff = cu(0)

    check_recommendation_one = models.IntegerField(initial=None, blank=True)
    recommendation_one = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)

    def recommendation_one_min(self):
        return self.cost_realization

    check_recommendation_two = models.IntegerField(initial=None, blank=True)
    recommendation_two = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost)

    def recommendation_two_min(self):
        return self.cost_realization

    select_one = models.BooleanField(initial=False, blank=True)

    select_two = models.BooleanField(initial=False, blank=True)

    check_report_one = models.IntegerField(initial=None, blank=True)
    report_one = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost)

    def report_one_min(self):
        return self.cost_realization

    check_report_two = models.IntegerField(initial=None, blank=True)
    report_two = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)

    def report_two_min(self):
        return self.cost_realization

    group_report = models.CurrencyField(initial=None,blank=False)

    # Which report will be selected?
    select_report_one = models.IntegerField()
    select_report_two = models.IntegerField()

    payoff_one = models.CurrencyField(blank=True, initial=None)
    payoff_two = models.CurrencyField(blank=True, initial=None)
    group_profit = models.CurrencyField(blank=True, initial=None)

    role_random_last = models.IntegerField(Initial=0)

    def set_report_payoffs(self):
        if self.self_selection == 1:
            if self.select_one == 1 and self.select_two == 0:
                self.group_report = self.report_one
                self.select_report_one = 1
                self.select_report_two = 0
            elif self.select_one == 0 and self.select_two == 1:
                self.group_report = self.report_two
                self.select_report_one = 0
                self.select_report_two = 1
            else:
                role_random_last = random.randint(1, 2)
                self.role_random_last = role_random_last
                if role_random_last == 1:
                    self.group_report = self.report_one
                    self.select_report_one = 1
                    self.select_report_two = 0
                elif role_random_last == 2:
                    self.group_report = self.report_two
                    self.select_report_one = 0
                    self.select_report_two = 1
        else:
            role_random = random.randint(1, 2)
            if role_random == 1:
                self.group_report = self.report_one
                self.select_report_one = 1
                self.select_report_two = 0
            else:
                self.group_report = self.report_two
                self.select_report_one = 0
                self.select_report_two = 1

        self.group_profit = self.group_report - self.cost_realization
        self.payoff_one = self.group_profit / 2
        self.payoff_two = self.group_profit / 2

        for p in self.get_players():
            if p.id_in_group == 1:
                p.payoff = self.payoff_one
            elif p.id_in_group == 2:
                p.payoff = self.payoff_two

    # def dofus_trigger(self):
    #     for p in self.get_players():
    #         if p.dofus == 1:
    #             p.payoff = cu(0)

class Player(BasePlayer):
    #Dropout indicator
    drop_out = models.BooleanField(initial=False)
    drop_out_mate = models.BooleanField(initial=False)
    dofus = models.BooleanField(initial=False)

    # Control questions for instructions (removed blank=False)
    Instr1 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr2 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr3 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr4 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)