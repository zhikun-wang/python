# -*-coding:utf-8-*-

from datetime import datetime
import os
from apriori import Apriori
from fpgrowth import FPGrowth

from acrm import apriori as ap

data_set = ap.load_data_set()
print(data_set)

c1 = ap.create_c1(data_set)
print(c1)

d = map(set, data_set)
print(d)

l1, sup_data = ap.scan_d(d, c1, 0.20)
print(l1)
print(sup_data)

print("=========***********============")
l, sp = ap.apriori(data_set, min_support=0.1)
print(l)
print(sp)


def test_apriori(data_set, min_sup = 0.05):
    start = datetime.now()
    apriori = Apriori(data_set)
    re=apriori.generate_L(min_sup=min_sup)
    print(re)
    deltatime = datetime.now() - start
    print("Apriori over")
    return deltatime.seconds + deltatime.microseconds / 1000000
    # print("# of freq itemsets:", len(apriori.freq_itemsets))
    # print(apriori.freq_itemsets)



def test_fpgrowth(data_set, min_sup=0.11):
    start = datetime.now()
    fp = FPGrowth(data_set, min_sup=min_sup)
    fp.build_fptree()
    deltatime = datetime.now() - start
    print("FP-Growth over")
    print("# of freq itemsets:", len(fp.freq_itemsets))

    return deltatime.seconds + deltatime.microseconds / 1000000


print("2 =========***********============")

test_apriori(data_set)

print("3 =========***********============")

test_fpgrowth(data_set)