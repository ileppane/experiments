from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, set_time, profit, revenue, cost


class WelcomePage(Page):

    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = ['prolificcode']


class StartPage(Page):

    def is_displayed(self):
        return self.round_number == 1 or self.round_number == 21

    def vars_for_template(self):
        if self.player.round_number < 21:
            partnumber = 'one'
            costparam = 3 # ASSUME HIGH MARGIN (LOW COST PRODUCT) FIRST
            optq = 225

        else:
            partnumber = 'two'
            costparam = 9
            optq = 75

        return {
            'costparam': costparam,
            'part': partnumber,
            'nvframe': Constants.nvframe,
            'optq': optq # not needed if profitcalculator commented off
        }


class Practice(Page): # page that tells that practice rounds are over

    def is_displayed(self):
        return self.round_number == 6


class PreDecision(Page):

    timeout_seconds = 1

    def before_next_page(self):
        self.player.starttime = set_time()


class Decide(Page):

    form_model = 'player'
    form_fields = ['q', 'jsdectime_start', 'jsdectime_end']

    def vars_for_template(self):

        if self.player.round_number < 6:
            practice = 'yes'
        else:
            practice = 'no'

        if self.player.round_number < 21: # high margin is first
            costparam = 3
            margin = 'high'

        else:
            costparam = 9
            margin = 'low'

        if margin == 'high':
            optq = 225
        else:
            optq = 75

        return {
            'practice': practice,
            'practiceround': self.player.round_number,
            'round': self.player.round_number-5,
            'margin': margin,
            'costparam': costparam,
            'inittotalcost': 150 * costparam,
            'iswelcomepage': False,
            'optq': optq,
            'nvframe': Constants.nvframe

        }

    def before_next_page(self):
        if self.player.round_number < 21:
            margin = 'high'
        else:
            margin = 'low'

        self.player.d = self.session.vars['d'][self.round_number - 1]
        self.player.payoff = round(profit(self.player.d, self.player.q, margin),0)
        self.player.revenue = revenue(self.player.d, self.player.q)
        self.player.cost = cost(self.player.q, margin)
        self.player.endtime = set_time()
        self.player.fakeround_number = self.player.round_number-5


class Results(Page):

    def vars_for_template(self):

        if self.player.round_number < 6:
            practice = 'yes'
        else:
            practice = 'no'

        if self.player.round_number > 6:
            actualroundlist = self.player.in_rounds(6, self.player.round_number)
        else:
            actualroundlist = range(1,2)

        if self.player.round_number < 6:
            practice = 'yes'

        if self.player.round_number < 21: # high margin is first
            costparam = 3
            margin = 'high'
        else:
            costparam = 9
            margin = 'low'

        if margin == 'high':
            optq = 225
        else:
            optq = 75

        d = self.session.vars['d'][self.round_number-1]

        if Constants.nvframe == 'yes':
            if (d < self.player.q):
                demandtext = "Demand was smaller than your inventory: you have leftovers that do not bring you any profit"
            elif (d > self.player.q):
                demandtext = "Demand was larger than your inventory: you could not satisfy all the customer demand"
            else:
                demandtext = "Demand exactly matched your inventory"
        else:
            if (d < self.player.q):
                demandtext = "The red circle was smaller than your blue circle"
            elif (d > self.player.q):
                demandtext = "The red circle was larger than your blue circle"
            else:
                demandtext = "The red circle was exactly the same size as your blue circle"


        if round(self.player.payoff,0) >= 0:
            profitloss = 'You made a profit of ' + str(round(self.player.payoff,0))
        else:
            profitloss = 'You made a loss of ' + str(-round(self.player.payoff,0))

        return {
            'practice': practice,
            'practiceround': self.player.round_number,
            'round': self.player.round_number-5,
            'actualroundlist': actualroundlist,
            'roundlist': self.player.in_all_rounds,
            'margin': margin,
            'q': self.player.q,
            'd': d,
            'costi': self.player.q * costparam,
            'reve': round(self.player.payoff, 0) + self.player.q * costparam,
            'profit': round(self.player.payoff,0),
            'player_in_all_rounds': self.player.in_all_rounds(),
            'demandtext': demandtext,
            'costparam': costparam,
            'iswelcomepage': False,
            'profitloss': profitloss,
            'optq': optq,
            'nvframe': Constants.nvframe
        }


class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == 35

    form_model = 'player'
    form_fields = ['pecu', 'nonpecu', 'conflict']

    def vars_for_template(self):

        totpay = 0
        for p in self.player.in_rounds(6,35):
            totpay += p.payoff

        return {
            'averagepay': totpay/30,
            'monetary': 0,
        }


class FinalFinalPage(Page):

    def is_displayed(self):
        return self.round_number == 35

    def vars_for_template(self):
        return {
            'prolificurl': self.session.config['prolificurl']
        }

page_sequence = [WelcomePage, StartPage, Practice, PreDecision, Decide, Results, FinalPage, FinalFinalPage]
