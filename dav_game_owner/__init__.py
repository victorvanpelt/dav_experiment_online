from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'dav_game_four'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    COST_REPORTS = [
        5304,
        4488,
        6000,
        6000,
        5005,
        4686,
        5600,
        5996,
        4855,
        5353,
        4569,
        5572,
        4266,
        5844,
        4873,
        5977,
        5845,
        5683,
        5358,
        4096,
        6000,
        5499,
        6000,
        5161,
        5599,
        5224,
        4916,
        5286,
        4474,
        4603,
        4299,
        5468,
        5875,
        4825,
        5379,
        5580,
        5458,
        5000,
        5003,
        6000,
        5815,
        4017,
        5951,
        6000,
        5051,
        5244,
        5492,
        5800,
        5844,
        6000,
        5478,
        5600,
        6000,
        6000,
        4489,
        5490,
        5765,
        5500,
        5651,
        5581,
        5994,
        5503,
        5501,
        5505,
        4646,
        5587,
        5466,
        6000,
        6000,
        5600,
        5900,
        5017,
        4017,
        5804,
        5918,
        5822,
        4070,
        5501,
        5707,
        5263,
        5925,
        6000,
        5963,
        5604,
        5530,
        5664,
        5100,
        5116,
        4671,
        4891,
        5344,
        4918,
        4754,
        5438,
        6000,
        5338,
        4758,
        4603,
        5624,
        6000,
        5377,
        6000,
        5297,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
        6000,
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
