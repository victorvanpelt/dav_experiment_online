from os import environ

SESSION_CONFIGS = [
    {
        'name': 'dav_full_exp1',
        'display_name': "Experimental Study 1 - Communication",
        'num_demo_participants': 4,
        'app_sequence': ['instructions','dav_game', 'epq', 'payment_info'],
        'communication': 1,
        'self_selection': 0
    },
    {
        'name': 'dav_full_control',
        'display_name': "Control Study - No Communication",
        'num_demo_participants': 4,
        'app_sequence': ['instructions','dav_game', 'epq', 'payment_info'],
        'communication': 0,
        'self_selection': 0
    },
    {
        'name': 'dav_full_exp2',
        'display_name': "Experimental Study 2 - Communication including Chat",
        'num_demo_participants': 4,
        'app_sequence': ['instructions_chat','dav_game_chat', 'epq', 'payment_info'],
        'communication': 1,
        'self_selection': 0
    },
    {
        'name': 'dav_full_exp3a',
        'display_name': "Experimental Study 3 - Communication including Owner",
        'num_demo_participants': 4,
        'app_sequence': ['instructions_three','dav_game_three', 'epq_three', 'payment_info'],
        'communication': 1,
        'self_selection': 0
    },
    {
        'name': 'dav_full_exp3b',
        'display_name': "Experimental Study 3 - Owner",
        'num_demo_participants': 4,
        'app_sequence': ['instructions_owner','dav_game_owner', 'epq_owner', 'payment_info'],
    },
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

mturk_hit_settings = {
    'keywords': ['decision-making', 'study', 'academic'],
    'title': 'Academic study (earn up to $4.30 for +-10 minutes)',
    'description': 'Academic study that pays up to $4.30 for approximately 10 minutes.',
    'frame_height': 500,
    'template': 'global/mturk_template.html',
    'minutes_allotted_per_assignment': 45,
    'expiration_hours': 7*24, # 7 days

    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # No-retakers
        {
            'QualificationTypeId': "3Z755UFFEJQ0G4DCKMPG9LXU3S719U",
            'Comparator': "DoesNotExist",
        },
        # # Masters
        # {
        #         'QualificationTypeId': "2F1QJWKUDD8XADTFD2Q0G6UTO95ALH",
        #         'Comparator': "Exists",
        # },
        # Only US
        {
            'QualificationTypeId': "00000000000000000071",
            'Comparator': "EqualTo",
            'LocaleValues': [{'Country': "US"}]
        },
        # At least x HITs approved
        {
            'QualificationTypeId': "00000000000000000040",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [500]
        },
        # At least x% of HITs approved
        {
            'QualificationTypeId': "000000000000000000L0",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [95]
        },
        ]
}

POINTS_CUSTOM_NAME = 'Lira'

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.0027,
    participation_fee=0.25,
    doc="",
    mturk_hit_settings=mturk_hit_settings
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 2

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
 Server for research on team cost reporting and team composition.
 """

SECRET_KEY = '^i7o@zmr9=x$gdx(pxmcr@u3l8g%-hnysv6k8ap8y@4!^qho!q'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

PARTICIPANT_FIELDS = [
    'is_dropout',
    'is_dropout_mate',
    'is_dofus',
    'communication',
    'self_selection',
    'task_rounds',
    'wait_page_arrival'
]