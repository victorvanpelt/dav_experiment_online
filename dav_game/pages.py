from otree.api import Currency as cu, currency_range
from otree.models import subsession

from ._builtin import Page, WaitPage
from .models import Constants, Player
import random

class WaitForMatch(WaitPage):
    group_by_arrival_time = True
    after_all_players_arrive = "assign_stuff"
    title_text = "Please wait"
    body_text = "Please wait for the other participant."

    def app_after_this_page(self, upcoming_apps):
        if len(self.group.get_players()) == 1:
            self.group.drop_out_trigger()
            return upcoming_apps[-1]

class Start_study(Page):
    def is_displayed(self):
        return self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

    def get_timeout_seconds(self):
        return 60

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
        return self.group.self_selection == 1 and self.player.id_in_group == 1 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

    def get_timeout_seconds(self):
        return 90

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_one()

class Select_two(Page):
    form_model = 'group'
    form_fields = ['select_two']

    def is_displayed(self):
        return self.group.self_selection == 1 and self.player.id_in_group == 2 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

    def get_timeout_seconds(self):
        return 90

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_two()

class WaitForSelection(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."
    def is_displayed(self):
        return self.group.self_selection == 1 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

class Recommendation_one(Page):
    form_model = 'group'
    form_fields = ['recommendation_one', 'check_recommendation_one']

    def is_displayed(self):
        return self.group.communication == 1 and self.player.id_in_group == 1 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

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
        return self.group.communication == 1 and self.player.id_in_group == 2 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

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
        return self.group.communication == 1 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

class Chat_one(Page):
    form_model = 'group'
    form_fields = ['confirm_chat_one']

    def is_displayed(self):
        return self.group.communication == 1 and self.player.id_in_group == 1 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

    def get_timeout_seconds(self):
        return 120

    # def error_message(self, value):
    #     if value["confirm_chat_one"] == 0:
    #         return 'Please confirm that you finished chatting.'

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_one()

class Chat_two(Page):
    form_model = 'group'
    form_fields = ['confirm_chat_two']

    def is_displayed(self):
        return self.group.communication == 1 and self.player.id_in_group == 2 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

    def get_timeout_seconds(self):
        return 120

    # def error_message(self, value):
    #     if value["confirm_chat_two"] == 0:
    #         return 'Please confirm that you finished chatting.'

    def before_next_page(self):
        if self.timeout_happened:
            self.group.drop_out_trigger_two()

class WaitForChat(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."
    def is_displayed(self):
        return self.group.communication == 1 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False


class Report_one(Page):
    form_model = 'group'
    form_fields = ['report_one', 'check_report_one']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

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
        return self.player.id_in_group == 2 and self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

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
        return self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

class Results(Page):
    def is_displayed(self):
        return self.player.participant.is_dropout == False and self.player.participant.is_dropout_mate == False

    def vars_for_template(self):
        return {
            'total_payoff': self.player.participant.payoff + cu(500),
            'firm_profit': cu(6000) - self.group.group_report,
            'total_eur': (self.player.participant.payoff + cu(500)).to_real_world_currency(self.player.session),
        }

page_sequence = [
    WaitForMatch,
    Start_study,
    Select_one,
    Select_two,
    WaitForSelection,
    Recommendation_one,
    Recommendation_two,
    WaitForRecommendation,
    Chat_one,
    Chat_two,
    WaitForChat,
    Report_one,
    Report_two,
    WaitForResults,
    Results
]
