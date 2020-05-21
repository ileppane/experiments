from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, set_time, trial_generator
import numpy as np
import pandas as pd
import time


class InitialPage(Page):

    def is_displayed(self):
        return self.round_number == 1


class FixationPage(Page):

    # timer can be hidden from the page with CSS: https://otree.readthedocs.io/en/latest/timeouts.html#customizing-the-timer
    timeout_seconds = 0.5

    def before_next_page(self):
        self.player.pydectime = set_time() # here we set the start of the dectime in unix seconds


class DecisionPage(Page):

    # timeout_seconds = 2

    form_model = 'player'
    form_fields = ['choice', 'jsdectime_start', 'jsdectime_end']

    def vars_for_template(self):

        # this determines the height of the blue and red boxes in the right stimulus
        # and the text inside them
        # can be programmed to change in every round using self.round_number in for-loop

        treatment = self.session.vars['treatment']
        # treatment = np.random.choice(['A','E'])
        # treatment = 'A'
        # treatment = 'E'

        scaler = 2**0.5
        min_reward = 7.85
        min_risk = 41
        reward_lev = 4
        risk_lev = 3
        m_values = list(range(0,9))

        trial_table = trial_generator(scaler, min_reward, min_risk, reward_lev, risk_lev, m_values, treatment)

        reward = trial_table['reward'][self.round_number - 1]
        risk = trial_table['risk'][self.round_number - 1]
        certainty = trial_table['certainty'][self.round_number - 1]
        display = trial_table['display'][self.round_number - 1]

        if certainty.is_integer():
            certainty = int(certainty)

        self.player.reward = reward
        self.player.risk = risk
        self.player.certainty = certainty
        self.player.display = display

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

            'reward': '$' + str(reward),
            'certainty': '$' + str(certainty),
            'display': display,
        }

    def before_next_page(self):
        # Python Method of dectime collection: here we subtract from current unix time the start of the decision round that was set in the fixation page
        self.player.pydectime = set_time() - self.player.pydectime

        # JavaScript Method of dectime collection:
        self.player.jsdectime = (self.player.jsdectime_end - self.player.jsdectime_start) / 1000

        self.player.treatment = self.session.vars["treatment"]




class AfterPage(Page):
    # This AfterPage is used to display the confirmation animation, and to make the environment for Python time recording as simple as possible.

    timeout_seconds = 0.5

    def vars_for_template(self):


        reward = self.player.reward
        risk = self.player.risk
        certainty = self.player.certainty
        display = self.player.display

        choice = self.player.choice

        if reward.is_integer():
            reward = int(reward)

        if risk.is_integer():
            risk = int(risk)

        if certainty.is_integer():
            certainty = int(certainty)

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

            'reward': '$' + str(reward),
            'certainty': '$' + str(certainty),
            'display': display,
            'choice': choice
        }


class RestPage(Page):

    timeout_seconds = 300

    def is_displayed(self):
        rest_after = 3
        rest_round = list(range(rest_after, Constants.num_rounds, rest_after))
        if self.round_number in rest_round:
            return True
        else:
            return False

    # def vars_for_template(self):


class FinishPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        # Otherwise a participant can refresh the page to get desired outcome
        seed = self.session.vars['seed3']
        np.random.seed(seed)

        ######
        payoff_auc = self.participant.vars['payoff_auc']

        ######
        endowment = 32

        pick_round = np.random.choice(range(1, Constants.num_rounds +1))

        reward = self.player.in_round(pick_round).reward
        risk = int(self.player.in_round(pick_round).risk)
        certainty = self.player.in_round(pick_round).certainty
        display = self.player.in_round(pick_round).display

        LR = self.player.in_round(pick_round).choice
        if display == 0 and LR == 'left' or display == 1 and LR == 'right':
            # lottery is chosen
            proceed = True
        else:
            proceed = False

        dice = np.random.randint(1, 101)
        if dice <= risk:
            win = True
            payoff = endowment - certainty + reward
        else:
            win = False
            payoff = endowment - certainty

        payoff_ddm = {"endowment": endowment, "pick_round": pick_round, "reward": reward, "risk": risk, "certainty": certainty, "proceed": proceed, "win": win, "payoff": payoff}

        # # Just to test the program
        # pay_from = 'auc'
        # pay_from = 'ddm'

        pay_from = np.random.choice(['auc','ddm'])

        # record the payoff info
        if pay_from == 'auc':
            payoff_auc["pay_from"] = "auc"
            self.player.pay = str(payoff_auc)
        else:
            payoff_ddm["pay_from"] = "ddm"
            self.player.pay = str(payoff_ddm)

        # scenario verdict
        if pay_from == 'auc':
            # payoff to be chosen from the acution
            if payoff_auc["proceed"] == False:
                scenario = 1
                # selling price greater than the WTP
            elif payoff_auc["win"] == False:
                scenario = 2
                # open lottery and lose
            else:
                scenario = 3
                # open lottery and win

            return {
                'scenario': scenario,
                'endowment': payoff_auc["endowment"],
                'pick_round': payoff_auc["pick_round"],
                'reward': payoff_auc["reward"],
                'risk': payoff_auc["risk"],
                'WTP': payoff_auc["WTP"],
                'selling_price': payoff_auc["selling_price"],
                'payoff': payoff_auc["payoff"]
            }

        # payoff to be chosen from the binary choices
        else:
            if payoff_ddm["proceed"] == False:
                scenario = 4
                # did not choose to purchase the lottery
            elif payoff_ddm["win"] == False:
                scenario = 5
                # open lottery and lose
            else:
                scenario = 6
                # open lottery and win

            return {
                'scenario': scenario,
                'endowment': payoff_ddm["endowment"],
                'pick_round': payoff_ddm["pick_round"],
                'reward': payoff_ddm["reward"],
                'risk': payoff_ddm["risk"],
                'certainty': payoff_ddm["certainty"],
                'payoff': payoff_ddm["payoff"]
            }




page_sequence = [
InitialPage,
FixationPage,
DecisionPage,
AfterPage,
RestPage,
FinishPage
]

# sq1 = [InitialPage, FixationPage, DecisionPage]
# sq2 = [AfterPage, RestPage, FinishPage]
# page_sequence = sq1 + sq2
