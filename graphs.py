import pandas as pd
import json_methods
import plotly.graph_objects as go
import chart_studio as cs


def get_percentage(gender, dic):
    output = []
    for lst in dic.values():
        to_add = lst[gender] / (lst[0] + lst[1])
        output.append(to_add)
    return output

def get_quantity(gender, dic):
    output = []
    for lst in dic.values():
        to_add = lst[gender]
        output.append(to_add)
    return output

def make_graph_ratio(jsons, categories, categories_title, genders, html_name):
    read_jsons = [json_methods.read_jsonfile_to_dic(j) for j in jsons]
    roles = [key for key in read_jsons[0].keys()]
    
    for i in range(1, len(read_jsons)):
        roles += roles
    
    category_table = []
    for i in range(len(categories)):
        category_table += [categories[i] for _ in range(len(roles) // 2)]
    
    constant_col = [get_percentage(genders[i], read_jsons[i]) for i in range(len(read_jsons))]
    constant_col = [x for xs in constant_col for x in xs] # flatten list of lists

    

    final_table = pd.DataFrame({
        "Occupation": roles,
        categories_title: category_table,
        "Gender Ratio": constant_col
    })
    
    
    fig = go.Figure()
    for contestant, group in final_table.groupby(categories_title):
        fig.add_trace(go.Bar(x=group["Occupation"], y=group["Gender Ratio"], name=contestant,
            hovertemplate=categories_title+"=%s<br>Occupation=%%{x}<br>Gender Ratio=%%{y}<extra></extra>"% contestant))
    fig.update_layout(legend_title_text="Choose "+categories_title)
    fig.update_xaxes(title_text="Occupation")
    fig.update_yaxes(title_text="Gender Ratio")
    fig.update_layout(yaxis_tickformat = '.0%')
    # fig.write_html('graphs/' + html_name)
    cs.plotly.plot(fig, filename=html_name, auto_open=True)

def make_graph_quantity(jsons, categories, categories_title, genders, html_name):
    read_jsons = [json_methods.read_jsonfile_to_dic(j) for j in jsons]
    roles = [key for key in read_jsons[0].keys()]
    
    for i in range(1, len(read_jsons)):
        roles += roles
    
    category_table = []
    for i in range(len(categories)):
        category_table += [categories[i] for _ in range(len(roles) // 2)]
    
    constant_col = [get_quantity(genders[i], read_jsons[i]) for i in range(len(read_jsons))]
    constant_col = [x for xs in constant_col for x in xs] # flatten list of lists

    print(constant_col)
 

    final_table = pd.DataFrame({
        "Occupation": roles,
        categories_title: category_table,
        "Total Roles": constant_col
    })
    
    
    fig = go.Figure()
    for contestant, group in final_table.groupby(categories_title):
        fig.add_trace(go.Bar(x=group["Occupation"], y=group["Total Roles"], name=contestant,
            hovertemplate=categories_title+"=%s<br>Occupation=%%{x}<br>Total Roles=%%{y}<extra></extra>"% contestant))
    fig.update_layout(legend_title_text="Choose "+categories_title)
    fig.update_xaxes(title_text="Occupation")
    fig.update_yaxes(title_text="Total Roles")
    # fig.update_layout(yaxis_tickformat = '.0%')
    #fig.write_html('graphs/' + html_name)
    cs.plotly.plot(fig, filename=html_name, auto_open=True)


if __name__ == '__main__':

    username = 'DeGolan'
    #password = ''

    cs.tools.set_credentials_file(username=username, api_key=password)

    common_jsons = ['top_roles_imdb.json', 'top_roles_us_bureau.json']
    common_categories = ['Cinema', 'Real Life']

    # make_graph_ratio(common_jsons, common_categories, 'Reality', [0,0], 'men_most_common')
    make_graph_ratio(common_jsons, common_categories, 'Reality', [1,1], 'women_most_common')


    make_graph_quantity(['top_roles_imdb_women.json', 'top_roles_imdb_women.json'], ['Men', 'Women'], 'Gender', [0,1], 'top_cinema_roles_women')

    make_graph_ratio(['top_roles_imdb_women_more_than_man.json', 'top_roles_imdb_women_more_than_man.json'], ['Men', 'Women'], 'Gender', [0,1], 'woman_more_than_men_roles')
    make_graph_ratio(['top_generic_roles_imdb.json', 'top_generic_roles_imdb.json'], ['Men', 'Women'], 'Gender', [0,1], 'generic_roles')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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

    


