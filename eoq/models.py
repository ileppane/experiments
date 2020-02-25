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
    price = [300,12.5,5] # value of the item, only needed for reference to the holding cost
    ordercost = 5  # per batch
    holdingcost = 2.5 # THIS SHOULD BE IN PROPORTION TO PRICE
    backlogcost = 4*holdingcost # per item per year
    initialinventory = 20 # EOQ should be 89?
    randomdemandgame = 'no' # USE THIS IN CREATING SESSION!

    # Jacobs Chase Example 20.2
    # annual demand 1000
    # daily demand 1000/365
    # ordering cost 5
    # holding cost 1.25 per unit per year ==> this can be larger to drive ave level down
    # price 12.50
    # eoq calculated on yearly basis 89 units

class Subsession(BaseSubsession):

    def before_session_starts(self):
        if Constants.randomdemandgame == 'no':
            self.session.vars['demand'] = [1000]*Constants.num_rounds # annual demand for 365-day year
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
