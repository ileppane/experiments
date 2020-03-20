from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, set_time


class InitialPage(Page):

    def is_displayed(self):
        return self.round_number == 1


class FixationPage(Page):

    # timer can be hidden from the page with CSS: https://otree.readthedocs.io/en/latest/timeouts.html#customizing-the-timer
    timeout_seconds = 1

    def before_next_page(self):
        self.player.dectime = set_time() # here we set the start of the dectime in unix seconds


class DecisionPage(Page):

#    timeout_seconds = 5

    form_model = 'player'
    form_fields = ['choice']


    def vars_for_template(self):

        # this determines the height of the blue and red boxes in the right stimulus
        # and the text inside them
        # can be programmed to change in every round using self.round_number in for-loop

        reward = self.session.vars["reward"][self.round_number - 1]
        risk = self.session.vars["risk"][self.round_number - 1]
        certainty = self.session.vars["certainty"][self.round_number - 1]
        display = self.session.vars["display"][self.round_number - 1]

        risk_up = str(100 - risk)
        risk_up_px = ((100 - risk) / 100) * 300
        risk_down = str(risk)
        risk_down_px = (risk / 100) * 300

        return {
            'risk_up': risk_up,
            'risk_up_px': str(risk_up_px)+"px",
            'risk_down': risk_down,
            'risk_down_px': str(risk_down_px)+"px",

            'risk_up_posi': str(risk_up_px * 0.5 - 20)+"px",
            'risk_down_posi': str(risk_down_px * 0.5 - 20)+"px",

            'reward': '£' + str(reward),
            'certainty': '£' + str(certainty),
            'display': display
        }

    def before_next_page(self):
        self.player.dectime = set_time() - self.player.dectime # here we subtract from current unix time the start of the decision round that was set in the fixation page


class RestPage(Page):

    def is_displayed(self):
        rest_after = 4
        rest_round = list(range(rest_after, Constants.num_rounds, rest_after))
        if self.round_number in rest_round:
            return True
        else:
            return False

    timeout_seconds = 1


class FinishPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


# page_sequence = [InitialPage, DecisionPage, RestPage, FinishPage]

page_sequence = [InitialPage, FixationPage, DecisionPage, RestPage, FinishPage]
