from statistics import median


def split_male_female(args):
    female_set = {}
    male_set = {}
    for key, item in args.items():
        if item["sex"] == "male":
            male_set[key] = item
        if item["sex"] == "female":
            female_set[key] = item
    return female_set, male_set


def find_median_average(args):
    age_sum = 0
    age_median = {}
    for key, item in args.items():
        age_sum += item["age"]
        age_median[key] = item["age"]
    age_avg = age_sum / len(args)
    age_med_num = median(age_median.values())
    print(f"The average age of this group of people is {age_avg}")
    print(f"The median age of this group of people is {age_med_num}")


def print_values_above(args, num=0):
    if num <= 0:
        print(args)
    for key, item in args.items():
        if item["age"] > num:
            print(item)


def main():
    data_set = {
        1: {"name": "Noam", "age": 26, "sex": "male"},
        2: {"name": "Tal", "age": 25, "sex": "female"},
        3: {"name": "Omri", "age": 37, "sex": "male"}
    }
    female_set, male_set = split_male_female(data_set)
    print(f"These are the males: {male_set}")
    print(f"These are the females: {female_set}")
    find_median_average(data_set)
    print_values_above(data_set)


main()
