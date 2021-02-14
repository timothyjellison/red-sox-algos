from teams import *

ferocity_index = {
    ATLANTA_BRAVES: 1,
    MIAMI_MARLINS: 1,
    PHILADELPHIA_PHILLIES: 1,
    CHICAGO_CUBS: 1,
    PITTSBURGH_PIRATES: 1,
    ARIZONA_DIAMONDBACKS: 1,
    LOS_ANGELES_ANGELS: 1,
    DETROIT_TIGERS: 1,
    TAMPA_BAY_RAYS: 1,
    CLEVELAND_INDIANS: 1,
    SAN_FRANCISCO_GIANTS: 1,
    OAKLAND_ATHLETICS: 1,
    COLORADO_ROCKIES: 1,
    TEXAS_RANGERS: 1,
    BOSTON_RED_SOX: 0.5,
    CINCINNATI_REDS: 0,  # red socks beat the abstract color red
    CHICAGO_WHITE_SOX: 0,  # red socks beat white socks
    LOS_ANGELES_DODGERS: 0,  # their whole thing is avoiding confrontation
    MILWAUKEE_BREWERS: 0,  # peaceful occupation
    ST_LOUIS_CARDINALS: 0,  # birds are dumb
    BALTIMORE_ORIOLES: 0,  # birds are dumb
    TORONTO_BLUE_JAYS: 0,  # birds are dumb
    NEW_YORK_METS: 0,  # congrats you live in a metropolis
    WASHINGTON_NATIONALS: 0,  # what is a national?
    HOUSTON_ASTROS: 0,  # what is an astro?
    MINNESOTA_TWINS: 0,  # twin what?
    KANSAS_CITY_ROYALS: 0,  # this is america
    SEATTLE_MARINERS: 0,  # peaceful occupation
    SAN_DIEGO_PADRES: 0,  # relatively peaceful occupation / dads
    NEW_YORK_YANKEES: 0,  # yankees suck obviously
}


def main(opponent):
    return ferocity_index[opponent] < ferocity_index[BOSTON_RED_SOX]
