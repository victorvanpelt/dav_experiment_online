from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instruct_one(Page):
    form_model = 'player'
    form_fields = ['Instr1']

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.player.Instr1 != 2 or self.timeout_happened:
            self.player.participant.is_dofus = True
            self.player.dofus = True
            self.player.dofus_trigger()
        # if self.timeout_happened:
        #     self.player.drop_out = True
        #     self.player.participant.is_dropout = True

    def app_after_this_page(self, upcoming_apps):
        if self.player.Instr1 != 2 or self.timeout_happened:
            return upcoming_apps[-1]

class Instruct_two(Page):
    form_model = 'player'
    form_fields = ['Instr2']

    # def is_displayed(self):
    #     return self.player.participant.is_dofus == False

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.player.Instr2 != 1 or self.timeout_happened:
            self.player.participant.is_dofus = True
            self.player.dofus = True
            self.player.dofus_trigger()
        # if self.timeout_happened:
        #     self.player.drop_out = True
        #     self.player.participant.is_dropout = True

    def app_after_this_page(self, upcoming_apps):
        if self.player.Instr2 != 1 or self.timeout_happened:
            return upcoming_apps[-1]

class Instruct_three(Page):
    form_model = 'player'
    form_fields = ['Instr3']

    # def is_displayed(self):
    #     return self.player.participant.is_dofus == False

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.player.Instr3 != 1 or self.timeout_happened:
            self.player.participant.is_dofus = True
            self.player.dofus = True
            self.player.dofus_trigger()
        # if self.timeout_happened:
        #     self.player.drop_out = True
        #     self.player.participant.is_dropout = True

    def app_after_this_page(self, upcoming_apps):
        if self.player.Instr3 != 1 or self.timeout_happened:
            return upcoming_apps[-1]

class Instruct_four(Page):
    form_model = 'player'
    form_fields = ['Instr4']

    # def is_displayed(self):
    #     return self.player.participant.is_dofus == False

    def get_timeout_seconds(self):
        return 120

    def before_next_page(self):
        if self.player.Instr4 != 1 or self.timeout_happened:
            self.player.participant.is_dofus = True
            self.player.dofus = True
            self.player.dofus_trigger()
        # if self.timeout_happened:
        #     self.player.drop_out = True
        #     self.player.participant.is_dropout = True

    def app_after_this_page(self, upcoming_apps):
        if self.player.Instr4 != 1 or self.timeout_happened:
            return upcoming_apps[-1]

page_sequence = [
    Instruct_one,
    Instruct_two,
    Instruct_three,
    Instruct_four,
    ]