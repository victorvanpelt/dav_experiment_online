import itertools
import random
import time

from otree.api import *
from otree.models import subsession


author = 'Victor'
doc = """
DAV Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'dav_game'
    players_per_group = 2
    num_rounds = 1
    # Maximum cost realization and report
    max_cost = cu(6000)
    # Pre-drawn cost realizations for each group
    cost_realization = [
        4488,
        4090,
        4096,
        5081,
        4115,
        4017,
        5161,
        5393,
        4087,
        4070,
        4306,
        4123,
        4603,
        4041,
        5844,
        4671,
        5647,
        4262,
        5297,
        4939,
        5073,
        4529,
        4422,
        5124,
        4133,
        5364,
        5248,
        4723,
        5121,
        4288,
        5771,
        5790,
        4113,
        5335,
        5550,
        5909,
        4642,
        5825,
        4889,
        4327,
        4365,
        5948,
        5733,
        4088,
        5415,
        5677,
        5662,
        5280,
        4429,
        4119,
        5888,
        4830,
        5741,
        4215,
        5050,
        5953,
        5554,
        5007,
        4247,
        4432,
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    cost_realization = models.CurrencyField()
    communication = models.IntegerField()
    self_selection = models.IntegerField()
    confirm_chat_one = models.IntegerField(blank=False, initial=0, min=0, max=1)
    confirm_chat_two = models.IntegerField(blank=False, initial=0, min=0, max=1)
    check_recommendation_one = models.IntegerField(initial=None, blank=True)
    recommendation_one = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)
    check_recommendation_two = models.IntegerField(initial=None, blank=True)
    recommendation_two = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)
    select_one = models.BooleanField(initial=False, blank=True)
    select_two = models.BooleanField(initial=False, blank=True)
    check_report_one = models.IntegerField(initial=None, blank=True)
    report_one = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)
    check_report_two = models.IntegerField(initial=None, blank=True)
    report_two = models.CurrencyField(initial=None, blank=False, max=Constants.max_cost)
    group_report = models.CurrencyField(initial=None, blank=False)
    # Which report will be selected?
    select_report_one = models.IntegerField()
    select_report_two = models.IntegerField()
    payoff_one = models.CurrencyField(blank=True, initial=None)
    payoff_two = models.CurrencyField(blank=True, initial=None)
    group_profit = models.CurrencyField(blank=True, initial=None)
    role_random_last = models.IntegerField(Initial=0)


class Player(BasePlayer):
    # Dropout indicator
    drop_out = models.BooleanField(initial=False)
    drop_out_mate = models.BooleanField(initial=False)
    dofus = models.BooleanField(initial=False)
    confirm_chat = models.IntegerField(blank=False, initial=0, min=0, max=1)

# FUNCTIONS
def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    if len(waiting_players) >= 2:
        return waiting_players[:2]
    for player in waiting_players:
        if waiting_too_long(player):
            # make a single-player group.
            return [player]


def assign_stuff(group: Group):
    # Assign cost realization and base dropout variables
    group.cost_realization = cu(Constants.cost_realization[group.id_in_subsession - 2])
    # Load dropout variables
    for p in group.get_players():
        p.drop_out = p.participant.is_dropout
        p.drop_out_mate = p.participant.is_dropout_mate
        p.dofus = p.participant.is_dofus
        # Load conditions based on session config else randomize per dyad
        if p.participant.communication == 1:
            group.communication = 1
        elif p.participant.communication == 0:
            group.communication = 0
        if p.participant.self_selection == 1:
            group.self_selection = 1
        elif p.participant.self_selection == 0:
            group.self_selection = 0


# This method triggers when a participant drop out due to time-out
def drop_out_trigger(group: Group):
    for p in group.get_players():
        p.participant.is_dropout = True
        p.drop_out = True
        #p.payoff = -cu(500)


def drop_out_trigger_one(group: Group):
    for p in group.get_players():
        if p.id_in_group == 1:
            p.participant.is_dropout = True
            p.drop_out = True
            #p.payoff = -cu(500)
            p.payoff = cu(0)
        elif p.id_in_group == 2:
            p.participant.is_dropout_mate = True
            p.drop_out_mate = True
            if p.participant.is_dropout == False:
                #p.payoff = cu(0)
                p.payoff = cu(500)


def drop_out_trigger_two(group: Group):
    for p in group.get_players():
        if p.id_in_group == 2:
            p.participant.is_dropout = True
            p.drop_out = True
            #p.payoff = -cu(500)
            p.payoff = cu(0)
        elif p.id_in_group == 1:
            p.participant.is_dropout_mate = True
            p.drop_out_mate = True
            if p.participant.is_dropout == False:
                #p.payoff = cu(0)
                p.payoff = cu(500)


def recommendation_one_min(group: Group):
    return group.cost_realization


def recommendation_two_min(group: Group):
    return group.cost_realization


def report_one_min(group: Group):
    return group.cost_realization


def report_two_min(group: Group):
    return group.cost_realization


def set_report_payoffs(group: Group):
    if group.self_selection == 1:
        if group.select_one == 1 and group.select_two == 0:
            group.group_report = group.report_one
            group.select_report_one = 1
            group.select_report_two = 0
        elif group.select_one == 0 and group.select_two == 1:
            group.group_report = group.report_two
            group.select_report_one = 0
            group.select_report_two = 1
        else:
            role_random_last = random.randint(1, 2)
            group.role_random_last = role_random_last
            if role_random_last == 1:
                group.group_report = group.report_one
                group.select_report_one = 1
                group.select_report_two = 0
            elif role_random_last == 2:
                group.group_report = group.report_two
                group.select_report_one = 0
                group.select_report_two = 1
    else:
        role_random = random.randint(1, 2)
        if role_random == 1:
            group.group_report = group.report_one
            group.select_report_one = 1
            group.select_report_two = 0
        else:
            group.group_report = group.report_two
            group.select_report_one = 0
            group.select_report_two = 1
    group.group_profit = group.group_report - group.cost_realization
    group.payoff_one = group.group_profit / 2
    group.payoff_two = group.group_profit / 2
    for p in group.get_players():
        if p.id_in_group == 1:
            p.payoff = group.payoff_one + cu(500)
        elif p.id_in_group == 2:
            p.payoff = group.payoff_two + cu(500)


# def dofus_trigger(self):
#     for p in self.get_players():
#         if p.dofus == 1:
#             p.payoff = cu(0)
def waiting_too_long(player: Player):
    # import time
    # assumes you set wait_page_arrival in PARTICIPANT_FIELDS.
    return (time.time() - player.participant.wait_page_arrival) > 5 * 60


# PAGES
class WaitForMatch(WaitPage):
    group_by_arrival_time = True
    after_all_players_arrive = "assign_stuff"
    title_text = "Please wait"
    body_text = "Please wait for the other participant."

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        if len(player.group.get_players()) == 1:
            drop_out_trigger(player.group)
            return upcoming_apps[-1]


class Start_study(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (
            player.participant.is_dropout == False and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 60

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            if player.id_in_group == 1:
                drop_out_trigger_one(player.group)
            elif player.id_in_group == 2:
                drop_out_trigger_two(player.group)


class Select_one(Page):
    form_model = 'group'
    form_fields = ['select_one']

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.group.self_selection == 1
            and player.id_in_group == 1
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 90

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            drop_out_trigger_one(player.group)


class Select_two(Page):
    form_model = 'group'
    form_fields = ['select_two']

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.group.self_selection == 1
            and player.id_in_group == 2
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 90

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            drop_out_trigger_two(player.group)


class WaitForSelection(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.group.self_selection == 1
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )


class Recommendation_one(Page):
    form_model = 'group'
    form_fields = ['recommendation_one', 'check_recommendation_one']

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.group.communication == 1
            and player.id_in_group == 1
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 90

    @staticmethod
    def error_message(player: Player, value):
        if value["check_recommendation_one"] == None:
            return 'Please use the slider to make a decision.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            drop_out_trigger_one(player.group)


class Recommendation_two(Page):
    form_model = 'group'
    form_fields = ['recommendation_two', 'check_recommendation_two']

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.group.communication == 1
            and player.id_in_group == 2
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 90

    @staticmethod
    def error_message(player: Player, value):
        if value["check_recommendation_two"] == None:
            return 'Please use the slider to make a decision.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            drop_out_trigger_two(player.group)


class WaitForRecommendation(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.group.communication == 1
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

class Chat(Page):
    form_model = 'player'
    form_fields = ['confirm_chat']

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.group.communication == 1
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 120

    @staticmethod
    def live_method(player: Player, data):
        if data['type'] == 'leaving':
            return {0: dict(type='leaving', id_in_group=player.id_in_group)}

    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    # @staticmethod
    # def before_next_page(player: Player, timeout_happened):
    #     if timeout_happened:
    #         if player.id_in_group == 1:
    #             drop_out_trigger_one(player.group)
    #         elif player.id_in_group == 2:
    #             drop_out_trigger_two(player.group)

class WaitForChat(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.group.communication == 1
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )


class Report_one(Page):
    form_model = 'group'
    form_fields = ['report_one', 'check_report_one']

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.id_in_group == 1
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 90

    @staticmethod
    def error_message(player: Player, value):
        if value["check_report_one"] == None:
            return 'Please use the slider to make a decision.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            drop_out_trigger_one(player.group)


class Report_two(Page):
    form_model = 'group'
    form_fields = ['report_two', 'check_report_two']

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.id_in_group == 2
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def get_timeout_seconds(player: Player):
        return 90

    @staticmethod
    def error_message(player: Player, value):
        if value["check_report_two"] == None:
            return 'Please use the slider to make a decision.'

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            drop_out_trigger_two(player.group)


class WaitForResults(WaitPage):
    title_text = "Please wait"
    body_text = "Please wait for the other participant."
    after_all_players_arrive = 'set_report_payoffs'

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.participant.is_dropout == False and player.participant.is_dropout_mate == False
        )


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return (
            player.participant.is_dropout == False and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_payoff': player.participant.payoff,
            'firm_profit': cu(6000) - player.group.group_report,
            'total_eur': (player.participant.payoff).to_real_world_currency(
                player.session
            ),
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
    # Chat_one,
    # Chat_two,
    Chat,
    WaitForChat,
    Report_one,
    Report_two,
    WaitForResults,
    Results,
]
