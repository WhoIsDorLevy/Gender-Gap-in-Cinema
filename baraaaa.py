# def doctors():
#     dentists = [167, 0.387]
#     other = [921, 0.397]
#     surgeons = [59, 0.277]

#     total_women = int(dentists[0]*dentists[1] +other[0]*other[1] + surgeons[0]*surgeons[1])
#     total = dentists[0] + other[0] + surgeons[0]
#     total_men = total - total_women
#     return (total_men, total_women)
import openpyxl
def unit_roles(lst_of_lsts):
    total_women = 0
    for lst in lst_of_lsts:
        tot = lst[0]
        per_women = lst[2]
        total_women += int(tot * per_women)
    return [total - total_women, total_women]


if __name__ == '__main__':
    doctors = unit_roles([[167, 0.387], [921, 0.397], [59, 0.277]])
    detectives = unit_roles([[92, 0.158], [130, 0.273], [95, 42]])
    police_officers = unit_roles([753, 0.153])


# percentage_women = total_women / total * 100
# percentage_men = 100.0 - percentage_women

# # print(total)
# # print(total_men)
# # print(total_women)
# # print(percentage_men)
# # print(percentage_women)




