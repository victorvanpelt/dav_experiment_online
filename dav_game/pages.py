from otree.api import Currency as c, currency_range
from otree.models import subsession

from ._builtin import Page, WaitPage
from .models import Constants, Player
import random

class WaitForMatch(WaitPage):
    group_by_arrival_time = True
    after_all_players_arrive = "assign_stuff"
    title_text = "Please wait"
    body_text = "Please wait for the other participant."

class Intro(Page):
    timeout_seconds = 120

    form_model = 'player'
    form_fields = ['accept_conditions']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def before_next_page(self):
        if self.timeout_happened:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()

class Instruct_one(Page):
    form_model = 'player'
    form_fields = ['Instr1']

    def is_displayed(self):
        return self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.timeout_happened:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()
        if self.player.Instr1 != 1:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()

class Instruct_two(Page):
    form_model = 'player'
    form_fields = ['Instr2']

    def is_displayed(self):
        return self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.timeout_happened:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()
        if self.player.Instr2 != 1:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()

class Instruct_three(Page):
    form_model = 'player'
    form_fields = ['Instr3']

    def is_displayed(self):
        return self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.timeout_happened:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()
        if self.player.Instr3 != 2:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()

class Instruct_four(Page):
    form_model = 'player'
    form_fields = ['Instr4']

    def is_displayed(self):
        return self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.timeout_happened:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()
        if self.player.Instr4 != 1:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()

class Start_study(Page):
    def is_displayed(self):
        return self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.timeout_happened:
            if self.player.id_in_group == 1:
                self.group.drop_out_trigger_one()
            elif self.player.id_in_group == 2:
                self.group.drop_out_trigger_two()

class Select_one(Page):
    form_model = 'group'
    form_fields = ['select_one']

    def is_displayed(self):
        return self.group.self_selection == 1 and self.player.id_in_group == 1 and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 90

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_one()

class Select_two(Page):
    form_model = 'group'
    form_fields = ['select_two']

    def is_displayed(self):
        return self.group.self_selection == 1 and self.player.id_in_group == 2 and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 90

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_two()

class WaitForSelection(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."
    def is_displayed(self):
        return self.group.self_selection == 1 and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

class Recommendation_one(Page):
    form_model = 'group'
    form_fields = ['recommendation_one', 'check_recommendation_one']

    def is_displayed(self):
        return self.group.communication == 1 and self.player.id_in_group == 1 and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 90

    def error_message(self, value):
        if value["check_recommendation_one"] == None:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_one()

class Recommendation_two(Page):
    form_model = 'group'
    form_fields = ['recommendation_two', 'check_recommendation_two']

    def is_displayed(self):
        return self.group.communication == 1 and self.player.id_in_group == 2 and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 90

    def error_message(self, value):
        if value["check_recommendation_two"] == None:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_two()

class WaitForRecommendation(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."
    def is_displayed(self):
        return self.group.communication == 1 and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

class Report_one(Page):
    form_model = 'group'
    form_fields = ['report_one', 'check_report_one']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 90

    def error_message(self, value):
        if value["check_report_one"] == None:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_one()

class Report_two(Page):
    form_model = 'group'
    form_fields = ['report_two', 'check_report_two']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def get_timeout_seconds(self):
        return 90

    def error_message(self, value):
        if value["check_report_two"] == None:
            return 'Please use the slider to make a decision.'

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_two()

class WaitForResults(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."
    after_all_players_arrive = 'set_report_payoffs'

    def is_displayed(self):
        return self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

class Results(Page):
    def is_displayed(self):
        return self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def vars_for_template(self):
        return {
            'payoff': self.participant.payoff
        }

page_sequence = [
    WaitForMatch,
    Intro,
    Instruct_one,
    Instruct_two,
    Instruct_three,
    Instruct_four,
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
