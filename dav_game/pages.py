from otree.api import Currency as c, currency_range
from otree.models import subsession

from ._builtin import Page, WaitPage
from .models import Constants, Player
import random

class WaitForMatch(WaitPage):
    group_by_arrival_time = True
    after_all_players_arrive = "assign_stuff"
    title_text = "Please wait"
    body_text = "Please wait to be matched to another participant."

class Intro(Page):
    timeout_seconds = 100

    form_model = 'player'
    form_fields = ['accept_conditions']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.player.intro_to = True

class Instruct_one(Page):
    form_model = 'player'
    form_fields = ['Instr1']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 100

    def error_message(self, value):
        if value["Instr1"] != 2:
            return 'Your answer is incorrect. The team’s cost report must not exceed 6000 Lira, nor can it be lower than the actual project costs. Please try again.'

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.player.instruct_one_to = True

class Instruct_two(Page):
    form_model = 'player'
    form_fields = ['Instr2']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 100

    def error_message(self, value):
        if value["Instr2"] != 2:
            return "Your answer is incorrect. Either your or the other participant's cost report will be submitted as the team's cost report. Please try again."

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.player.instruct_two_to = True

class Instruct_three(Page):
    form_model = 'player'
    form_fields = ['Instr3']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 100

    def error_message(self, value):
        if value["Instr3"] != 1:
            return 'Your answer is incorrect. The team’s cost report affects how many Lira the other participant and you earn. Please try again.'

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.player.instruct_three_to = True

class Start_study(Page):
    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.player.start_study_to = True

class Select_one(Page):
    form_model = 'group'
    form_fields = ['select_one']

    def is_displayed(self):
        if self.group.self_selection == 1:
            return self.player.id_in_group == 1

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.group.select_one_to = True
            self.group.select_one = 0

class Select_two(Page):
    form_model = 'group'
    form_fields = ['select_two']

    def is_displayed(self):
        if self.group.self_selection == 1:
            return self.player.id_in_group == 2

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.group.select_two_to = True
            self.group.select_two = 0

class WaitForSelection(WaitPage):
    def is_displayed(self):
        return self.group.self_selection == 1

class Recommendation_one(Page):
    form_model = 'group'
    form_fields = ['recommendation_one', 'check_recommendation_one']

    def is_displayed(self):
        if self.group.communication == 1:
            return self.player.id_in_group == 1
        else:
            return False

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 60

    def vars_for_template(self):
        return {
            'cost_realization': self.group.cost_realization
        }

    def error_message(self, value):
        if value["check_recommendation_one"] == None:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.group.recommendation_one_to = True
            self.group.recommendation_one = c(0)

class Recommendation_two(Page):
    form_model = 'group'
    form_fields = ['recommendation_two', 'check_recommendation_two']

    def is_displayed(self):
        if self.group.communication == 1:
            return self.player.id_in_group == 2
        else:
            return False

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 60

    def vars_for_template(self):
        return {
            'cost_realization': self.group.cost_realization
        }

    def error_message(self, value):
        if value["check_recommendation_two"] == None:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.group.recommendation_two_to = True
            self.group.recommendation_two = c(0)

class WaitForRecommendation(WaitPage):
    def is_displayed(self):
        return self.group.communication == 1

class Report_one(Page):
    form_model = 'group'
    form_fields = ['report_one', 'check_report_one']

    def vars_for_template(self):
        return {
            'cost_realization': self.group.cost_realization
        }

    def is_displayed(self):
        return self.player.id_in_group == 1

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 60

    def error_message(self, value):
        if value["check_report_one"] == None:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.group.report_one_to = True
            if self.group.report_one == c(0):
                self.group.report_one = self.group.cost_realization

class Report_two(Page):
    form_model = 'group'
    form_fields = ['report_two', 'check_report_two']

    def vars_for_template(self):
        return {
            'cost_realization': self.group.cost_realization
        }

    def is_displayed(self):
        return self.player.id_in_group == 2

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 60

    def error_message(self, value):
        if value["check_report_two"] == None:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        if self.timeout_happened:
            self.group.report_two_to = True
            self.participant.vars['is_dropout'] = True
            if self.group.report_two == c(0):
                self.group.report_two = self.group.cost_realization

class WaitForResults(WaitPage):
    after_all_players_arrive = 'set_report_payoffs'

class Results(Page):
    # def is_displayed(self):
    #     return self.subsession.round_number == Constants.num_rounds

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1
        else:
            return 100

    def vars_for_template(self):
        return {
            # 'round_to_pay': self.participant.vars['round_to_pay'],
            'payoff': self.participant.payoff
        }

page_sequence = [
    WaitForMatch,
    Intro,
    Instruct_one,
    Instruct_two,
    Instruct_three,
    Start_study,
    Select_one,
    Select_two,
    WaitForSelection,
    Recommendation_one,
    Recommendation_two,
    WaitForRecommendation,
    Report_one,
    Report_two,
    WaitForResults,
    Results
]
