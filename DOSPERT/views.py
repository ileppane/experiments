from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from decimal import Decimal, ROUND_HALF_UP


class Questions(Page):
    form_model = models.Player
    form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30']

    #def before_next_page(self):
    #    self.player.dospertscore = self.player.q1


class Proceed(Page):

    def vars_for_template(self):

        return {

        }


page_sequence = [
    Questions,
    Proceed
]
