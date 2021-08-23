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

import numpy as np
import time
import random

author = 'Tianqi and Ilkka'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ECI_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                # t = 1000 * time.time() # current time in milliseconds
                # p.participant.vars['seed1'] = int(t) % 2**32

                p.participant.vars['seed1'] = np.random.randint(low = 1000, high = 10000000)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    prolific_code = models.CharField()

    ### PANAS survey (10 items)
    # test scores ranges from 5-25

    PA_score = models.IntegerField(initial=0)
    NA_score = models.IntegerField(initial=0)

    PA1 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )
    PA2 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )
    PA3 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )
    PA4 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )
    PA5 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )

    NA1 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )
    NA2 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )
    NA3 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )
    NA4 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )
    NA5 = models.PositiveIntegerField(
        choices = [[1,'1 = Never'],[2, '2 = Rarely'],[3,'3 = Sometimes'],[4,'4 = Often'],[5,'5 = Always']], widget=widgets.RadioSelect()
        )

    ### DOSPERT survey
    # test scores: RTP (Risk-Taking Propensity), E (Ethical), F (Financial), FI (Financial Investment), FG (Financial Gambling), HS (Health/Safty), R (Recreational), S (Social)
    RTP_E = models.IntegerField(initial=0)
    RTP_F = models.IntegerField(initial=0)
    RTP_FI = models.IntegerField(initial=0)
    RTP_FG = models.IntegerField(initial=0)
    RTP_HS = models.IntegerField(initial=0)
    RTP_R = models.IntegerField(initial=0)
    RTP_S = models.IntegerField(initial=0)
    RTP_average = models.FloatField(initial=0)

    # questions (30 items)
    dq1 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq2 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq3 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq4 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq5 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq6 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq7 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq8 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq9 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq10 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq11 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq12 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq13 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq14 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq15 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq16 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq17 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq18 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq19 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq20 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq21 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq22 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq23 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq24 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq25 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq26 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq27 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq28 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq29 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )
    dq30 = models.PositiveIntegerField(
        choices = [[1,'1 = Extremely Unlikely'],[2,'2 = Moderately Unlikely'],[3,'3 = Somewhat Unlikely'],[4,'4 = Not Sure'],[5,'5 = Somewhat Likely'],[6,'6 = Moderately Likely'],[7,'7 = Extremely Likely']], widget=widgets.RadioSelect()
        )


    ### The following section contians variables the CRT:
    reflectiveness_score = models.IntegerField(initial=0)
    intuitiveness_score = models.IntegerField(initial=0)

    crt1 = models.StringField(widget = widgets.RadioSelect())

    def crt1_choices(self):
        np.random.seed(self.participant.vars['seed1'] + 1)
        choices = ['5 pence', '10 pence', '9 pence', '1 pence']
        np.random.shuffle(choices)
        return choices

    crt2 = models.StringField(widget = widgets.RadioSelect())

    def crt2_choices(self):
        np.random.seed(self.participant.vars['seed1'] + 2)
        choices = ['5 minutes', '100 minutes', '20 minutes', '500 minutes']
        np.random.shuffle(choices)
        return choices

    crt3 = models.StringField(widget = widgets.RadioSelect())

    def crt3_choices(self):
        np.random.seed(self.participant.vars['seed1'] + 3)
        choices = ['47 days', '24 days', '12 days', '36 days']
        np.random.shuffle(choices)
        return choices

    crt4 = models.StringField(widget = widgets.RadioSelect())

    def crt4_choices(self):
        np.random.seed(self.participant.vars['seed1'] + 4)
        choices = ['4 days', '9 days', '12 days', '3 days']
        np.random.shuffle(choices)
        return choices

    crt5 = models.StringField(widget = widgets.RadioSelect())

    def crt5_choices(self):
        np.random.seed(self.participant.vars['seed1'] + 5)
        choices = ['29 students', '30 students', '1 student', '15 students']
        np.random.shuffle(choices)
        return choices

    crt6 = models.StringField(widget = widgets.RadioSelect())

    def crt6_choices(self):
        np.random.seed(self.participant.vars['seed1'] + 6)
        choices = ['20 pounds', '10 pounds', '0 pounds', '30 pounds']
        np.random.shuffle(choices)
        return choices

    crt7 = models.StringField(widget = widgets.RadioSelect())

    def crt7_choices(self):
        np.random.seed(self.participant.vars['seed1'] + 7)
        choices = ['has lost money.', 'is ahead of where he began.', 'has broken even in the stock market.', 'it cannot be determined.']
        np.random.shuffle(choices)
        return choices

    ### The section below contains variables for decition times
    dt_start = models.FloatField()
    dt_end = models.FloatField()
    # the two timers above are for recording the start and end of all other RT measurements.

    dt_dospert = models.FloatField()
    dt_panas = models.FloatField()

    dt_crt1 = models.FloatField()
    dt_crt2 = models.FloatField()
    dt_crt3 = models.FloatField()
    dt_crt4 = models.FloatField()
    dt_crt5 = models.FloatField()
    dt_crt6 = models.FloatField()
    dt_crt7 = models.FloatField()
