from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, set_time
import random
from random import choice

class InitialPage(Page):

    def is_displayed(self):
        return self.round_number == 1


class FixationPage(Page):

    # timer can be hidden from the page with CSS: https://otree.readthedocs.io/en/latest/timeouts.html#customizing-the-timer
    timeout_seconds = 0.5

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

        reward = self.session.vars["reward_ddm"][self.round_number - 1]
        risk = self.session.vars["risk_ddm"][self.round_number - 1]
        certainty = self.session.vars["certainty_ddm"][self.round_number - 1]
        display = self.session.vars["display_ddm"][self.round_number - 1]

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

    def vars_for_template(self):

        payoff_auc = self.participant.vars['payoff_auc']

        ######
        endowment = 32

        pick_round = choice(range(1, Constants.num_rounds +1))

        reward = self.session.vars["reward_ddm"][pick_round - 1]
        risk = self.session.vars["risk_ddm"][pick_round - 1]
        certainty = self.session.vars["certainty_ddm"][pick_round - 1]
        display = self.session.vars["display_ddm"][pick_round - 1]

        LR = self.player.in_round(pick_round).choice
        if display == 0 and LR == 'left' or display == 1 and LR == 'right':
            # lottery is chosen
            proceed = True
        else:
            proceed = False

        dice = random.randint(1, 100)
        if dice <= risk:
            win = True
            payoff = endowment - certainty + reward
        else:
            win = False
            payoff = endowment - certainty

        payoff_ddm = {"endowment": endowment, "pick_round": pick_round, "reward": reward, "risk": risk, "certainty": certainty, "proceed": proceed, "win": win, "payoff": payoff}

        # # Just to test the program
        # treatment = 'auc'
        # treatment = 'ddm'

        treatment = choice(['auc','ddm'])

        # record the payoff info
        if treatment == 'auc':
            payoff_auc["treatment"] = "auc"
            self.player.pay = str(payoff_auc)
        else:
            payoff_ddm["treatment"] = "ddm"
            self.player.pay = str(payoff_ddm)

        # scenario verdict
        if treatment == 'auc':
            # payoff to be chosen from the treatment 1
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

        # payoff to be chosen from the treatment 2
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



        # return {
        #     'payoff_auc': payoff_auc,
        #     'payoff_ddm': payoff_ddm
        #
        # }



# page_sequence = [InitialPage, DecisionPage, RestPage, FinishPage]

page_sequence = [InitialPage, FixationPage, DecisionPage, RestPage, FinishPage]
