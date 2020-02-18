from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, set_time


class InitialPage(Page):

    def is_displayed(self):
        return self.round_number == 1


class FixationPage(Page):

    timeout_seconds = 2

    def before_next_page(self):
        self.player.starttime = set_time()


class DecisionPage(Page):

#    timeout_seconds = 5

    form_model = 'player'
    form_fields = ['choice']


    def vars_for_template(self):

        # this determines the height of the blue and red boxes in the right stimulus
        # and the text inside them
        # can be programmed to change in every round using self.round_number in for-loop
        upval = "30%"
        upvalpx = 0.3*300
        downval = "70%"
        downvalpx = 0.7*300

        return {
            'upvalpx': str(upvalpx)+"px",
            'downvalpx': str(downvalpx)+"px",
            'upval': upval,
            'downval': downval
        }

    def before_next_page(self):
        self.player.endtime = set_time()


class RestPage(Page):

    def is_displayed(self):
        return self.round_number == 5 | self.round_number == 7 # shown only on these rounds

    timeout_seconds = 5


class FinishPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [InitialPage, FixationPage, DecisionPage, RestPage, FinishPage]