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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'REItest'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # name = models.CharField()
    # email = models.CharField()
    # student_number = models.CharField()

    nfcscore = models.PositiveIntegerField()
    fiscore = models.PositiveIntegerField()


    q1 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q2 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())

    q3 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q4 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q5 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q6 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q7 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q8 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q9 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q10 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q11 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q12 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q13 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q14 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q15 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q16 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q17 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q18 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q19 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q20 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q21 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q22 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q23 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q24 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q25 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q26 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q27 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q28 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q29 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q30 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q31 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    '''
    q32 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q33 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q34 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q35 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q36 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q37 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q38 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q39 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    q40 = models.PositiveIntegerField(
        choices = [[1,'1 = definitely not true'],[2, '2 = somewhat not true'],[3,'3 = neither true nor untrue'],[4,'4 = somewhat true'],[5,'5 = definitely true']], widget=widgets.RadioSelect())
    '''
