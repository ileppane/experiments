from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random, time, csv
from timeit import default_timer as timer


author = 'IL'

doc = """
Newsvendor game
Payoffs given in a payoff table
High and low margin treatments
"""


def trueorderquantity(orderquantity, margin):

    if (margin == 'low'):
        toq = 500 + orderquantity * 50
    else:
        toq = 300 + orderquantity * 100

    return toq


def profit(demand, orderquantity, margin):

    toq = trueorderquantity(orderquantity, margin)

    if (margin == 'low'):
        if (demand >= toq):
            prof = 7.28 * toq - 5.72 * toq
        else:
            prof = 7.28 * demand - 5.72 * toq

    else:
        if (demand >= toq):
            prof = 1.78 * toq - 0.38 * toq
        else:
            prof = 1.78 * demand - 0.38 * toq

    return prof


def set_time():

    timme = timer()

    return timme


class Constants(BaseConstants):

    name_in_url = 'newsvendor'
    players_per_group = None
    num_rounds = 25
    endowment = None


class Subsession(BaseSubsession):

    def before_session_starts(self):

        ifile = open('randomdemand.csv', 'rt')
        dema = []
        try:
            reader = csv.reader(ifile)
            for row in reader:
                dema.append(list(map(int, row)))
        finally:
            ifile.close()

        if (self.session.config['margin'] == 'low'):
            self.session.vars['demand'] = dema[0]

        else:
            self.session.vars['demand'] = dema[1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    starttime = models.FloatField()
    endtime = models.FloatField()
    orderquantity = models.PositiveIntegerField(choices=[0, 1, 2, 3, 4, 5, 6], widget=widgets.RadioSelect())
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
