import random
import itertools
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
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
    max_cost = c(6000)

    #Fixed salary
    fixed_salary = c(500)


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    cost_realization = models.CurrencyField()
    communication = models.IntegerField()
    self_selection = models.IntegerField()

    def assign_stuff(self):
        # Assign cost realization and base dropout variables
        self.cost_realization = c(random.randint(4000,6000))
        for p in self.get_players():
            p.participant.vars['is_dropout'] = False
            p.participant.vars['is_dropout_mate'] = False

        # Assign conditions based on session config else randomize per dyad
        if self.session.config['communication'] == 1:
            self.communication = 1
        elif self.session.config['communication'] == 0:
            self.communication = 0
        else:
            # comm_condition = itertools.cycle([0, 1])
            # self.communication = next(comm_condition)
            # self.communication = random.randint(0,1)
            if self.id_in_subsession % 2 == 0:
                self.communication = 1
            else:
                self.communication = 0
        if self.session.config['self_selection'] == 1:
            self.self_selection = 1
        elif self.session.config['self_selection'] == 0:
            self.self_selection = 0
            # return self.self_selection
        else:
            # sel_condition = itertools.cycle([0, 1])
            # self.self_selection = next(sel_condition)
            # self.self_selection = random.randint(0,1)
            if self.id_in_subsession % 2 == 0:
                self.self_selection = 1
            else:
                self.self_selection = 0

    # This method triggers when a participant drop out either due to time-out or getting a question wrong
    def drop_out_trigger_one(self):
        for p in self.get_players():
            if p.id_in_group == 1:
                p.participant.vars['is_dropout'] = True
                p.drop_out = True
                p.payoff = c(0)
            elif p.id_in_group == 2:
                p.participant.vars['is_dropout_mate'] = True
                p.drop_out_mate = True
                if p.participant.vars['is_dropout'] == False:
                    p.payoff = c(185)

    def drop_out_trigger_two(self):
        for p in self.get_players():
            if p.id_in_group == 2:
                p.participant.vars['is_dropout'] = True
                p.drop_out = True
                p.payoff = c(0)
            elif p.id_in_group == 1:
                p.participant.vars['is_dropout_mate'] = True
                p.drop_out_mate = True
                if p.participant.vars['is_dropout'] == False:
                    p.payoff = c(185)

    check_recommendation_one = models.IntegerField(initial=None, blank=True)
    recommendation_one = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)

    def recommendation_one_min(self):
        return self.cost_realization

    check_recommendation_two = models.IntegerField(initial=None, blank=True)
    recommendation_two = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost)

    def recommendation_two_min(self):
        return self.cost_realization

    select_one = models.BooleanField(initial=False, blank=True)

    # select_one = models.IntegerField(
    #     blank=False,
    #     widget=widgets.RadioSelect
    # )
    # def select_one_choices(self):
    #     choices = [
    #         [0, 'I do not want to assume the manager`s role'],
    #         [1, 'I want to assume the manager`s role']
    #     ]
    #     random.shuffle(choices)
    #     return choices

    select_two = models.BooleanField(initial=False, blank=True)

    # select_two = models.IntegerField(
    #     blank=False,
    #     widget=widgets.RadioSelect
    # )
    #
    # def select_two_choices(self):
    #     choices = [
    #         [0, 'I do not want to assume the manager`s role'],
    #         [1, 'I want to assume the manager`s role']
    #     ]
    #     random.shuffle(choices)
    #     return choices

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
                p.payoff = self.payoff_one + Constants.fixed_salary
            elif p.id_in_group == 2:
                p.payoff = self.payoff_two + Constants.fixed_salary


class Player(BasePlayer):
    #Dropout indicator
    drop_out = models.BooleanField(initial=False)
    drop_out_mate = models.BooleanField(initial=False)

    # Agree to terms of participation at start.
    accept_conditions = models.BooleanField(blank=False)

    # Control questions for instructions (removed blank=False)
    Instr1 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr2 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr3 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr4 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)