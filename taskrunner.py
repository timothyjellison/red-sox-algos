from algos import cointoss, mascotferocity
from utils.teams import *


def winOrLoss(bool):
    if bool:
        return "Win"
    else:
        return "Loss"


print("Cointoss:", winOrLoss(cointoss.main()))
print("Mascot Ferocity:", winOrLoss(mascotferocity.main(ATLANTA_BRAVES)))
