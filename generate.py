import pandas
import click
import plotly.express as px


@click.command()
@click.option('--state', help='State in the US', required=True)
@click.option('--county', help='County in the US', required=True)
@click.option('--graph', help='cases | deaths', default='cases')
def run(state, county, graph):
    

    data = {
        'date': [],
        'cases': [],
        'deaths': []
    }

    f = open('covid-19-data/us-counties.csv', 'r')
    results = f.read()
    split = results.split('\n')[1:]
    for item in split:
        date,_county,_state,fips,cases,deaths = item.split(',')
        if _county.lower() == county.lower() and _state.lower() == state.lower():
            data['date'].append(date)
            data['cases'].append(cases)
            data['deaths'].append(deaths)
    df = pandas.DataFrame(data=data)
    fig = px.line(df, x="date", y=graph, title='Cases in {} county, {}'.format(county.capitalize(), state.capitalize()))
    fig.show()



    f.close()


if __name__ == '__main__':
    run()