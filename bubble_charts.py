import plotly.graph_objects as go
import chart_studio as cs

def create_bubble_chart():
    size = [0, 8.620620, 0, 0, 11.228836, 0]
    percent_women = 8620620 / (8620620 + 11228836) * 100
    percent_men = 100 - percent_women
    fig = go.Figure(data=[go.Scatter(
        x=list(range(6)), y=list(range(6)),
        text=['', 'Total Women:<br>8,620,620 ({per:.2f}%)'.format(per=percent_women),'','', 'Total Men<br>11228836 ({per:.2f}%)'.format(per=(100 - percent_women)), ''],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)','rgb(255, 65, 54)','rgb(255, 65, 54)','rgb(255, 65, 54)','rgb(255, 65, 54)'],
            size=size,
            sizeref = 2. * 11.228836 / (31.228836 ** 2),
            

        )
    )])
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    # fig.write_html('graphs/total_occupation.html')
    cs.plotly.plot(fig, filename="total_occupation", auto_open=True)

if __name__ == '__main__':
    username = 'DeGolan'
    password = ""

    cs.tools.set_credentials_file(username=username, api_key=password)

    create_bubble_chart()