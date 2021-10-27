from otree.api import Currency as cu, currency_range, SubmissionMustFail
from . import *
from otree.api import Bot
, Player
import itertools
import random

class PlayerBot(Bot):

    #light = random.randint(0, 1)

    def play_round(self):

        #some info for the round
        cost_realization = Constants.cost_realization[self.subsession.round_number - 1]

        # Assign types and condition
        light = random.randint(0,1)

        if self.subsession.round_number == 1:

            #Instructions
            yield Intro, dict(accept_conditions=True)
            yield SubmissionMustFail(Instruct_one, dict(Instr1=2))
            yield Instruct_one, dict(Instr1=1)
            yield SubmissionMustFail(Instruct_two, dict(Instr2=2))
            yield Instruct_two, dict(Instr2=1)
            yield SubmissionMustFail(Instruct_three, dict(Instr3=1))
            yield Instruct_three, dict(Instr3=2)
            yield SubmissionMustFail(Instruct_four, dict(Instr4=2))
            yield Instruct_four, dict(Instr4=1)
            yield SubmissionMustFail(Instruct_five, dict(Instr5=1))
            yield Instruct_five, dict(Instr5=2)

        yield Start_round

        if self.subsession.round_number == Constants.num_rounds:
            if self.player.id_in_group == 1:
                if light == 1:
                    yield Select_one, dict(select_one=0)
                else:
                    yield Select_one, dict(select_one=1)
            else:
                if light == 1:
                    yield Select_two, dict(select_two=0)
                else:
                    yield Select_two, dict(select_two=1)
        if self.group.communication == 1:
            if self.player.id_in_group == 1:
                if light == 1:
                    yield Recommendation_one, dict(recommendation_one=cost_realization, check_recommendation_one=1)
                else:
                    yield Recommendation_one, dict(recommendation_one=cu(400), check_recommendation_one=1)
            else:
                if light == 1:
                    yield Recommendation_two, dict(recommendation_two=cost_realization, check_recommendation_two=1)
                else:
                    yield Recommendation_two, dict(recommendation_two=cu(400), check_recommendation_two=1)
        if self.player.id_in_group == 1:
            if light == 1:
                if self.group.communication == 1 and self.group.recommendation_two == cu(400):
                    yield Report_one, dict(report_one=cu(400), check_report_one=1)
                elif self.group.communication == 1 and self.group.recommendation_two == cost_realization:
                    yield Report_one, dict(report_one=cost_realization, check_report_one=1)
                else:
                    yield Report_one, dict(report_one=cost_realization, check_report_one=1)
            else:
                yield Report_one, dict(report_one=cu(400), check_report_one=1)
        else:
            if light == 1:
                if self.group.communication == 1 and self.group.recommendation_one == cu(400):
                    yield Report_two, dict(report_two=cu(400), check_report_two=1)
                elif self.group.communication == 1 and self.group.recommendation_one == cost_realization:
                    yield Report_two, dict(report_two=cost_realization, check_report_two=1)
                else:
                    yield Report_two, dict(report_two=cost_realization, check_report_two=1)
            else:
                yield Report_two, dict(report_two=cu(400), check_report_two=1)
        if self.subsession.round_number == Constants.num_rounds:
            yield Results
