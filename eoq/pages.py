from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StartPage(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self): # initialises first round holding and order cost, these are written over before first round ends
        self.player.hc = 0
        self.player.oc = 0
        self.player.bc = 0

class MyPage(Page):

#    timeout_seconds = 10

    form_model = 'player'
    form_fields = ['Q']

    def vars_for_template(self):

        if self.round_number == 1:
            prevQ = 0
        else:
            prevQ = self.player.in_round(self.round_number - 1).Q

        D = self.session.vars['demand'][self.round_number - 1] / 365  # demand for this round

        allI = [Constants.initialinventory]
        i = 1
        [thc, toc, tbc] = [(Constants.holdingcost)*(Constants.initialinventory), 0, 0]  # tot. costs
        while i < self.round_number:
            allI.append(self.player.in_round(i).I)
            thc += self.player.in_round(i).hc
            toc += self.player.in_round(i).oc
            tbc += self.player.in_round(i).bc
            i += 1

        # DETERMINE AVERAGE SERVICE LEVEL

        return {
            'priceA': Constants.price[0],
            'priceB': Constants.price[1],
            'priceC': Constants.price[2],
            'prevQ': prevQ,
            'allI': allI,
            'I': allI[self.round_number-1],
            'D': D,
            'thc': thc,
            'toc': toc,
            'tbc': tbc,
            'holdingcostpx': str(thc/(thc + toc + tbc) * 100)+"%",
            'orderingcostpx': str(toc / (thc + toc + tbc) * 100) + "%",
            'backlogcostpx': str(tbc / (thc + toc + tbc) * 100) + "%"
        }

    def before_next_page(self):

        if self.player.Q > 0:
            self.player.oc = Constants.ordercost
        else:
            self.player.oc = 0

        D = self.session.vars['demand'][self.round_number - 1] / 365

        if self.round_number == 1:
            self.player.I = Constants.initialinventory + self.player.Q - D
        else:
            self.player.I = self.player.in_round(self.round_number - 1).I + self.player.Q - D

        self.player.hc = max([(self.player.I)*(Constants.holdingcost), 0])
        self.player.bc = max([(-1)*(self.player.I)*(Constants.backlogcost), 0])

#       self.player.servicelevel =


class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [StartPage, MyPage, Results]