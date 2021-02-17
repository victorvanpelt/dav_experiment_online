from os import environ

SESSION_CONFIGS = [
    {
        'name': 'run_dav_experiment_full_ss',
        'display_name': "Dav full select",
        'num_demo_participants': 4,
        'app_sequence': ['dav_game', 'epq', 'payment_info'],
        'communication': 3,
        'self_selection': 1,
        'completion_code': "RPT20210209"
    },
    {
        'name': 'run_dav_experiment_full_no_ss',
        'display_name': "DAV full no select",
        'num_demo_participants': 4,
        'app_sequence': ['dav_game', 'epq', 'payment_info'],
        'communication': 3,
        'self_selection': 0,
        'completion_code': "RPT20210209"
    },
    {
        'name': 'dav_session_no_comm_ss',
        'display_name': "DAV no comm select",
        'num_demo_participants': 4,
        'app_sequence': ['dav_game', 'payment_info'],
        'communication': 0,
        'self_selection': 1,
        'completion_code': "RPT20210209"
    },
    {
        'name': 'dav_session_no_comm_no_ss',
        'display_name': "DAV no comm no select",
        'num_demo_participants': 4,
        'app_sequence': ['dav_game', 'payment_info'],
        'communication': 0,
        'self_selection': 0,
        'completion_code': "RPT20210209"
    },
    {
        'name': 'dav_session_comm_ss',
        'display_name': "DAV comm select",
        'num_demo_participants': 4,
        'app_sequence': ['dav_game', 'payment_info'],
        'communication': 1,
        'self_selection': 1,
        'completion_code': "RPT20210209"
    },
    {
        'name': 'dav_session_comm_no_ss',
        'display_name': "DAV comm no select",
        'num_demo_participants': 4,
        'app_sequence': ['dav_game', 'payment_info'],
        'communication': 1,
        'self_selection': 0,
        'completion_code': "RPT20210209"
    },
    # {
    #     'name': 'epq',
    #     'display_name': "Test EPQ",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['epq', 'payment_info'],
    #     'completion_code': "RPT20210209"
    # },
    # {
    #     'name': 'dav_session_nocomm_all',
    #     'display_name': "Test dav experiment no comm + epq",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['dav_game', 'epq', 'payment_info'],
    #     'communication': 0
    # },
    # {
    #     'name': 'dav_session_comm_all',
    #     'display_name': "Test dav experiment comm + epq",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['dav_game', 'epq', 'payment_info'],
    #     'communication': 1
    # },
    # {
    #     'name': 'payment_info',
    #     'display_name': "Test payment info",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['payment_info'],
    #     'completion_code': "RPT20210209"
    # },
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

mturk_hit_settings_cd = {
    'keywords': ['decision-making', 'study', 'academic'],
    'title': 'Academic study (earn up to $4.05 for +-10 minutes)',
    'description': 'Academic study in which you can earn money based on your and another person`s decisions. Takes approximately 10 minutes to complete).',
    'frame_height': 500,
    'template': 'global/mturk_template.html',
    'minutes_allotted_per_assignment': 45,
    'expiration_hours': 7*24, # 7 days

    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # No-retakers
        {
            'QualificationTypeId': "30LLG2NWCXJ09FSUO3LGVGEKYUS095",
            'Comparator': "DoesNotExist",
        },
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
            'IntegerValues': [98]
        },
        ]
}

POINTS_CUSTOM_NAME = 'Lira'

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.0027,
    participation_fee=1.35,
    doc="",
    #use_browser_bots=True
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 2

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
 Server for research on team misreporting and team composition
 """

SECRET_KEY = '^i7o@zmr9=x$gdx(pxmcr@u3l8g%-hnysv6k8ap8y@4!^qho!q'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
