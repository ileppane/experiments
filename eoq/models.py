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
    price = [300, 12.5, 5] # value of the item, only needed for reference to the holding cost
    ordercost = 5  # per batch
    holdingcost = [120, 5, 2] # THIS SHOULD BE 40% OF PRICE
    backlogcost = [480, 20, 8] # 4x holdingcost, per item per year
    initialinventory = 20 # same for all?
    randomdemandgame = 'no' # USE THIS IN CREATING SESSION!
    simple = 'no' # yes: only item B, no: all items

    # EOQ's
    # A: 9
    # B: 44
    # C: 70

    # Jacobs Chase Example 20.2

class Subsession(BaseSubsession):

    def before_session_starts(self):
        if Constants.randomdemandgame == 'no':
            self.session.vars['demandA'] = [1000]*Constants.num_rounds # annual demand for 365-day year
            self.session.vars['demandB'] = [1000] * Constants.num_rounds  # annual demand for 365-day year
            self.session.vars['demandC'] = [1000] * Constants.num_rounds  # annual demand for 365-day year
#        else:
#            self.session.vars['demand'] = [


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    QA = models.PositiveIntegerField(choices=range(101), initial=0) # order quantity
    QB = models.PositiveIntegerField(choices=range(101), initial=0) # order quantity
    QC = models.PositiveIntegerField(choices=range(101), initial=0) # order quantity
    IA = models.FloatField()     # onhand inventory
    IB = models.FloatField()     # onhand inventory
    IC = models.FloatField()     # onhand inventory
    ocA = models.FloatField()    # ordercost during current round
    hcA = models.FloatField()    # holdingcost during current round
    bcA = models.FloatField()    # backlog during current round
    ocB = models.FloatField()  # ordercost during current round
    hcB = models.FloatField()  # holdingcost during current round
    bcB = models.FloatField()  # backlog during current round
    ocC = models.FloatField()  # ordercost during current round
    hcC = models.FloatField()  # holdingcost during current round
    bcC = models.FloatField()  # backlog during current round
#    servicelevel = models.FloatField()  # during current round
