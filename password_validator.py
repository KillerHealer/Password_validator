from collections import defaultdict
# A1
s = "mvnlskjhlasdkjnfmlkjsaf"
d = {}
for char in s:
    d[char] = d.get(char, 0) + 1


print(sorted(d.items()))
# A2
reverseDict = defaultdict(list)
{reverseDict[v].append(k) for k, v in d.items()}
result = dict(reverseDict)
print(result)
# B1
l1 = [1, 2, 3, 3, 4, 5, 6, 7]
l2 = [2, 4, 12, 31, 21]
l3 = [54, 34, 23, 4, 2]
all_lst_dict = {"l1": l1, "l2": l2, "l3": l3}
fit_dic = {}
for name, lst in all_lst_dict.items():
    tmp_set = set(lst)
    if len(tmp_set) != len(lst):
        fit_dic[name] = tmp_set
        print(f"the list {lst} has at least one repeating items")
print()
# B2
common_values = set.intersection(*fit_dic.values())
print("B:")
print(common_values, " ".join(fit_dic.keys()))
print()
# C1
lastl = [31, 99, 3, 1943]
x1 = []
for item in lastl:
    x1.append([int(a) for a in str(item)])
res1 = []
for item in x1:
    for item2 in item:
        res1.append(item2)
res1 = set(res1)
sort_order = "desc"
if sort_order == "desc":
    print(sorted(res1, reverse=True))
if sort_order == "asc":
    print(sorted(res1))
