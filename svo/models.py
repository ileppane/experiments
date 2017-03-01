from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
SVO: 6 dictator allocations, strategy method, each has 9 options
"""


class Constants(BaseConstants):
    name_in_url = 'svo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolificcode = models.CharField()

    allocation1 = models.PositiveIntegerField(
        choices=[1,2,3,4,5,6,7,8,9], widget=widgets.RadioSelect())

    allocation2 = models.PositiveIntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9], widget=widgets.RadioSelect())

    allocation3 = models.PositiveIntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9], widget=widgets.RadioSelect())

    allocation4 = models.PositiveIntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9], widget=widgets.RadioSelect())

    allocation5 = models.PositiveIntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9], widget=widgets.RadioSelect())

    allocation6 = models.PositiveIntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7, 8, 9], widget=widgets.RadioSelect())

    check1 = models.PositiveIntegerField()
    check2 = models.PositiveIntegerField()