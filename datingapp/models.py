from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Ilkka Leppanen'

doc = """
Challenges for prospective BA students: Dating App
"""


class Constants(BaseConstants):
    name_in_url = 'datingapp'
    players_per_group = None
    num_rounds = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField()
    Jack = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    Thomas = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    James = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    Joshua = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    Daniel = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    Harry = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    Samuel = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    Joseph = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    Matthew = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])
    Callum = models.StringField(choices=['Chloe','Emily','Megan','Charlotte','Jessica','Lauren','Sophie','Olivia','Hannah','Lucy'])