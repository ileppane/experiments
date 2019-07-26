from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, moonroverfun


class MyPage(Page):
    form_model = 'player'
    form_fields = ['firstsite','secondsite','thirdsite','fourthsite']

# Water->Boulder->Fossils->Volcano
class Results(Page):

    def vars_for_template(self):

        [yourpoints, yourdist] = moonroverfun(self.player.firstsite, self.player.secondsite, self.player.thirdsite, self.player.fourthsite)

        if yourdist > 10:
            text = "Unfortunately your distance was longer than 10 km, and your answer cannot be accepted."
        else:
            text = "Your distance was within the 10 km limit of the moonrover, therefore your answer is accepted."

        return {
            'text': text,
            'dist': yourdist,
            'points': yourpoints
        }


page_sequence = [
    MyPage,
    Results
]
