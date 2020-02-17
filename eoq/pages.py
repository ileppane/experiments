from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StartPage(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self): # initialises first round holding and order cost, these are written over before first round ends
        self.player.holdingcosts = 0
        self.player.ordercosts = 0

class MyPage(Page):

#    timeout_seconds = 10

    form_model = 'player'
    form_fields = ['orderquantity']

    def vars_for_template(self):

        demand = self.session.vars['demand'] / Constants.num_rounds # demand for this round

        if self.round_number == 1:
            prevorder = 0
        else:
            prevorder = self.player.in_round(self.round_number - 1).orderquantity

        onhandlist = [Constants.initialinventory]
        i = 1
        totalholdingcosts = (Constants.holdingcost)*(Constants.initialinventory)
        totalordercosts = 0
        while i < self.round_number:
            onhandlist.append(self.player.in_round(i).onhand)
            totalholdingcosts += self.player.in_round(i).holdingcosts
            totalordercosts += self.player.in_round(i).ordercosts
            i += 1

        onhand = onhandlist[self.round_number-1]

        return {
            'prevorder': prevorder,
            'onhandlist': onhandlist,
            'onhand': onhand,
            'demand': demand,
            'totalholdingcosts': totalholdingcosts,
            'totalordercosts': totalordercosts
        }

    def before_next_page(self):

        if self.player.orderquantity > 0:
            self.player.ordercosts = Constants.ordercost
        else:
            self.player.ordercosts = 0

        weekdemand = self.session.vars['demand'] / Constants.num_rounds

        if self.round_number == 1:
            self.player.onhand = Constants.initialinventory + self.player.orderquantity - weekdemand
        else:
            self.player.onhand = self.player.in_round(self.round_number - 1).onhand + self.player.orderquantity - weekdemand

        if self.player.onhand > 0:
            self.player.holdingcosts = (self.player.onhand)*(Constants.holdingcost)
        else:
            self.player.holdingcosts = 0


class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds



page_sequence = [StartPage, MyPage, Results]
