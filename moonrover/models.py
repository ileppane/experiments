from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import math

author = 'I Leppanen'

doc = """
BA challenge: Moonrover
"""

def moonroverfun(first,second,third,fourth):

    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    # must modify: each site can be visited only once
    startx = 4
    starty = 6
    x = [9, 8, 8, 7, 7, 7, 5, 2, 1, 4]
    y = [7, 4, 1, 8, 6, 3, 2, 3, 8, 10]
    points = [1, 1, 2, 2, 4, 5, 4, 3, 3, 5]
    sites = ['Plains', 'Boulder', 'Rocks', 'Cliffs', 'Water', 'Fossils', 'Volcano', 'Mountain', 'Crater', 'Electromagnetic']

    ifirst = sites.index(first)
    isecond = sites.index(second)
    ithird = sites.index(third)
    ifourth = sites.index(fourth)

    yourpoints = points[ifirst]

    if isecond is not ifirst:
        yourpoints = yourpoints + points[isecond]

    if ithird is not isecond:
        if ithird is not ifirst:
            yourpoints = yourpoints + points[ithird]

    if ifourth is not ithird:
        if ifourth is not isecond:
            if ifourth is not ifirst:
                yourpoints = yourpoints + points[ifourth]

    yourdist = distance(startx,starty,x[ifirst],y[ifirst]) + distance(x[ifirst],y[ifirst],x[isecond],y[isecond]) + distance(x[isecond],y[isecond],x[ithird],y[ithird]) + distance(x[ithird],y[ithird],x[ifourth],y[ifourth])

    return [yourpoints, yourdist]


class Constants(BaseConstants):
    name_in_url = 'moonrover'
    players_per_group = None
    num_rounds = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    firstsite = models.StringField(choices=['Crater','Electromagnetic','Cliffs','Plains','Water','Boulder','Fossils','Mountain','Volcano','Rocks'])
    secondsite = models.StringField(choices=['Crater','Electromagnetic','Cliffs','Plains','Water','Boulder','Fossils','Mountain','Volcano','Rocks'])
    thirdsite = models.StringField(choices=['Crater','Electromagnetic','Cliffs','Plains','Water','Boulder','Fossils','Mountain','Volcano','Rocks'])
    fourthsite = models.StringField(choices=['Crater','Electromagnetic','Cliffs','Plains','Water','Boulder','Fossils','Mountain','Volcano','Rocks'])
    points = models.IntegerField()