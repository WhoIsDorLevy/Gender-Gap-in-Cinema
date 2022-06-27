import os
import csv
import json
from collections import Counter


def read_tsv(path):
    with open(path, encoding="utf-8") as file:
        file = csv.reader(file, delimiter="\t")
        dict = {}
        # counter = 0
        for row in file:
            category = row[3]
            characters = row[5]
            if category == "actor":
                tmp = dict.setdefault(characters, [0, 0])
                dict[characters][0] = tmp[0] + 1
            if category == "actress":
                tmp = dict.setdefault(characters, [0, 0])
                dict[characters][1] = tmp[1] + 1
            # counter += 1
            # if counter == 1000:
            #     break
        return dict


def write_dict_to_json(dict, name):
    with open(os.path.join("resources", name), 'w') as out_file:
        json.dump(dict, out_file)


def read_jsonfile_to_dic(name):
    with open(os.path.join("resources", name), 'r') as file:
        return json.load(file)


def unit_roles(roles, dic):
    s = list(filter(lambda item: same(item, roles), dic.items()))
    actors = [sum([item[1][0] for item in s]), sum([item[1][1] for item in s])]
    return actors


def same(item, roles):
    for role in roles:
        if role.lower() in item[0].lower():
            return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    
    

    # #step1
    # mypath = os.getcwd()
    # os.chdir("..")
    # data_path = os.getcwd() + "\\title.principals.tsv\\data.tsv"
    # dict = read_tsv(data_path)

    

    # #step2 - set things up and get total representation of men and women
    # os.chdir(mypath)  # return to the origin path
    # write_dict_to_json(dict, "dict_before_filter.json")
    dic = read_jsonfile_to_dic("dict_before_filter.json")
    total_men = 0
    total_women = 0
    for lst in dic.values():
        total_men += lst[0]
        total_women += lst[1]
    total_occupation = {"Men": total_men, "Women": total_women}
    write_dict_to_json(total_occupation, "total_occupation.json")
    # step3 - write file of top roles with number of actors and actresses
    # dic = read_jsonfile_to_dic("dict_before_filter.json")
    # role_list = {"Doctor":["dr.", "doctor"],
    #             "Professor" : ["professor","prof."],
    #             "Detective":["detective","det."],
    #             "Agent" :["agent"],
    #             "Student": ["student"],
    #             "Policeman/Policewoman":["policewoman","policeman"],
    #             "Engineer" :["engineer"],
    #             "Lawyer": ["lawyer"],
    #             "Designer":["designer"],
    #             "Coach" :["coach"],
    #             "Photographer":["photographer"],
    #             "Nurse":["nurse"],
    #             "Bartender":["bartender"],
    #             "Waiter/Waitress":["waiter","waitress"],
    #             "Cashier":["cashier"]}
    # dic_after_filter = {}
    # for role in role_list.items():
    #     dic_after_filter[role[0]] = unit_roles(role[1],dic)
    # print(dic_after_filter)
    # write_dict_to_json(dic_after_filter, "top_roles_imdb.json")

    # # step4 - write file with top roles for women
    # dic = read_jsonfile_to_dic("dict_before_filter.json")
    # top_five_women_roles = ["Narrator", "Dancer", "Nurse", "Waitress", "Singer"]
    # s = list(filter(lambda item: item[0].replace("\"", "").replace("[", "").replace("]", "") in top_five_women_roles, dic.items()))
    # s = {item.replace("\"", "").replace("[", "").replace("]", ""): x for (item, x) in s}
    # print(s)
    # write_dict_to_json(s, "top_roles_imdb_women.json")

    # # step5 - write file of roles with more women than men
    # dic = read_jsonfile_to_dic("dict_before_filter.json")
    # s = list(filter(lambda item: item[1][0] < item[1][1] and item[1][0] != 0 and item[1][1]/item[1][0] < 10, dic.items()))
    # s = sorted(s, key=lambda item: item[1][1], reverse=True)[:100]
    # top_five_women_more_than_man_roles = ["Dancer", "Nurse", "Model", "Teacher", "Secretary"]
    # s = list(filter(lambda item: item[0].replace("\"", "").replace("[", "").replace("]", "") in top_five_women_more_than_man_roles,
    #                  dic.items()))
    # s = {item.replace("\"", "").replace("[", "").replace("]", ""): x for (item, x) in s}
    # print(s)
    # write_dict_to_json(s, "top_roles_imdb_women_more_than_man.json")

    # #step6 - top generic roles
    # dic = read_jsonfile_to_dic("dict_before_filter.json")
    # generic_role_list = {"Husband/Wife": ["Husband", "Wife"],
    #              "Father/Dad/Mother/Mom": ["Father", "Dad", "Mother", "Mom"],
    #              "Boy/Kid/Child/Girl": ["Boy", "Kid", "Child", "Girl"],
    #              "Son/Daughter": ["Daughter", "Son"],
    #              "Grandparent": ["grandmother", "grandfather", "grandparent"],
    #              "Grandchild": ["granddaughter", "grandson", "grandchild"]
    #              }
    # dic_after_generic_role_filter = {}
    # for role in generic_role_list.items():
    #     dic_after_generic_role_filter[role[0]] = unit_roles(role[1], dic)
    # print(dic_after_generic_role_filter)
    # write_dict_to_json(dic_after_generic_role_filter, "top_generic_roles_imdb.json")