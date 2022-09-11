from sys import path

path.append('..\\packages')

import extra.iota
print(extra.iota.FunI())

import extra.good.best.sigma as sig #sigma aliased as sig
import extra.good.alpha as alp #alpha aliased as alp

print(sig.FunS())
print(alp.FunA())
