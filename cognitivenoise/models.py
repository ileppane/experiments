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
from timeit import default_timer as timer

import numpy as np
import pandas as pd


author = 'Your name here'

doc = """
App with decision task, to come after elicitation task
"""


def set_time():

    time_now = timer()

    return time_now

def trial_generator(scaler, min_reward, min_risk, reward_lev, risk_lev, m_values):

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

    mode1 = [0,1,0]
    mode2 = [1,0,1]
    mode_use = 1
    trial_list = []
    for reward in rewards:
        for risk in risks:
            for m in m_values:
                if risk < 50:
                    devider = (2 ** 1.5) ** (m / 4)
                elif risk < 70:
                    devider = 2 ** (m / 4)
                else:
                    devider = (2 ** 0.5) ** (m / 4)

                certainty = round(reward / devider, 2)

                if mode_use == 1:
                    for display in range(3):
                        trial_list.append([reward, risk, certainty, mode1[display]])
                    mode_use += 1
                else:
                    for display in range(3):
                        trial_list.append([reward, risk, certainty, mode2[display]])
                    mode_use -= 1

    trial_table = pd.DataFrame(trial_list)

    columns = ['reward', 'risk', 'certainty', 'display']
    trial_table.columns = columns

    np.random.seed(123456)
    trial_table = trial_table.sample(frac=1).reset_index(drop=True)

    return trial_table

scaler = 2**0.5
min_reward = 7.85
min_risk = 41
reward_lev = 4
risk_lev = 3
m_values = list(range(0,9))

trial_table = trial_generator(scaler, min_reward, min_risk, reward_lev, risk_lev, m_values)


class Constants(BaseConstants):
    name_in_url = 'cognitivenoise'
    players_per_group = None
    num_rounds = 10
    # num_rounds should be changed to 324 when deployed in experiment

    # instructions_template = 'cognitivenoise/Instructions.html'
    # In a template: "You can write the instructions on a template file and include here using the below line: {% include Constants.instructions_template %}"


class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.session.vars["reward_ddm"] = trial_table['reward']
        self.session.vars["risk_ddm"] = trial_table['risk']
        self.session.vars["certainty_ddm"] = trial_table['certainty']
        self.session.vars["display_ddm"] = trial_table['display']


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    choice = models.StringField()
    dectime = models.FloatField()

    reward = models.FloatField()
    risk = models.FloatField()
    certainty = models.FloatField()
    display = models.IntegerField()

    pay = models.LongStringField()
