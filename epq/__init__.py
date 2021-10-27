import itertools
import json
import random

from otree.api import *


author = 'Victor van Pelt'
doc = """
Ex-post Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'epq'
    players_per_group = None
    tasks = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    num_rounds = len(tasks)
    StandardChoicesFive = [
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
    # EPQ 1 - Randomization, understandability, and motivation
    # serious = models.IntegerField(
    #     label="I participated seriously in the study.",
    #     choices=Constants.StandardChoicesFive
    # )
    # lose_interest = models.IntegerField(
    #     label="I started to lose my interest as the study progressed.",
    #     choices=Constants.StandardChoicesFive
    # )
    # cared = models.IntegerField(
    #     label="I cared about the outcomes of my decisions.",
    #     choices=Constants.StandardChoicesFive
    # )
    recommendation_check = models.IntegerField(
        label="Before I submitted the cost report that I wanted my team to submit, I received a cost report recommendation from the other participant.",
        choices=[
            [0, 'False'],
            [1, 'True'],
        ],
    )
    self_select_check = models.IntegerField(
        label="I could choose whether I wanted to become my team’s manager.",
        choices=[
            [0, 'False'],
            [1, 'True'],
        ],
    )
    concerned_about_honest = models.IntegerField(
        label="I was concerned about reporting about our team’s project cost honestly to corporate headquarters.",
        choices=Constants.StandardChoicesFive,
    )
    attractive_dishonesty = models.IntegerField(
        label="It was attractive to report a project cost above the actual project cost.",
        choices=Constants.StandardChoicesFive,
    )
    # EPQ 2 - Mach
    mach1 = models.IntegerField(
        label="It’s not wise to tell your secrets.", choices=Constants.StandardChoicesFive
    )
    mach2 = models.IntegerField(
        label="I like to use clever manipulation to get my way.",
        choices=Constants.StandardChoicesFive,
    )
    mach3 = models.IntegerField(
        label="Whatever it takes, you must get the important people on your side.",
        choices=Constants.StandardChoicesFive,
    )
    mach4 = models.IntegerField(
        label="Avoid direct conflict with others because they may be useful in the future.",
        choices=Constants.StandardChoicesFive,
    )
    mach5 = models.IntegerField(
        label="It's wise to keep track of information that you can use against people later.",
        choices=Constants.StandardChoicesFive,
    )
    mach6 = models.IntegerField(
        label="You should wait for the right time to get back at people.",
        choices=Constants.StandardChoicesFive,
    )
    mach7 = models.IntegerField(
        label="There are things you should hide from other people to preserve your reputation.",
        choices=Constants.StandardChoicesFive,
    )
    mach8 = models.IntegerField(
        label="Make sure your plans benefit yourself, not others.",
        choices=Constants.StandardChoicesFive,
    )
    mach9 = models.IntegerField(
        label="Most people can be manipulated.", choices=Constants.StandardChoicesFive
    )
    # EPQ 3 - Narc
    narc1 = models.IntegerField(
        label="People see me as a natural leader.", choices=Constants.StandardChoicesFive
    )
    narc2 = models.IntegerField(
        label="I hate being the center of attention.", choices=Constants.StandardChoicesFive
    )
    narc3 = models.IntegerField(
        label="Many group activities tend to be dull without me.",
        choices=Constants.StandardChoicesFive,
    )
    narc4 = models.IntegerField(
        label="I know that I am special because everyone keeps telling me so.",
        choices=Constants.StandardChoicesFive,
    )
    narc5 = models.IntegerField(
        label="I like to get acquainted with important people.",
        choices=Constants.StandardChoicesFive,
    )
    narc6 = models.IntegerField(
        label="I feel embarrassed if someone compliments me.", choices=Constants.StandardChoicesFive
    )
    narc7 = models.IntegerField(
        label="I have been compared to famous people.", choices=Constants.StandardChoicesFive
    )
    narc8 = models.IntegerField(
        label="I am an average person.", choices=Constants.StandardChoicesFive
    )
    narc9 = models.IntegerField(
        label="I insist on getting the respect I deserve.", choices=Constants.StandardChoicesFive
    )
    # EPQ 4 - Psy
    psy1 = models.IntegerField(
        label="I like to get revenge on authorities.", choices=Constants.StandardChoicesFive
    )
    psy2 = models.IntegerField(
        label="I avoid dangerous situations.", choices=Constants.StandardChoicesFive
    )
    psy3 = models.IntegerField(
        label="Payback needs to be quick and nasty.", choices=Constants.StandardChoicesFive
    )
    psy4 = models.IntegerField(
        label="People often say I’m out of control.", choices=Constants.StandardChoicesFive
    )
    psy5 = models.IntegerField(
        label="It’s true that I can be mean to others.", choices=Constants.StandardChoicesFive
    )
    psy6 = models.IntegerField(
        label="People who mess with me always regret it.", choices=Constants.StandardChoicesFive
    )
    psy7 = models.IntegerField(
        label="I have never gotten into trouble with the law.",
        choices=Constants.StandardChoicesFive,
    )
    psy8 = models.IntegerField(
        label="I enjoy having sex with people I hardly know.", choices=Constants.StandardChoicesFive
    )
    psy9 = models.IntegerField(
        label="I’ll say anything to get what I want.", choices=Constants.StandardChoicesFive
    )
    # EPQ 5 - Light Triad
    faith1 = models.IntegerField(
        label="I tend to see the best in people.", choices=Constants.StandardChoicesFive
    )
    faith2 = models.IntegerField(
        label="I tend to trust that other people will deal fairly with me.",
        choices=Constants.StandardChoicesFive,
    )
    faith3 = models.IntegerField(
        label="I think people are mostly good.", choices=Constants.StandardChoicesFive
    )
    faith4 = models.IntegerField(
        label="I am quick to forgive people who have hurt me.",
        choices=Constants.StandardChoicesFive,
    )
    human1 = models.IntegerField(
        label="I tend to admire others.", choices=Constants.StandardChoicesFive
    )
    human2 = models.IntegerField(
        label="I tend to applaud the successes of other people.",
        choices=Constants.StandardChoicesFive,
    )
    human3 = models.IntegerField(
        label="I tend to treat others as valuable.", choices=Constants.StandardChoicesFive
    )
    human4 = models.IntegerField(
        label="I enjoy listening to people from all walks of life.",
        choices=Constants.StandardChoicesFive,
    )
    kant1 = models.IntegerField(
        label="I prefer honesty over charm.", choices=Constants.StandardChoicesFive
    )
    kant2 = models.IntegerField(
        label="I don't feel comfortable overtly manipulating people to do something I want.",
        choices=Constants.StandardChoicesFive,
    )
    kant3 = models.IntegerField(
        label="I would like to be authentic even if it may damage my reputation.",
        choices=Constants.StandardChoicesFive,
    )
    kant4 = models.IntegerField(
        label="When I talk to people, I am rarely thinking about what I want from them.",
        choices=Constants.StandardChoicesFive,
    )
    # # EPQ 6 - Big 5 Short
    # big1 = models.IntegerField(
    #     label="I see myself as extraverted, enthusiastic.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big2 = models.IntegerField(
    #     label="I see myself as critical, quarrelsome.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big3 = models.IntegerField(
    #     label="I see myself as dependable, self-disciplined.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big4 = models.IntegerField(
    #     label="I see myself as anxious, easily upset.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big5 = models.IntegerField(
    #     label="I see myself as open to new experiences, complex.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big6 = models.IntegerField(
    #     label="I see myself as reserved, quiet.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big7 = models.IntegerField(
    #     label="I see myself as sympathetic, warm.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big8 = models.IntegerField(
    #     label="I see myself as disorganized, careless.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big9 = models.IntegerField(
    #     label="I see myself as calm, emotionally stable.",
    #     choices=Constants.StandardChoicesFive
    # )
    # big10 = models.IntegerField(
    #     label="I see myself as conventional, uncreative.",
    #     choices=Constants.StandardChoicesFive
    # )
    # EPQ 6 - Demographics
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
    # trust = models.IntegerField(
    #     label="Generally speaking, would you say that most people can be trusted or that you can’t be too careful in dealing with people?",
    #     blank=False,
    #     choices=[
    #         [1, 'Most people can be trusted'],
    #         [0, "One can't be too careful"]
    #     ]
    # )
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
        choices=Constants.StandardChoicesFive,
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


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            dark_position = random.randint(1, 2)
            if dark_position == 1:
                # [3, 4, 5] + [6]
                random_numbers = [3, 4, 5, 6]
            else:
                # [4, 5, 6] + [3]
                random_numbers = [4, 5, 6, 3]
            p.randomized_pages = json.dumps(random_numbers)
            # Add everything to complete round_numbers list
            round_numbers = [1, 2, Constants.num_rounds]  # Actual order of tasks
            round_numbers = (
                round_numbers[: round_numbers.index(2)]
                + [2]
                + random_numbers
                + round_numbers[round_numbers.index(2) + 1 :]
            )  # Adds randomized list at 2
            p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
            p.task_rounds = json.dumps(round_numbers)


# PAGES
class Introduction(Page):
    @staticmethod
    def progress(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return progress

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.round_number == player.participant.vars['task_rounds']['A']
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )


class Checks(Page):
    form_model = 'player'
    form_fields = [
        'recommendation_check',
        'self_select_check',
        'concerned_about_honest',
        'attractive_dishonesty',
    ]

    @staticmethod
    def get_form_fields(player: Player):
        fields = [
            'recommendation_check',
            'self_select_check',
            'concerned_about_honest',
            'attractive_dishonesty',
        ]
        random.shuffle(fields)
        return fields

    @staticmethod
    def progress(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return progress

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.round_number == player.participant.vars['task_rounds']['B']
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def vars_for_template(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return dict(
            curpageindex=curpageindex,
            tot_pages=tot_pages,
            round_number=player.round_number,
            progress=progress,
        )


class Page_2(Page):
    form_model = 'player'
    form_fields = ['mach1', 'mach2', 'mach3', 'mach4', 'mach5', 'mach6', 'mach7', 'mach8', 'mach9']

    @staticmethod
    def progress(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return progress

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.round_number == player.participant.vars['task_rounds']['C']
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def vars_for_template(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return dict(
            curpageindex=curpageindex,
            tot_pages=tot_pages,
            round_number=player.round_number,
            progress=progress,
        )


class Page_3(Page):
    form_model = 'player'
    form_fields = ['narc1', 'narc2', 'narc3', 'narc4', 'narc5', 'narc6', 'narc7', 'narc8', 'narc9']

    @staticmethod
    def progress(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return progress

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.round_number == player.participant.vars['task_rounds']['D']
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def vars_for_template(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return dict(
            curpageindex=curpageindex,
            tot_pages=tot_pages,
            round_number=player.round_number,
            progress=progress,
        )


class Page_4(Page):
    form_model = 'player'
    form_fields = ['psy1', 'psy2', 'psy3', 'psy4', 'psy5', 'psy6', 'psy7', 'psy8', 'psy9']

    @staticmethod
    def progress(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return progress

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.round_number == player.participant.vars['task_rounds']['E']
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def vars_for_template(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return dict(
            curpageindex=curpageindex,
            tot_pages=tot_pages,
            round_number=player.round_number,
            progress=progress,
        )


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
        'kant4',
    ]

    @staticmethod
    def get_form_fields(player: Player):
        fields = [
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
            'kant4',
        ]
        random.shuffle(fields)
        return fields

    @staticmethod
    def progress(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return progress

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.round_number == player.participant.vars['task_rounds']['F']
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def vars_for_template(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return dict(
            curpageindex=curpageindex,
            tot_pages=tot_pages,
            round_number=player.round_number,
            progress=progress,
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

    @staticmethod
    def is_displayed(player: Player):
        return (
            player.round_number == player.participant.vars['task_rounds']['G']
            and player.participant.is_dropout == False
            and player.participant.is_dropout_mate == False
        )

    @staticmethod
    def progress(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return progress

    @staticmethod
    def vars_for_template(player: Player):
        curpageindex = player.round_number - 1
        progress = curpageindex / tot_pages * 100
        return dict(
            curpageindex=curpageindex,
            tot_pages=tot_pages,
            round_number=player.round_number,
            progress=progress,
        )


page_sequence = [Introduction, Checks, Page_2, Page_3, Page_4, Page_5, Demographics]
tot_pages = len(page_sequence)
