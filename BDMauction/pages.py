from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, bigger, lottery_generator
import numpy as np
import pandas as pd

class Initial(Page):

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):

        endowment = self.session.vars['endowment']
        pound = endowment / self.session.vars['exchange']
        # endowment = 25
        # pound = endowment / 5

        if pound.is_integer():
            pound = int(pound)

        reward = 12
        risk = 75

        risk_up = str(100 - risk)
        risk_up_px = ((100 - risk) / 100) * 300
        risk_down = str(risk)
        risk_down_px = (risk / 100) * 300

        bid = 8.5
        win = endowment - bid + reward
        loss = endowment - bid

        return {
            'endowment': '$' + str(endowment),
            'pound': '£' + str(pound),

            'reward': '$' + str(reward),

            'risk_up': risk_up,
            'risk_up_px': str(risk_up_px)+"px",
            'risk_down': risk_down,
            'risk_down_px': str(risk_down_px)+"px",

            'risk_up_posi': str(risk_up_px * 0.5 - 20)+"px",
            'risk_down_posi': str(risk_down_px * 0.5 - 20)+"px",

            'bid': '$' + str(bid),
            'win': '$' + str(win),
            'loss': '$' + str(loss),
        }


class Auction(Page):

    form_model = 'player'
    form_fields = ['WTP', 'jsdectime_start', 'jsdectime_end']


    def vars_for_template(self):

        treatment = self.session.vars["treatment"]
        # treatment = np.random.choice(['A','E'])
        # treatment = 'A'
        # treatment = 'E'

        scaler = 2**0.5
        min_reward = 7.85
        min_risk = 41
        reward_lev = 4
        risk_lev = 3

        lottery_table = lottery_generator(scaler, min_reward, min_risk, reward_lev, risk_lev, treatment)

        reward = lottery_table['reward'][self.round_number - 1]
        risk = lottery_table['risk'][self.round_number - 1]

        self.player.reward = reward
        self.player.risk = risk

        risk_up = str(100 - risk)
        risk_up_px = ((100 - risk) / 100) * 300
        risk_down = str(risk)
        risk_down_px = (risk / 100) * 300

        # floor = 0

        if self.round_number == 1:
            floor = 0
        elif reward == min_reward or reward == round(min_reward):
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

            'reward': '$' + str(reward),

            'floor': '$' + str(floor),
            'ceiling': '$' + str(float(reward)),

        }

    def before_next_page(self):
        # JavaScript Method of dectime collection:
        self.player.jsdectime = (self.player.jsdectime_end - self.player.jsdectime_start) / 1000

        self.player.treatment = self.session.vars["treatment"]



class End(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):

        # Otherwise a participant can refresh the page to get desired outcome (though hidden in this app)
        seed = self.session.vars['seed2']
        np.random.seed(seed)

        ######

        endowment = self.session.vars['endowment']

        pick_round = np.random.choice(range(1, Constants.num_rounds +1))

        reward = self.player.in_round(pick_round).reward
        risk = int(self.player.in_round(pick_round).risk)

        selling_price = round(np.random.uniform(0, reward), 2)

        WTP = self.player.in_round(pick_round).WTP
        if selling_price <= WTP:
            proceed = True
        else:
            proceed = False

        dice = np.random.randint(1, 101)
        if dice <= risk:
            win = True
            payoff = round(endowment - selling_price + reward, 2)
        else:
            win = False
            payoff = round(endowment - selling_price, 2)

        payoff_auc = {"endowment": endowment, "pick_round": pick_round, "reward": reward, "risk": risk, "WTP": WTP, "selling_price": selling_price, "proceed": proceed, "win": win, "payoff": payoff}

        self.player.payoff_auc = str(payoff_auc)

        self.participant.vars['payoff_auc'] = payoff_auc





page_sequence = [
Initial,
Auction,
End
]
