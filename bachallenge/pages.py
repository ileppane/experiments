from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class WelcomePage(Page):
    form_model = 'player'
    form_fields = ['appchoice']


class MyPage(Page):
    form_model = 'player'
    form_fields = ['name']

    # https://otree.readthedocs.io/en/latest/pages.html#app-after-this-page
    def app_after_this_page(self, upcoming_apps):
        if self.player.appchoice == 'Dating App':
            return "datingapp"
        elif self.player.appchoice == 'Digital Marketing':
            return "digitalmarketing"
        elif self.player.appchoice == 'Moonrover':
            return "moonrover"

    def before_next_page(self):

        self.participant.vars['username'] = self.player.name


page_sequence = [
    WelcomePage,
    MyPage
]
