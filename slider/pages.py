from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, profit, revenue, cost


class DecideOrderQuantity(Page):

    form_model = 'player'
    form_fields = ['q']

    def vars_for_template(self):

        if self.session.config['margin'] == 'low':
            costparam = 9
        else:
            costparam = 3

        return {
            'round': self.player.round_number,
            'margin': self.session.config['margin'],
            'costparam': costparam,
            'iswelcomepage': False
        }

    def before_next_page(self):
        self.player.d = self.session.vars['d'][self.round_number - 1]
        self.player.payoff = round(profit(self.player.d, self.player.q, self.session.config['margin']),0)
        self.player.revenue = revenue(self.player.d, self.player.q)
        self.player.cost = cost(self.player.q, self.session.config['margin'])


class Results(Page):

    def vars_for_template(self):

        if self.session.config['margin'] == 'low':
            costparam = 9
        else:
            costparam = 3

        d = self.session.vars['d'][self.round_number-1]

        if (d < self.player.q):
            demandtext = "Demand was smaller than your inventory: you have leftovers that do not bring you any profit"
        elif (d > self.player.q):
            demandtext = "Demand was larger than your inventory: you could not satisfy all the customer demand"
        else:
            demandtext = "Demand exactly matched your inventory"

        return {
            'round': self.player.round_number,
            'margin': self.session.config['margin'],
            'q': self.player.q,
            'd': d,
            'profit': round(self.player.payoff,0),
            'player_in_all_rounds': self.player.in_all_rounds(),
            'demandtext': demandtext,
            'costparam': costparam,
            'iswelcomepage': False
        }


class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        if (self.session.config['margin'] == 'low'):
            baselinereward = '0.12'

        else:
            baselinereward = '0.20'

        return {
            'averagepay': self.participant.payoff/Constants.num_rounds,
            'reward': self.player.payoff,
            'baselinereward': baselinereward
        }


page_sequence = [
    DecideOrderQuantity,
    Results,
    FinalPage
]
