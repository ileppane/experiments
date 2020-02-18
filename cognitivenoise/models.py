from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from timeit import default_timer as timer


author = 'Your name here'

doc = """
App with decision task, to come after elicitation task
"""


def set_time():

    time_now = timer()

    return time_now


class Constants(BaseConstants):
    name_in_url = 'cognitivenoise'
    players_per_group = None
    num_rounds = 10 # this can be changed later
    instructions_template = 'cognitivenoise/Instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    choice = models.StringField()
    starttime = models.FloatField()
    endtime = models.FloatField()