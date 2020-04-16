import os
from os import environ

import random

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True


# don't share this with anybody.
SECRET_KEY = 'g#^90ip)&$$q-q!4@sv90@r%if&a5*%zhye*@s75t7s&80z@2q'

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

SENTRY_DSN = 'http://7bba1340f6ba4cdea4a43db7cdede209:e1ce95d7ef444299bbac99164877f292@sentry.otree.org/140'

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = True
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 5
POINTS_CUSTOM_NAME = ''
POINTS_DECIMAL_PLACES = 2

# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]


# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 5,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'funnel',
        'display_name': 'Deming funnel experiment',
        'num_demo_participants': 1,
        'app_sequence': ['funnel'],
    },

    # {
    #     'name': 'MCN',
    #     'display_name': 'Modelling Cognitive Noise',
    #     'num_demo_participants': 1,
    #     # 'app_sequence': ['cognitivenoise', 'BDMauction'],
    #     'app_sequence': ['REItest', 'BDMauction', 'cognitivenoise'],
    # },

    {
        'name': 'REItest',
        'display_name': 'REI Survey',
        'num_demo_participants': 1,
        # 'app_sequence': ['REItest'],
        'app_sequence': ['REItest'],#, 'BDMauction', 'cognitivenoise'],
    },
    {
        'name': 'BDMauction',
        'display_name': 'BDMauction',
        'num_demo_participants': 1,
        'app_sequence': ['BDMauction','cognitivenoise'],
    },
    {
        'name': 'cognitivenoise',
        'display_name': 'Decision Task in Cognitive Noise Study',
        'num_demo_participants': 1,
        'app_sequence': ['cognitivenoise'],
        # 'app_sequence': ['cognitivenoise', 'BDMauction'],
    },
    {
        'name': 'eoq',
        'display_name': 'Stock Control Game',
        'num_demo_participants': 1,
        'app_sequence': ['eoq'],
        'simple': 'yes',
        'randomdemandgame': 'no'
    },
    {
        'name': 'foundationtask',
        'display_name': 'foundationtask',
        'num_demo_participants': 1,
        'app_sequence': ['foundationtask'],
        'returnurl': 'http://www.google.com'
    },
    # {
    #     'name': 'prolificgame',
    #     'display_name': 'prolificgame',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['svo','nvsingle','nvcompnoniid'],
    #     'prolificurl': 'https://www.prolific.ac'
    # },
    # {
    #     'name': 'svo',
    #     'display_name': 'svo',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['svo']
    # },
    # {
    #     'name': 'nvsingle',
    #     'display_name': 'nvsingle',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['nvsingle']
    # },
    # {
    #     'name': 'nvcompnoniid2',
    #     'display_name': 'nvcompnoniid2',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['nvcompnoniid2'],
    # 	'prolificurl': 'https://www.prolific.ac'
    # },
    # {
    #     'name': 'nvcompnoniid',
    #     'display_name': 'nvcompnoniid',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['nvcompnoniid'],
    # 	'prolificurl': 'https://www.prolific.ac'
    # },
    # {
    #     'name': 'nvcomp',
    #     'display_name': 'nvcomp',
    #     'num_demo_participants': 2,
    #     'app_sequence': ['nvsingle', 'nvcomp'],
    # 'prolificurl': 'https://www.prolific.ac'
    # },
    # {
    #     'name': 'ERQ',
    #     'display_name': 'ERQ',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['ERQ']
    # },
    # {
    #     'name': 'DOSPERT',
    #     'display_name': 'DOSPERT',
    #     'num_demo_participants': 1,
    #     'prolificurl': 'https://www.prolific.ac',
    #     'app_sequence': ['DOSPERT']
    # },
    # {
    #     'name': 'neuronewsvendor',
    #     'display_name': 'Neuronewsvendor (blocks)',
    #     'num_demo_participants': 1,
    #     'app_sequence': ['svofirst', 'neuronewsvendor', 'DOSPERT'],
    #     'prolificurl': 'https://www.prolific.ac',
    #     'margin': 'high',
    #     'blocks1': ['reap', 'att', 'att', 'reap', 'att', 'reap', 'reap', 'att'],
    #     'blocks2': ['att',  'reap', 'reap', 'att', 'reap', 'att', 'att', 'reap']
    # },
    # {
    #     'name': 'OMNV',
    #     'display_name': "Newsvendor game for OM participants",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['OMNV'],
    #     'margin': random.choice(['low','high']),
    # },
    # {
    #     'name': 'dsraq',
    #     'display_name': "DSR and AQ",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['dsraq'],
    # },
    # {
    #     'name': 'dreber',
    #     'display_name': "Repeated PD",
    #     'num_demo_participants': 2,
    #     'app_sequence': ['dreber'],
    #     'prolificurl': 'http://www.google.com',
    #     'treatment': 'p1',
    # },
    # {
    #     'name': 'twopartynewsvendor',
    #     'display_name': "Two party newsvendor",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['svo', 'twopartynewsvendor'],
    #     'prolificurl': 'https://prolific.ac/submissions/complete?cc=5A8RZ4J9',
    #     'margin': 'low',
    # },
    # {
    #     'name': 'linkstudy',
    #     'display_name': "linkstudy",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['linkstudy','LAFsurvey'],
    #     'prolificurl': 'http://www.google.com',
    # },
    # {
    #     'name': 'LAFsurvey',
    #     'display_name': "LAFsurvey",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['LAFsurvey'],
    # },
    # {
    #     'name': 'neutralvendor',
    #     'display_name': "Neutralvendor",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['svo', 'neutralvendor'],
    # 	'prolificurl': 'http://www.google.com',
    # },
    # {
    #     'name': 'newsvendor',
    #     'display_name': "Newsvendor",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['newsvendor','svo'],
    # 	'prolificurl': 'http://www.google.com',
    # 	'margin': 'low',
    # },

]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
