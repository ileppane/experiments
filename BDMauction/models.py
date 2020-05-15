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
import time

author = 'Your name here'

doc = """
Your app description
"""

def lottery_generator(scaler, min_reward, min_risk, reward_lev, risk_lev, treatment):

    rewards = []
    risks = []

    counter = 1
    if treatment == 'A':
        while counter <= reward_lev:
            rewards.append(min_reward)
            min_reward *= scaler
            min_reward = round(min_reward, 2)
            counter += 1
    else:
        while counter <= reward_lev:
            rewards.append(round(min_reward))
            min_reward *= scaler
            min_reward = round(min_reward, 2)
            counter += 1

    counter = 1
    if treatment == 'A':
        while counter <= risk_lev:
            risks.append(min_risk)
            min_risk *= scaler
            min_risk = round(min_risk)
            counter += 1
    else:
        while counter <= risk_lev:
            risks.append(round(min_risk / 10) * 10)
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

# The valus of these variables need to be kept same with those in the page.py
scaler = 2**0.5
min_reward = 7.85
min_risk = 41
reward_lev = 4
risk_lev = 3


def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def decimal_places(number):
    x = re.findall(r'\.\d*', str(number))
    places = len(x[0]) -1
    return places


class Constants(BaseConstants):
    name_in_url = 'BDMauction'
    players_per_group = None
    num_rounds = 3
    # num_rounds should be 12 when deployed in experiment


class Subsession(BaseSubsession):
    def before_session_starts(self):

        self.session.vars['treatment'] = np.random.choice(['A','E'])

        # t = 1000 * time.time() # current time in milliseconds
        # self.session.vars['seed'] = int(t) % 2**32

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    treatment = models.StringField()

    WTP = models.FloatField()

    reward = models.FloatField()
    risk = models.FloatField()

    floor = models.FloatField()

    def WTP_max(self):

        # ceiling = self.reward

        treatment = self.session.vars["treatment"]
        # treatment = random.choice(['A','E'])
        # treatment = 'A'
        # treatment = 'E'

        lottery_table = lottery_generator(scaler, min_reward, min_risk, reward_lev, risk_lev, treatment)

        ceiling = lottery_table['reward'][self.round_number - 1]

        return ceiling

    def WTP_min(self):

        treatment = self.session.vars["treatment"]
        # treatment = random.choice(['A','E'])
        # treatment = 'A'
        # treatment = 'E'

        lottery_table = lottery_generator(scaler, min_reward, min_risk, reward_lev, risk_lev, treatment)

        reward = lottery_table['reward'][self.round_number - 1]
        # risk = lottery_table['risk'][self.round_number - 1]

        if self.round_number == 1:
            floor = 0
            return floor
        elif reward == min_reward or reward == round(min_reward):
            floor = self.in_round(self.round_number - 1).WTP
            return floor
        elif self.round_number % risk_lev == 1:
            floor = self.in_round(self.round_number - risk_lev).WTP
            return floor
        else:
            floor = bigger(self.in_round(self.round_number - 1).WTP, self.in_round(self.round_number - risk_lev).WTP)
            return floor


    def WTP_error_message(self, value):

        if decimal_places(value) > 2:
            return "your specified price cannot have a unit smaller than $0.01."
