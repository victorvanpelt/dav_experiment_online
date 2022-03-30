from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'dav_game_four'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    COST_REPORTS = [
        6000,
        5500,
        5000,
        4500,
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    cost_report = models.CurrencyField()

# FUNCTIONS
def set_payoffs(player: Player):
    player.cost_report = cu(C.COST_REPORTS[player.id_in_group - 1])
    player.payoff = cu(6000) - player.cost_report

# PAGES
class Start_study(Page):
    def before_next_page(player: Player, timeout_happened):
        set_payoffs(player)

class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_payoff': player.participant.payoff,
            'firm_profit': cu(6000) - player.cost_report,
            'total_eur': (player.participant.payoff).to_real_world_currency(
                player.session
            ),
        }


page_sequence = [Start_study, Results]
