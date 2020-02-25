from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

author = 'IL'

doc = """
Inventory game for OM students
"""


class Constants(BaseConstants):
    name_in_url = 'eoq'
    players_per_group = None
    instructions_template = 'eoq/Instructions.html'
    num_rounds = 30 # days
    price = [300,20,5] # value of the item, only needed for reference to the holding cost
    ordercost = 20  # per batch
    holdingcost = 8 # as 40% of price
    backlogcost = 4*holdingcost # per item per year
    initialinventory = 100 # EOQ should be 89?
    randomdemandgame = 'no' # USE THIS IN CREATING SESSION!
    # class B item price should be 20, C item 5 and A item 300


class Subsession(BaseSubsession):

    def before_session_starts(self):
        if Constants.randomdemandgame == 'no':
            self.session.vars['demand'] = [1277.5]*Constants.num_rounds # aver annual demand for 365-day year
#        else:
#            self.session.vars['demand'] = [40,60,30, ...


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    Q = models.PositiveIntegerField(choices=range(11), initial=0) # order quantity
    I = models.FloatField()     # onhand inventory
    oc = models.FloatField()    # ordercost during current round
    hc = models.FloatField()    # holdingcost during current round
    bc = models.FloatField()    # backlog during current round
    servicelevel = models.FloatField()  # during current round
