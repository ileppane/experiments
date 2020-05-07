from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, bigger
import random
from random import choice

class Initial(Page):

    def is_displayed(self):
        return self.round_number == 1

class Auction(Page):

    form_model = 'player'
    form_fields = ['WTP']


    def vars_for_template(self):

        reward = self.session.vars["reward_auc"][self.round_number - 1]
        risk = self.session.vars["risk_auc"][self.round_number - 1]
        min_reward = self.session.vars["min_reward_auc"]
        risk_lev = self.session.vars["risk_lev_auc"]

        self.player.reward = reward
        self.player.risk = risk

        self.player.treatment = self.session.vars["treatment"]

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

    def before_next_page(self):

        endowment = 32

        pick_round = choice(range(1, Constants.num_rounds +1))

        reward = self.session.vars["reward_auc"][pick_round - 1]
        risk = self.session.vars["risk_auc"][pick_round - 1]

        selling_price = round(random.uniform(0, reward), 2)

        WTP = self.player.in_round(pick_round).WTP
        if selling_price < WTP:
            proceed = True
        else:
            proceed = False

        dice = random.randint(1, 100)
        if dice <= risk:
            win = True
            payoff = endowment - selling_price + reward
        else:
            win = False
            payoff = endowment - selling_price

        payoff_auc = {"endowment": endowment, "pick_round": pick_round, "reward": reward, "risk": risk, "WTP": WTP, "selling_price": selling_price, "proceed": proceed, "win": win, "payoff": payoff}

        self.participant.vars['payoff_auc'] = payoff_auc





page_sequence = [Initial, Auction, End]
