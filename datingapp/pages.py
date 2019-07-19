from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['Jack','Thomas','James','Joshua','Daniel','Harry','Samuel','Joseph','Matthew','Callum']


class Results(Page):

    def vars_for_template(self):

        correct = ""
        points = 0
        if (self.player.Jack == "Emily"):
            correct = correct + "Jack with Emily\n "
            points = points + 1
        if (self.player.Thomas == "Megan"):
            correct = correct + "Thomas with Megan\n"
            points = points + 1
        if (self.player.James == "Olivia"):
            correct = correct + "James with Olivia\n"
            points = points + 1
        if (self.player.Joshua == "Lucy"):
            correct = correct + "Joshua with Lucy\n"
            points = points + 1
        if (self.player.Daniel == "Sophie"):
            correct = correct + "Daniel with Sophie\n"
            points = points + 1
        if (self.player.Harry == "Chloe"):
            correct = correct + "Harry with Chloe\n"
            points = points + 1
        if (self.player.Samuel == "Jessica"):
            correct = correct + "Samuel with Jessica\n"
            points = points + 1
        if (self.player.Joseph == "Hannah"):
            correct = correct + "Joseph with Hannah\n"
            points = points + 1
        if (self.player.Matthew == "Lauren"):
            correct = correct + "Matthew with Lauren\n"
            points = points + 1
        if (self.player.Callum == "Charlotte"):
            correct = correct + "Callum with Charlotte\n"
            points = points + 1

        if (correct == ""):
            correct = "You did not have any correct matches."

        return {
            'correct': correct,
            'points': points
        }


page_sequence = [
    MyPage,
    Results
]
