from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = 'player'
    form_fields = ['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy']

class Results(Page):

    def vars_for_template(self):

        correct = ""
        points = 0
        if (self.player.Emily == "Jack"):
            correct = correct + "Jack with Emily\n "
            points = points + 1
        if (self.player.Megan == "Thomas"):
            correct = correct + "Thomas with Megan\n"
            points = points + 1
        if (self.player.Olivia == "James"):
            correct = correct + "James with Olivia\n"
            points = points + 1
        if (self.player.Lucy == "Joshua"):
            correct = correct + "Joshua with Lucy\n"
            points = points + 1
        if (self.player.Sophie == "Daniel"):
            correct = correct + "Daniel with Sophie\n"
            points = points + 1
        if (self.player.Chloe == "Harry"):
            correct = correct + "Harry with Chloe\n"
            points = points + 1
        if (self.player.Jessica == "Samuel"):
            correct = correct + "Samuel with Jessica\n"
            points = points + 1
        if (self.player.Hannah == "Joseph"):
            correct = correct + "Joseph with Hannah\n"
            points = points + 1
        if (self.player.Lauren == "Matthew"):
            correct = correct + "Matthew with Lauren\n"
            points = points + 1
        if (self.player.Charlotte == "Callum"):
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
