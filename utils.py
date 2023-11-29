import collections


def sorted_dict_by_key(unsorted_dict):
    return collections.OrderedDict(sorted(unsorted_dict.items(), key=lambda d: d[0]))


def pprint(chains):
    for i, chain in enumerate(chains):
        print(f'{"="*25} chain {i} {"="*25}')
        for k, v in chain.items():
            if k == "transaction":
                print(k)
                for d in v:
                    print(f'{"-"*25}')
                    for kk, vv in d.items():
                        print(f"{kk:30}{vv}")
            print(f"{k:15}{v}")
    print(f'{"*"*25}')
