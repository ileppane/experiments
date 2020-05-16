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

    # The following section contians variables the CRT:
    crt1 = models.StringField(
    choices = ['5 pence', '10 pence', '9 pence', '1 pence'], widget = widgets.RadioSelect()
    )
    crt2 = models.StringField(
    choices = ['5 minutes', '100 minutes', '20 minutes', '500 minutes'], widget = widgets.RadioSelect()
    )
    crt3 = models.StringField(
    choices = ['47 days', '24 days', '12 days', '36 days'], widget = widgets.RadioSelect()
    )
    crt4 = models.StringField(
    choices = ['4 days', '9 days', '12 days', '3 days'], widget = widgets.RadioSelect()
    )
    crt5 = models.StringField(
    choices = ['29 students', '30 students', '1 student', '15 students'], widget = widgets.RadioSelect()
    )
    crt6 = models.StringField(
    choices = ['20 pounds', '10 pounds', '0 pounds', '30 pounds'], widget = widgets.RadioSelect()
    )
    crt7 = models.StringField(
    choices = ['has lost money.', 'is ahead of where he began.', 'has broken even in the stock market.', 'it cannot be determined.'], widget = widgets.RadioSelect()
    )

    # Both scores range between 0 - 7
    reflectiveness_score = models.IntegerField(initial=0)
    intuitiveness_score = models.IntegerField(initial=0)

    # The following section contians variables for the BNT:
    bnt1 = models.StringField(
    choices = ['5 out of 50 throws', '25 out of 50 throws', '30 out of 50 throws', 'None of the above'], widget = widgets.RadioSelect()
    )

    bnt2 = models.StringField(
    choices = ['10 %', '25 %', '40 %', 'None of the above'], widget = widgets.RadioSelect()
    )

    bnt3 = models.StringField(
    choices = ['20 out of 70 throws', '23 out of 70 throws', '35 out of 70 throws', 'None of the above'], widget = widgets.RadioSelect()
    )

    bnt4 = models.StringField(
    choices = ['4 %', '20 %', '50 %', 'None of the above'], widget = widgets.RadioSelect()
    )

    # BNT score ranges between 0 - 4
    bnt_score = models.IntegerField(initial=0)

    # The following section contians variables for the NFC and FI survey
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
