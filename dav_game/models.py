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
    max_cost = c(6000.00)

    # Randomly drawn cost realizations
    #cost_realization = [c(251.00), c(379.00), c(44.00), c(343.00), c(61.00), c(199.00), c(73.00), c(300.00), c(96.00), c(195.00), c(65.00)]

class Subsession(BaseSubsession):
    pass
    # def group_by_arrival_time_method(self, waiting_players):
    #     if len(waiting_players) >=2:
    #         return waiting_players[:2]

    # def assign_stuff(self):
    #     # Set cost realization for group
    #     for g in self.get_groups():
    #         g.set_cost_realization()
    #
    #     # Set communication manipulation for group
    #     if self.session.config['communication'] == 1:
    #         for g in self.get_groups():
    #             g.communication = 1
    #     elif self.session.config['communication'] == 0:
    #         for g in self.get_groups():
    #             g.communication = 0
    #     else:
    #         condition = itertools.cycle([1, 0])
    #         for g in self.get_groups():
    #             g.communication = next(condition)
    #
    #     # Set self_selection manipulation for group
    #     if self.session.config['self_selection'] == 1:
    #         for g in self.get_groups():
    #             g.self_selection = 1
    #     elif self.session.config['self_selection'] == 0:
    #         for g in self.get_groups():
    #             g.self_selection = 0
    #     else:
    #         condition = itertools.cycle([1, 0])
    #         for g in self.get_groups():
    #             g.self_selection = next(condition)

    # def creating_session(self):
    #     # Give groups their cost realization at the start
    #     for g in self.get_groups():
    #         g.set_cost_realization()

        #Assigns conditions to people at the start
    # def assign_conditions(self):
    #     if self.session.config['communication'] == 1:
    #         for g in self.get_groups():
    #             g.communication = 1
    #     elif self.session.config['communication'] == 0:
    #         for g in self.get_groups():
    #             g.communication = 0
    #     else:
    #         condition = itertools.cycle([1, 0])
    #         for g in self.get_groups():
    #             g.communication = next(condition)
    #     if self.session.config['self_selection'] == 1:
    #         for g in self.get_groups():
    #             g.communication = 1
    #     elif self.session.config['self_selection'] == 0:
    #         for g in self.get_groups():
    #             g.communication = 0
    #     else:
    #         condition = itertools.cycle([1, 0])
    #         for g in self.get_groups():
    #             g.self_selection = next(condition)

class Group(BaseGroup):
    cost_realization = models.CurrencyField()
    communication = models.IntegerField()
    self_selection = models.IntegerField()

    # def set_cost_realization(self):
    #     self.cost_realization = c(round(random.randint(4000,6000)))
    #     return self.cost_realization

    def assign_stuff(self):
        self.cost_realization = c(round(random.randint(4000,6000)))
        if self.session.config['communication'] == 1:
            self.communication = 1
            # return self.communication
        elif self.session.config['communication'] == 0:
            self.communication = 0
            # return self.communication
        else:
            condition = itertools.cycle([1, 0])
            self.communication = next(condition)
            # return self.communication
        if self.session.config['self_selection'] == 1:
            self.self_selection = 1
            # return self.self_selection
        elif self.session.config['self_selection'] == 0:
            self.self_selection = 0
            # return self.self_selection
        else:
            condition = itertools.cycle([1, 0])
            self.self_selection = next(condition)
            # return self.self_selection

    check_recommendation_one = models.IntegerField(initial=None, blank=True)
    # recommendation_one = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost,widget=widgets.Input(attrs={'step': '1', 'style': 'width:500px'}, show_value=False))
    recommendation_one = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)

    def recommendation_one_min(self):
        return self.cost_realization

    check_recommendation_two = models.IntegerField(initial=None, blank=True)
    # recommendation_two = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost,widget=widgets.Input(attrs={'step': '1', 'style': 'width:500px'}, show_value=False))
    recommendation_two = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost)

    def recommendation_two_min(self):
        return self.cost_realization

    select_one = models.IntegerField(
        blank=False,
        widget=widgets.RadioSelect
    )
    def select_one_choices(self):
        choices = [
            [0, 'I want to assume the assistant`s role'],
            [1, 'I want to assume the manager`s role']
        ]
        random.shuffle(choices)
        return choices

    select_two = models.IntegerField(
        blank=False,
        widget=widgets.RadioSelect
    )

    def select_two_choices(self):
        choices = [
            [0, 'I want to assume the assistant`s role'],
            [1, 'I want to assume the manager`s role']
        ]
        random.shuffle(choices)
        return choices

    check_report_one = models.IntegerField(initial=None, blank=True)
    # report_one = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost,widget=widgets.Input(attrs={'step': '1', 'style': 'width:500px'}, show_value=False))
    report_one = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost)

    def report_one_min(self):
        return self.cost_realization

    check_report_two = models.IntegerField(initial=None, blank=True)
    # report_two = models.CurrencyField(initial=None,blank=False,max=Constants.max_cost,widget=widgets.Input(attrs={'step': '1', 'style': 'width:500px'}, show_value=False))
    report_two = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)

    def report_two_min(self):
        return self.cost_realization

    # All the time-out data decision_making stage
    report_one_to = models.BooleanField(initial=False)
    report_two_to = models.BooleanField(initial=False)
    recommendation_one_to = models.BooleanField(initial=False)
    recommendation_two_to = models.BooleanField(initial=False)
    select_one_to = models.BooleanField(initial=False)
    select_two_to = models.BooleanField(initial=False)

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

class Player(BasePlayer):
    # communication = models.IntegerField()
    # self_selection = models.IntegerField()

    # all time-out data instruction stage
    intro_to = models.BooleanField(initial=False)
    instruct_one_to = models.BooleanField(initial=False)
    instruct_two_to = models.BooleanField(initial=False)
    instruct_three_to = models.BooleanField(initial=False)
    start_study_to = models.BooleanField(initial=False)

    # Agree to terms of participation at start.
    # accept_conditions = models.BooleanField(blank=False, widget=widgets.CheckboxInput)
    accept_conditions = models.BooleanField(blank=False)

    # Control questions for instructions (removed blank=False)
    Instr1 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr2 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)
    Instr3 = models.IntegerField(choices=[[1, 'True'], [2, 'False']], widget=widgets.RadioSelect)

    pay_this_round = models.BooleanField()
    round_result = models.CurrencyField()