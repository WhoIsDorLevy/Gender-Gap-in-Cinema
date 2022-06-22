import openpyxl
import os
import json
# from main import write_dict_to_json


def unit_roles(lst_of_lsts):
    total_women = 0
    total = 0
    for lst in lst_of_lsts:
        tot = lst[0]
        per_women = lst[1]
        total_women += int(tot * per_women)
        total += tot
    return [int(total - total_women), int(total_women)]

def extract_rows(keyword):    
    wookbook = openpyxl.load_workbook('resources/cpsaat11.xlsx')
    worksheet = wookbook.active
    rows = [[str(row[0]), str(row[1]), str(row[2])] for i, row in enumerate(worksheet.iter_rows(values_only=True))]
    rows = [row for row in rows if keyword in row[0].lower() and '–' not in row[2]]
    rows = [[int(row[1]), float(row[2]) / 100.0] for row in rows]
    return rows

def write_dict_to_json(dict, name):
    with open(os.path.join("resources", name), 'w') as out_file:
        json.dump(dict, out_file)

if __name__ == '__main__':
    to_json = {}
    to_json["Doctor"] = unit_roles([[167, 0.387], [921, 0.397], [59, 0.277]])
    to_json["Detective"] = unit_roles([[92, 0.158], [130, 0.273], [95, 0.423]])
    to_json["Police Officer"] = unit_roles([[753, 0.153]])
    engineer_rows = extract_rows('engineers')
    to_json["Engineer"] = unit_roles(engineer_rows)
    to_json["Lawyer"] = unit_roles([[1085, 0.379]])
    designer_rows = extract_rows('designers')
    to_json["Designer"] = unit_roles(designer_rows)
    to_json["Coache"] = unit_roles([[235, 0.443]])
    to_json["Photographer"] = unit_roles([[192, 0.493]])
    nurse_rows = extract_rows('nurse')
    to_json["Nurse"] = unit_roles(nurse_rows)
    to_json["Bartender"] = unit_roles([[362, 0.574]])
    to_json["Waiter/Waitress"] = unit_roles([[1631, 0.682]])
    to_json["Cashier"] = unit_roles([[1184, 0.329]])
    # print(to_json)
    write_dict_to_json(to_json, 'top_roles_us_bureau.json')



# percentage_women = total_women / total * 100
# percentage_men = 100.0 - percentage_women

# # print(total)
# # print(total_men)
# # print(total_women)
# # print(percentage_men)
# # print(percentage_women)




