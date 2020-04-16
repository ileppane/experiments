from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import math, numpy


class InitialPage(Page):

    timeout_seconds = -1

    def before_next_page(self):

        if self.round_number == 1:
            locx = 0
            locy = 0

        else:
            locx = self.player.in_round(self.round_number - 1).x
            locy = self.player.in_round(self.round_number - 1).y

        xcoord = numpy.ceil(numpy.random.normal(locx, 30))
        ycoord = numpy.ceil(numpy.random.normal(locy, 30))

        if xcoord > 150:
            xcoord = 150

        if xcoord < -150:
            xcoord = -150

        if ycoord > 150:
            ycoord = 150

        if ycoord < -150:
            ycoord = -150

        self.player.xcoord = xcoord
        self.player.ycoord = ycoord
        self.player.score = math.sqrt(xcoord*xcoord + ycoord*ycoord)


class MyPage(Page):

    form_model = 'player'
    form_fields = ['x','y']

    def vars_for_template(self):

        allycoord = [0]
        allxcoord = [0]

        cumulativescore = 0
        i = 1
        while i < self.round_number:
            allxcoord.append(self.player.in_round(i).xcoord)
            allycoord.append(self.player.in_round(i).ycoord)
            cumulativescore += self.player.in_round(i).score
            i += 1

        if self.round_number == 1:
            prevx = 0
            prevy = 0
        else:
            prevx = self.player.in_round(i - 1).x
            prevy = self.player.in_round(i - 1).y

        return {
            'allxcoord': allxcoord,
            'allycoord': allycoord,
            'round': self.player.round_number,
            'prevx': prevx,
            'prevy': prevy,
            'cumulativescore': cumulativescore
        }


class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [InitialPage, MyPage, Results]
