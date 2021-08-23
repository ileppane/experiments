from otree.api import Currency as c, currency_range
# from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import numpy as np
import random

# # The import code below does not work here becasue psycopg2 is not istalled,
# # However these codes are necessary to ensure the program to run on servers.
# from psycopg2.extensions import register_adapter, AsIs
# def addapt_numpy_float64(numpy_float64):
#     return AsIs(numpy_float64)
# def addapt_numpy_int64(numpy_int64):
#     return AsIs(numpy_int64)
# register_adapter(np.float64, addapt_numpy_float64)
# register_adapter(np.int64, addapt_numpy_int64)

class Consent(Page):
    form_model = 'player'
    form_fields = ['prolific_code']

class Introduction(Page):
    pass


class PANASpage(Page):
    form_model = 'player'
    form_fields = ['PA1', 'PA2', 'PA3', 'PA4', 'PA5',
                   'NA1', 'NA2', 'NA3', 'NA4', 'NA5',
                   'dt_start', 'dt_end']

    def before_next_page(self):
        self.player.PA_score = self.player.PA1 + self.player.PA2 + self.player.PA3 + \
        self.player.PA4 + self.player.PA5

        self.player.NA_score = (6 - self.player.NA1) + (6 - self.player.NA2) + \
        (6 - self.player.NA3) + (6 - self.player.NA4) + (6 - self.player.NA5)

        self.player.dt_panas = (self.player.dt_end - self.player.dt_start) / 1000


class DOSPERT(Page):
    form_model = 'player'
    form_fields = ['dq1', 'dq2', 'dq3', 'dq4', 'dq5', 'dq6', 'dq7', 'dq8', 'dq9', 'dq10',
                   'dq11', 'dq12', 'dq13', 'dq14', 'dq15', 'dq16', 'dq17', 'dq18', 'dq19', 'dq20',
                   'dq21', 'dq22', 'dq23', 'dq24', 'dq25', 'dq26', 'dq27', 'dq28', 'dq29', 'dq30',
                   'dt_start', 'dt_end']

    def before_next_page(self):

        self.player.RTP_E = self.player.dq6 + self.player.dq9 + self.player.dq10 + self.player.dq16 + self.player.dq29 + self.player.dq30

        self.player.RTP_F = self.player.dq3 + self.player.dq4 + self.player.dq8 + self.player.dq12 + self.player.dq14 + self.player.dq18

        self.player.RTP_FI = self.player.dq12 + self.player.dq4 + self.player.dq18

        self.player.RTP_FG = self.player.dq3 + self.player.dq14 + self.player.dq8

        self.player.RTP_HS = self.player.dq5 + self.player.dq15 + self.player.dq17 + self.player.dq20 + self.player.dq23 + self.player.dq26

        self.player.RTP_R = self.player.dq2 + self.player.dq11 + self.player.dq13 + self.player.dq19 + self.player.dq24 + self.player.dq25

        self.player.RTP_S = self.player.dq1 + self.player.dq7 + self.player.dq21 + self.player.dq22 + self.player.dq27 + self.player.dq28

        self.player.RTP_average = (self.player.RTP_E + self.player.RTP_F + self.player.RTP_HS + self.player.RTP_R + self.player.RTP_S) / 5

        self.player.dt_dospert = (self.player.dt_end - self.player.dt_start) / 1000


""" CRT """
class CRT1page(Page):
    # form_model = models.Player # This seems to be the old way of doing the thing but now it has changed.
    form_model = 'player'
    form_fields = ['crt1', 'dt_start', 'dt_end']

    def vars_for_template(self):
        number = CRT_seq.index(CRT1page) + 1
        return {
            'CRT_total': len(CRT_seq),
            'number': number
        }

    def before_next_page(self):
        if self.player.crt1 == '5 pence':
            self.player.reflectiveness_score += 1
        elif self.player.crt1 == '10 pence':
            self.player.intuitiveness_score += 1

        self.player.dt_crt1 = (self.player.dt_end - self.player.dt_start) / 1000


class CRT2page(Page):
    form_model = 'player'
    form_fields = ['crt2', 'dt_start', 'dt_end']

    def vars_for_template(self):
        number = CRT_seq.index(CRT2page) + 1
        return {
            'CRT_total': len(CRT_seq),
            'number': number
        }

    def before_next_page(self):
        if self.player.crt2 == '5 minutes':
            self.player.reflectiveness_score += 1
        elif self.player.crt2 == '100 minutes':
            self.player.intuitiveness_score += 1

        self.player.dt_crt2 = (self.player.dt_end - self.player.dt_start) / 1000


class CRT3page(Page):
    form_model = 'player'
    form_fields = ['crt3', 'dt_start', 'dt_end']

    def vars_for_template(self):
        number = CRT_seq.index(CRT3page) + 1
        return {
            'CRT_total': len(CRT_seq),
            'number': number
        }

    def before_next_page(self):
        if self.player.crt3 == '47 days':
            self.player.reflectiveness_score += 1
        elif self.player.crt3 == '24 days':
            self.player.intuitiveness_score += 1

        self.player.dt_crt3 = (self.player.dt_end - self.player.dt_start) / 1000


class CRT4page(Page):
    form_model = 'player'
    form_fields = ['crt4', 'dt_start', 'dt_end']

    def vars_for_template(self):
        number = CRT_seq.index(CRT4page) + 1
        return {
            'CRT_total': len(CRT_seq),
            'number': number
        }

    def before_next_page(self):
        if self.player.crt4 == '4 days':
            self.player.reflectiveness_score += 1
        elif self.player.crt4 == '9 days':
            self.player.intuitiveness_score += 1

        self.player.dt_crt4 = (self.player.dt_end - self.player.dt_start) / 1000


class CRT5page(Page):
    form_model = 'player'
    form_fields = ['crt5', 'dt_start', 'dt_end']

    def vars_for_template(self):
        number = CRT_seq.index(CRT5page) + 1
        return {
            'CRT_total': len(CRT_seq),
            'number': number
        }

    def before_next_page(self):
        if self.player.crt5 == '29 students':
            self.player.reflectiveness_score += 1
        elif self.player.crt5 == '30 students':
            self.player.intuitiveness_score += 1

        self.player.dt_crt5 = (self.player.dt_end - self.player.dt_start) / 1000


class CRT6page(Page):
    form_model = 'player'
    form_fields = ['crt6', 'dt_start', 'dt_end']

    def vars_for_template(self):
        number = CRT_seq.index(CRT6page) + 1
        return {
            'CRT_total': len(CRT_seq),
            'number': number
        }

    def before_next_page(self):
        if self.player.crt6 == '20 pounds':
            self.player.reflectiveness_score += 1
        elif self.player.crt6 == '10 pounds':
            self.player.intuitiveness_score += 1

        self.player.dt_crt6 = (self.player.dt_end - self.player.dt_start) / 1000


class CRT7page(Page):
    form_model = 'player'
    form_fields = ['crt7', 'dt_start', 'dt_end']

    def vars_for_template(self):
        number = CRT_seq.index(CRT7page) + 1
        return {
            'CRT_total': len(CRT_seq),
            'number': number
        }

    def before_next_page(self):
        if self.player.crt7 == 'has lost money.':
            self.player.reflectiveness_score += 1
        elif self.player.crt7 == 'is ahead of where he began.':
            self.player.intuitiveness_score += 1

        self.player.dt_crt7 = (self.player.dt_end - self.player.dt_start) / 1000



class End(Page):
    pass


CRT_seq = [CRT1page, CRT2page, CRT3page, CRT4page, CRT5page, CRT6page, CRT7page]

page_sequence = [
Consent,
Introduction,
PANASpage,
DOSPERT,
CRT1page,
CRT2page,
CRT3page,
CRT4page,
CRT5page,
CRT6page,
CRT7page,
End
]


#
# page_sequence = [
# Consent,
# Introduction,
# PANASpage,
# DOSPERT,
# CRT_seq[0],
# CRT_seq[1],
# CRT_seq[2],
# CRT_seq[3],
# CRT_seq[4],
# CRT_seq[5],
# CRT_seq[6],
# End
# ]
