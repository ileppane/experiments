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


author = 'IL'

doc = """
Inventory game for OM students
Length = 5 weeks
"""


class Constants(BaseConstants):
    name_in_url = 'eoq'
    players_per_group = None
    instructions_template = 'eoq/Instructions.html'
    num_rounds = 20
    price = 20 # value of the item, only needed for reference to the holding cost; if there are many items, then ABC classification is based on this
    ordercost = 20  # per batch
    holdingcost = 8 # as 40% of price
    backlogcost = 4*holdingcost
    initialinventory = 8


class Subsession(BaseSubsession):

    def before_session_starts(self):
        self.session.vars['demand'] = 40 # demand over all rounds


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    orderquantity = models.PositiveIntegerField(choices=range(11), initial=0)
    onhand = models.FloatField()
    ordercosts = models.FloatField()    # during current round
    holdingcosts = models.FloatField()  # during current round
    backlogcosts = models.FloatField()  # during current round
    servicelevel = models.FloatField()  # during current round
