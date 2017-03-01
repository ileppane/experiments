from otree.api import Currency as c, currency_range, safe_json
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import csv


class WelcomePage(Page):
    form_model = models.Player
    form_fields = ['prolificcode']


class ElicitSVO(Page):
    form_model = models.Player
    form_fields = ['allocation1', 'allocation2', 'allocation3', 'allocation4', 'allocation5', 'allocation6']

    def vars_for_template(self):
        ifile = open('test.csv', 'rt')
        alloc = []
        try:
            reader = csv.reader(ifile)
            for row in reader:
                alloc.append(list(map(int,row)))
        finally:
            ifile.close()

        return {
            'alloc': safe_json(alloc)
        }


class Results(Page):

    form_model = models.Player
    form_fields = ['check1', 'check2']

    def vars_for_template(self):
        ifile = open('test.csv', 'rt')
        alloc = []
        try:
            reader = csv.reader(ifile)
            for row in reader:
                alloc.append(list(map(int,row)))
        finally:
            ifile.close()

        return {
            'alloc': safe_json(alloc),
            'alloc2': safe_json(self.player.allocation2)
        }


page_sequence = [
    WelcomePage,
    ElicitSVO,
    Results
]
