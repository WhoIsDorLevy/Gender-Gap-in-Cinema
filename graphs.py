import pandas as pd
import json_methods
import plotly.graph_objects as go

def get_percentage(gender, dic):
    output = []
    for lst in dic.values():
        to_add = lst[gender] / (lst[0] + lst[1])
        output.append(to_add)
    return output

def make_graph(jsons, categories, stats, categories_title, constants, gender, html_name):
    read_jsons = [json_methods.read_jsonfile_to_dic(j) for j in jsons]
    roles = [key for key in read_jsons[0].keys()]
    
    for i in range(1, len(read_jsons)):
        roles += roles
    
    category_table = []
    for i in range(len(categories)):
        category_table += [categories[0] for _ in range(len(roles) // 2)]
    
    constant_col = [get_percentage(gender, dic) for dic in read_jsons]
    constant_col = [x for xs in constant_col for x in xs] # flatten list of lists

    print(len(roles))
    print(len(category_table))
    print(len(constant_col))

    final_table = pd.DataFrame({
        stats: roles,
        categories_title: category_table,
        constants: constant_col
    })
    
    
    fig = go.Figure()
    for contestant, group in final_table.groupby(categories_title):
        # hovertemplate_str = "%s=%s<br>%s".format(categories_title, stats, Reality) + "=%%{x}<br>Gender Ratio=%%{y}<extra></extra>"
        # fig.add_trace(go.Bar(x=group[stats], y=group[constants], name=Reality,
        # hovertemplate=hovertemplate_str))
        # "%s=%s<br>%s=%%{x}<br>Gender Ratio=%%{y}<extra></extra>"% categories_title stats Reality))
        #  hovertemplate="Contestant=%s<br>Fruit=%%{x}<br>Number Eaten=%%{y}<extra></extra>"% contestant))
         fig.add_trace(go.Bar(x=group["Occupation"], y=group["Gender Ratio"], name=contestant,
        hovertemplate="Reality=%s<br>Occupation=%%{x}<br>Gender Ratio=%%{y}<extra></extra>"% contestant))
    fig.update_layout(legend_title_text="Choose Reality")
    fig.update_xaxes(title_text=stats)
    fig.update_yaxes(title_text=constants)
    fig.update_layout(yaxis_tickformat = '.0%')
    fig.write_html('graphs/' + html_name)



if __name__ == '__main__':
    jsons = ['top_roles_imdb.json', 'top_roles_us_bureau.json']
    categories = ['Cinema', 'Real Life']
    make_graph(jsons, categories, 'Occupation', 'Reality', 'Gender Ratio', 0, 'men_most_common.html')
    # imdb_dic = json_methods.read_jsonfile_to_dic('top_roles_imdb.json')
    # real_life_dic = json_methods.read_jsonfile_to_dic('top_roles_us_bureau.json')
    # roles = [key for (key, val) in imdb_dic.items()]
    # roles += roles
    # # print(roles)
    # # women_table = pd.DataFrame({
    # # "Occupation": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    # # "Reality": ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"],
    # # "Gender Ratio": [2, 1, 3, 1, 3, 2],
    # # })
    # reality = ["Cinema" for _ in range(len(roles) // 2)]
    # reality += ["Real Life" for _ in range(len(roles) // 2)]
    # women_table = pd.DataFrame({
    #     "Occupation": roles,
    #     "Reality": reality,
    #     "Gender Ratio": get_percentage(1, imdb_dic) + get_percentage(1, real_life_dic)
    # })

    # # Plotly Express

    # import plotly.express as px

    # fig = px.bar(women_table, x="Occupation", y="Gender Ratio", color="Reality", barmode="group")
    # fig.show()


    # Graph Objects

    


