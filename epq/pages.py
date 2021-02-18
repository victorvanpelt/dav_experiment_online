from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
import random

class Introduction(Page):
    def progress(self):
        curpageindex = self.round_number-1
        progress = curpageindex / tot_pages * 100
        return progress

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['A'] and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

class Checks(Page):
    form_model = 'player'
    form_fields = [
        'recommendation_check',
        'self_select_check',
        'concerned_about_honest',
        'attractive_dishonesty'

    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

    def progress(self):
        curpageindex = self.round_number-1
        progress = curpageindex / tot_pages * 100
        return progress

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['B'] and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def vars_for_template(self):
        progress = self.progress()
        return {
            'progress': progress
        }

class Page_2(Page):
    form_model = 'player'
    form_fields = [
        'mach1',
        'mach2',
        'mach3',
        'mach4',
        'mach5',
        'mach6',
        'mach7',
        'mach8',
        'mach9'
    ]

    def progress(self):
        curpageindex = self.round_number-1
        progress = curpageindex / tot_pages * 100
        return progress

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['C'] and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def vars_for_template(self):
        progress = self.progress()
        return {
            'progress': progress
        }

class Page_3(Page):
    form_model = 'player'
    form_fields = [
        'narc1',
        'narc2',
        'narc3',
        'narc4',
        'narc5',
        'narc6',
        'narc7',
        'narc8',
        'narc9'
    ]

    def progress(self):
        curpageindex = self.round_number-1
        progress = curpageindex / tot_pages * 100
        return progress

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['D'] and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def vars_for_template(self):
        progress = self.progress()
        return {
            'progress': progress
        }

class Page_4(Page):
    form_model = 'player'
    form_fields = [
        'psy1',
        'psy2',
        'psy3',
        'psy4',
        'psy5',
        'psy6',
        'psy7',
        'psy8',
        'psy9'
    ]

    def progress(self):
        curpageindex = self.round_number-1
        progress = curpageindex / tot_pages * 100
        return progress

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['E'] and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def vars_for_template(self):
        progress = self.progress()
        return {
            'progress': progress
        }

class Page_5(Page):
    form_model = 'player'
    form_fields = [
        'faith1',
        'faith2',
        'faith3',
        'faith4',
        'human1',
        'human2',
        'human3',
        'human4',
        'kant1',
        'kant2',
        'kant3',
        'kant4'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

    def progress(self):
        curpageindex = self.round_number-1
        progress = curpageindex / tot_pages * 100
        return progress

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['F'] and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def vars_for_template(self):
        progress = self.progress()
        return {
            'progress': progress
        }

class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'age',
        'trust',
        'education',
        'english',
        'corona'
    ]

    def get_form_fields(self):
        fields = self.form_fields
        random.shuffle(fields)
        return fields

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['G'] and self.participant.vars['is_dropout'] == False and self.participant.vars['is_dropout_mate'] == False

    def progress(self):
        curpageindex = self.round_number-1
        progress = curpageindex / tot_pages * 100
        return progress

    def vars_for_template(self):
        progress = self.progress()
        return {
            'progress': progress
        }

page_sequence = [
    Introduction,
    Checks,
    Page_2,
    Page_3,
    Page_4,
    Page_5,
    Demographics
]

tot_pages = len(page_sequence)
