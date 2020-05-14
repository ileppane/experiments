from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, moonroverfun


class MyPage(Page):
    form_model = 'player'
    form_fields = ['startx','starty','firstsite','secondsite','thirdsite','fourthsite']

    def before_next_page(self):

        [yourpoints, yourdist] = moonroverfun(self.player.startx, self.player.starty, self.player.firstsite, self.player.secondsite, self.player.thirdsite, self.player.fourthsite)

        if yourdist > 20.3:
            self.player.points = 0
        else:
            self.player.points = yourpoints

class Results(Page):

    def vars_for_template(self):

        [yourpoints, yourdist] = moonroverfun(self.player.startx, self.player.starty, self.player.firstsite, self.player.secondsite, self.player.thirdsite, self.player.fourthsite)

        text2 = ""
        if yourdist > 20.3:
            text = 'Unfortunately the distance was more than allowed for the drone, therefore your answer cannot be accepted. Go ahead and try again.'
        else:
            if yourpoints < 15 and yourpoints > 9:
                text = "Close! The maximum profit you could achieve is XX. Go ahead and try again!"
            elif yourpoints <= 9:
                text = "You could do better, go ahead and try again!"
            else:
                text = "Congratulations! You achieved the maximum profit."
                text2 = "Interested in how you could use these sorts of data skills in a business career? Read section below and sign up to our next Open Day."

        return {
            'startx': self.player.startx,
            'starty': self.player.starty,
            'firstsite': self.player.firstsite,
            'secondsite': self.player.secondsite,
            'thirdsite': self.player.thirdsite,
            'fourthsite': self.player.fourthsite,
            'text': text,
            'text2': text2,
            'dist': yourdist,
            'points': yourpoints
        }


page_sequence = [
    MyPage,
    Results
]
