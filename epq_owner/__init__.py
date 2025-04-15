import itertools
import json
import random

from otree.api import *


author = 'Victor van Pelt'
doc = """
Ex-post Questionnaire
"""


class C(BaseConstants):
    NAME_IN_URL = 'epq_four'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    STANDARDCHOICESFIVE = [
        [1, 'Disagree strongly'],
        [2, 'Disagree'],
        [3, 'Neither agree nor disagree'],
        [4, 'Agree'],
        [5, 'Agree strongly'],
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    randomized_pages = models.StringField()
    task_rounds = models.StringField()

    #EPQ - Demographics
    gender = models.IntegerField(
        label="Please select your gender.",
        blank=False,
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
        ],
    )
    age = models.IntegerField(label="Please enter your age.", min=14, max=100, blank=False)
    education = models.IntegerField(
        label="What is the highest level of education that you have completed?",
        choices=[
            [1, 'Less than High school'],
            [2, 'High school'],
            [3, 'Vocational or trade school'],
            [4, '2-year College or University'],
            [5, '4-year College or University (BS, BA, or similar)'],
            [6, 'Postgraduate (MS, MA, PhD, MBA, or MD.)'],
        ],
    )
    english = models.IntegerField(
        label="Please rate your English on a percentage scale between 0 (not proficient) and 100 (proficient).",
        min=0,
        max=100,
        blank=False,
        initial=None,
    )
    corona = models.IntegerField(
        label="I am worried about the Corona virus (COVID2019).",
        blank=False,
        choices=C.STANDARDCHOICESFIVE,
    )
    risk = models.IntegerField(
        label="Please rate your willingness to take risks in general on a scale from 0 (not at all willing) to 10 (very willing)",
        min=0,
        step=1,
        max=10,
        blank=False,
        initial=None,
    )
    trustworthy = models.IntegerField(
        label="If someone does me a favor, I am ready to return it. Please rate how strongly this applies to you on a scale from 0 (does not apply to me at all) to 10 (applies to me completely)",
        min=0,
        step=1,
        max=10,
        blank=False,
        initial=None,
    )
    trusting = models.IntegerField(
        label="Generally speaking, would you say that most people can be trusted or that you can’t be too careful in dealing with people?",
        blank=False,
        choices=[[0, 'Most people can be trusted'], [1, 'One can`t be too careful']],
    )

class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'gender',
        'age',
        'trusting',
        'trustworthy',
        'risk',
        'education',
        'english',
        'corona',
    ]

    @staticmethod
    def get_form_fields(player: Player):
        fields = [
            'gender',
            'age',
            'trusting',
            'trustworthy',
            'risk',
            'education',
            'english',
            'corona',
        ]
        random.shuffle(fields)
        return fields

page_sequence = [Demographics]
