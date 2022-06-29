import plotly.graph_objects as go
import chart_studio as cs

def create_bubble_chart():
    size = [8.620620, 11.228836]
    percent_women = 8620620 / (8620620 + 11228836) * 100
    percent_men = 100 - percent_women
    fig = go.Figure(data=[go.Scatter(
        x=['Women', 'Men'], y=list(range(2)),
        text=['Total Women:<br>8,620,620 ({per:.2f}%)'.format(per=percent_women),'Total Men<br>11,228,836 ({per:.2f}%)'.format(per=(100 - percent_women))],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)'],
            size=size,
            sizeref = 2. * 11.228836 / (21.228836 ** 2),
            

        )
    )])

    fig.update_yaxes(visible=False)
    fig.update_layout(
    title={
        'text': "Total Occupation in Cinema",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    fig.write_html('graphs/total_occupation.html')
    cs.plotly.plot(fig, filename="total_occupation", auto_open=True)

if __name__ == '__main__':
    username = 'DLevy'
    password = ""

    cs.tools.set_credentials_file(username=username, api_key=password)

    create_bubble_chart()