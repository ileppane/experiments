from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, consensus2
import csv, pandas


class FirstPage(Page):

    form_fields = ['code']


class MyPage(Page):

    form_fields = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']

    def before_next_page(self):
        df = pandas.read_csv('output.csv')
        df.set_index = 'id'
        newdf = df.loc[df['id'] == self.player.code]
        grouppi = newdf.iloc[-1][1]
        data = [[self.player.code, grouppi,
                 self.player.p1, self.player.p2, self.player.p3, self.player.p4, self.player.p5, self.player.p6]]
        newdfrow = pandas.DataFrame(data, columns=['id', 'group', 'project1', 'project2',
                                                   'project3', 'project4', 'project5', 'project6'])
        newdfrow.to_csv('output.csv', mode='a', header=None, index=False)


class Results(Page):

    def vars_for_template(self):
        cons = consensus2(self.player.code)

        return {
            'consensus': cons
        }


page_sequence = [
    FirstPage,
    MyPage,
    Results
]
