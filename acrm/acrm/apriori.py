# -*-coding:utf-8-*-
import sys

print("begin run ", sys.version)


def load_data_set():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def create_c1(ds):
    c = []
    for transaction in ds:
        for item in transaction:
            if not [item] in c:
                c.append([item])

    c.sort()
    return map(frozenset, c)


def scan_d(d, ck, min_support):
    ss_cnt = {}
    for tid in d:
        for can in ck:
            if can.issubset(tid):
                if can in ss_cnt:
                    ss_cnt[can] += 1
                else:
                    ss_cnt[can] = 1

    num_items = float(len(d))
    re_lists = []
    support_data = {}
    for key in ss_cnt:
        support = ss_cnt[key] / num_items
        if support >= min_support:
            re_lists.insert(0, key)
        support_data[key] = support

    return re_lists, support_data


def apriori_gen(lk, k):
    re_list = []
    len_lk = len(lk)
    for i in range(len_lk):
        for j in range(i + 1, len_lk):
            l1 = list(lk[i])[:k - 2]
            l2 = list(lk[j])[:k - 2]
            l1.sort()
            l2.sort()
            if l1 == l2:
                re_list.append(lk[i] | lk[j])

    return re_list


def apriori(ds, min_support=0.1):
    c1 = create_c1(ds)
    d = map(set, ds)
    l1, support_data = scan_d(d, c1, min_support)
    re_l = [l1]
    k = 2
    while (len(re_l[k - 2]) > 0):
        ck = apriori_gen(re_l[k - 2], k)
        lk, sup_k = scan_d(d, ck, min_support)
        support_data.update(sup_k)
        re_l.append(lk)
        k += 1
    return re_l, support_data
