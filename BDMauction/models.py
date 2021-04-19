from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import numpy as np
import pandas as pd
import re

author = 'Your name here'

doc = """
Becker-DeGroot-Marschak auction
"""

def lottery_generator(scaler, min_reward, min_risk, reward_lev, risk_lev):

    rewards = []
    risks = []

    counter = 1
    while counter <= reward_lev:
        rewards.append(min_reward)
        min_reward *= scaler
        min_reward = round(min_reward, 2)
        counter += 1

    counter = 1
    while counter <= risk_lev:
        risks.append(min_risk)
        min_risk *= scaler
        min_risk = round(min_risk)
        counter += 1

    lottery_list = []

    for reward in rewards:
        for risk in risks:
            lottery_list.append([reward, risk])

    lottery_table = pd.DataFrame(lottery_list)

    columns = ['reward', 'risk']
    lottery_table.columns = columns

    # lottery_table = lottery_table.sort_values(by=['reward'])

    return lottery_table



def bigger(a, b):
    if a > b:
        return a
    else:
        return b

# def decimal_places(number):
#     x = re.findall(r'\.\d*', str(number))
#     places = len(x[0]) -1
#     return places


class Constants(BaseConstants):
    name_in_url = 'BDMauction'
    players_per_group = None
    num_rounds = 18


#class Subsession(BaseSubsession):
#    pass

    # num_rounds should be 18 when deployed in experiment


class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.session.vars["reward_auc"] = lottery_table['reward']
        self.session.vars["risk_auc"] = lottery_table['risk']

        self.session.vars["min_reward_auc"] = min_reward
        self.session.vars["risk_lev_auc"] = risk_lev


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    WTP = models.FloatField()

    reward = models.FloatField()
    risk = models.FloatField()

    # def WTP_max(self):
    #     ceiling = lottery_table['reward'][self.round_number - 1]
    #     return ceiling
    #
    # def WTP_min(self):
    #     if self.round_number == 1:
    #         floor = 0
    #         return floor
    #
    #     elif lottery_table['reward'][self.round_number - 1] == min_reward:
    #         floor = self.in_round(self.round_number - 1).WTP
    #         return floor
    #
    #     elif self.round_number % risk_lev == 1:
    #         floor = self.in_round(self.round_number - risk_lev).WTP
    #         return floor
    #
    #     else:
    #         floor = bigger(self.in_round(self.round_number - 1).WTP, self.in_round(self.round_number - risk_lev).WTP)
    #         return floor
