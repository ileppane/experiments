from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class REIpage(Page):
    form_model = models.Player
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31']#, 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40']
    # the below are only for NFCFI31

    def before_next_page(self):
        self.player.nfcscore = (6-self.player.q1) + (6-self.player.q2) + self.player.q3 + (6-self.player.q4) + (6-self.player.q5) + (6-self.player.q6) + (6-self.player.q7) + self.player.q8 + (6-self.player.q9) + (6-self.player.q10) + (6-self.player.q11) + self.player.q12 + (6-self.player.q13) + self.player.q14 + (6-self.player.q15) + (6-self.player.q16) + self.player.q17 + (6-self.player.q18) + (6-self.player.q19)

        self.player.fiscore = self.player.q20 + self.player.q21 + self.player.q22 + self.player.q23 + self.player.q24 + self.player.q25 + self.player.q26 + self.player.q27 + self.player.q28 + self.player.q29 + self.player.q30 + self.player.q31


class End(Page):
    pass


page_sequence = [Introduction, REIpage, End]
