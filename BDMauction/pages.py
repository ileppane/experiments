from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, bigger


class Initial(Page):

    def is_displayed(self):
        return self.round_number == 1

class Auction(Page):

    form_model = 'player'
    form_fields = ['WTP']


    def vars_for_template(self):

        reward = self.session.vars["reward"][self.round_number - 1]
        risk = self.session.vars["risk"][self.round_number - 1]
        min_reward = self.session.vars["min_reward"]
        risk_lev = self.session.vars["risk_lev"]

        risk_up = str(100 - risk)
        risk_up_px = ((100 - risk) / 100) * 300
        risk_down = str(risk)
        risk_down_px = (risk / 100) * 300

        if self.round_number == 1:
            floor = 0
        elif reward == min_reward:
            floor = self.player.in_round(self.round_number - 1).WTP
        elif self.round_number % risk_lev == 1:
            floor = self.player.in_round(self.round_number - risk_lev).WTP
        else:
            floor = bigger(self.player.in_round(self.round_number - 1).WTP, self.player.in_round(self.round_number - risk_lev).WTP)


        return {
            'risk_up': risk_up,
            'risk_up_px': str(risk_up_px)+"px",
            'risk_down': risk_down,
            'risk_down_px': str(risk_down_px)+"px",

            'risk_up_posi': str(risk_up_px * 0.5 - 20)+"px",
            'risk_down_posi': str(risk_down_px * 0.5 - 20)+"px",

            'reward': '£' + str(reward),

            'floor': '£' + str(floor)
        }


class End(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

page_sequence = [Initial, Auction, End]
