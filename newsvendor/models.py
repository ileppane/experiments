from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random, time
from timeit import default_timer as timer


author = 'IL'

doc = """
Newsvendor game, 30 rounds with low/high margin treatments
Demand distribution should be the same for players!
Treatments randomized
Payoffs given in a payoff table
Two subsessions: high and low margin treatments
"""


class Constants(BaseConstants):

    name_in_url = 'newsvendor'
    players_per_group = None
    num_rounds = 4
    endowment = None


class Subsession(BaseSubsession):

    def before_session_starts(self):

        margin = random.sample(['low','high'], 1)
        self.session.vars['margin'] = margin[0]
        demandlow = [0]*int(Constants.num_rounds)
        demandhigh = [0]*int(Constants.num_rounds)

        t = 0
        while t < Constants.num_rounds:
            demandlow[t] = random.randrange(500, 800, 50)
            demandhigh[t] = random.randrange(300, 900, 100)
            t += 1

        if (margin[0] == 'low'):
            self.session.vars['demand'] = demandlow

        if (margin[0] == 'high'):
            self.session.vars['demand'] = demandhigh


class Group(BaseGroup):

    def set_payoffs(self):

        for p in self.get_players():

            p.demand = self.session.vars['demand'][self.round_number - 1]

            if (p.margin == 'low'):

                p.trueorderquantity = 500 + p.orderquantity * 50

                if (self.session.vars['demand'][self.round_number-1] >= (500+p.orderquantity*50)):
                    p.payoff = 7.28*(500+p.orderquantity*50) - 5.72*(500+p.orderquantity*50)
                else:
                    p.payoff = 7.28*self.session.vars['demand'][self.round_number-1] - 5.72*(500+p.orderquantity*50)

            else:

                p.trueorderquantity = 300 + p.orderquantity * 100

                if (self.session.vars['demand'][self.round_number-1] >= (300+p.orderquantity*100)):
                    p.payoff = 1.78*(300+p.orderquantity*100) - 0.38*(300+p.orderquantity*100)
                else:
                    p.payoff = 1.78*self.session.vars['demand'][self.round_number-1] - 0.38*(300+p.orderquantity*100)

    def start_timer(self):

        for p in self.get_players():
            p.starttime = timer()

    def end_timer(self):

        for p in self.get_players():
            p.endtime = timer()

    def set_margin(self):

        for p in self.get_players():
            p.margin = self.session.vars['margin']


class Player(BasePlayer):

    margin = models.CharField()
    starttime = models.FloatField()
    endtime = models.FloatField()

    orderquantity = models.PositiveIntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6], widget=widgets.RadioSelect())
    trueorderquantity = models.PositiveIntegerField()
    demand = models.PositiveIntegerField()

    check1low = models.PositiveIntegerField(
        choices=[[1, '936'], [2, '364'], [3, '858']], widget=widgets.RadioSelect(), blank=True)
    check2low = models.PositiveIntegerField(
        choices=[[1, '0'], [2, '1/7'], [3, '5/7']], widget=widgets.RadioSelect(), blank=True)
    check3low = models.PositiveIntegerField(
        choices=[[1, '5/7'], [2, '1/7'], [3, '2/7']], widget=widgets.RadioSelect(), blank=True)
    check1high = models.PositiveIntegerField(
        choices=[[1, '560'], [2, '522'], [3, '662']], widget=widgets.RadioSelect(), blank=True)
    check2high = models.PositiveIntegerField(
        choices=[[1, '0'], [2, '1/7'], [3, '5/7']], widget=widgets.RadioSelect(), blank=True)
    check3high = models.PositiveIntegerField(
        choices=[[1, '5/7'], [2, '1/7'], [3, '2/7']], widget=widgets.RadioSelect(), blank=True)

    check4 = models.PositiveIntegerField(
        choices=[[1, 'Not all customers can be satisfied'], [2, 'Nothing'], [3, 'Not all items can be sold']], widget=widgets.RadioSelect(), blank=True)
    check5 = models.PositiveIntegerField(
        choices=[[1, '£0.11'], [2, '£11.30'], [3, '£1.13']], widget=widgets.RadioSelect(), blank=True)

    pecu = models.PositiveIntegerField(
        choices=[[1, '1 = Not at all'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9 = As much as possible']], widget=widgets.RadioSelect())
    nonpecu = models.PositiveIntegerField(
        choices=[[1, '1 = Not at all'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9 = As much as possible']], widget=widgets.RadioSelect())
    conflict = models.PositiveIntegerField(
        choices=[[1, '1 = Least conflicted'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9 = Most conflicted']], widget=widgets.RadioSelect())