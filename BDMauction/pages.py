from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, bigger, lottery_generator


class Initial(Page):

    def is_displayed(self):
        return self.round_number == 1

class Auction(Page):

    form_model = 'player'
    form_fields = ['WTP']

    def vars_for_template(self):

        scaler = 2 ** 0.5
        min_reward = 5.55
        min_risk = 43
        reward_lev = 6
        risk_lev = 3

        min_reward = min_reward
        risk_lev = risk_lev

        lottery_table = lottery_generator(scaler, min_reward, min_risk, reward_lev, risk_lev)

        reward = lottery_table['reward'][self.round_number - 1]
        risk = lottery_table['risk'][self.round_number - 1]

        risk_up = str(100 - risk)
        risk_up_px = ((100 - risk) / 100) * 300
        risk_down = str(risk)
        risk_down_px = (risk / 100) * 300

        # floor = 0

        if self.round_number == 1:
            floor = 0
        elif reward == min_reward:
            floor = self.player.in_round(self.round_number - 1).WTP
        elif self.round_number % risk_lev == 1:
            floor = self.player.in_round(self.round_number - risk_lev).WTP
        else:
            floor = bigger(self.player.in_round(self.round_number - 1).WTP, self.player.in_round(self.round_number - risk_lev).WTP)

        bar_length = (reward - floor) / 31.4
        bar_length = bar_length * 1.5 + 0.2 #just to make it longer in case it is too short
        if bar_length > 1:
            bar_length = 1

        initial_value = (reward - floor) / 2 + floor

        return {
            'risk_up': risk_up,
            'risk_up_px': str(risk_up_px)+"px",
            'risk_down': risk_down,
            'risk_down_px': str(risk_down_px)+"px",

            'risk_up_posi': str(risk_up_px * 0.5 - 20)+"px",
            'risk_down_posi': str(risk_down_px * 0.5 - 20)+"px",

            'reward': '£' + str(reward),
            'floor': '£' + str(floor),
            'reward_raw': str(reward),
            'floor_raw': str(floor),

            'bar_length': str(bar_length * 100) + "%",
            'initial_value': str(initial_value)
        }


class End(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

page_sequence = [Initial, Auction, End]
