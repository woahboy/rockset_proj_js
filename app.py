from flask import Flask, request, render_template
from rockset import Client, ParamDict
import sys
import re
app = Flask(__name__)

args = {}
args['pythonFile'] =  sys.argv[0]

for arg in sys.argv[1:]:
  variable = re.search('\-\-(.*)\=',arg)
  variable = variable.group(1)
  value = re.search('\=(.*)',arg)
  value = value.group(1)
  args[variable] = value

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    rs = Client(api_key=args["api_key"],
          api_server='https://api.use1a1.rockset.com')
    year = request.form['variable']
    # retrieve Most Popular Movies
    qlambda1 = rs.QueryLambda.retrieveByTag(
        '1_most_popular_movies_v1',
        tag='latest',
        workspace='commons')

    # retreive Highest Grossing Movies
    qlambda2 = rs.QueryLambda.retrieveByTag(
        '2_highest_grossing_movies_v1',
        tag='latest',
        workspace='commons')

    # retrieve Most Popular Genre
    qlambda3 = rs.QueryLambda.retrieveByTag(
        '3_most_popular_genres_v1',
        tag='latest',
        workspace='commons')

    # retrieve Largest Producers
    qlambda4 = rs.QueryLambda.retrieveByTag(
        '4_most_popular_genres_v1',
        tag='latest',
        workspace='commons')

    params = ParamDict()
    params['cal_year'] = request.form['variable']
    results1 = qlambda1.execute(parameters=params)
    results2 = qlambda2.execute(parameters=params)
    results3 = qlambda3.execute(parameters=params)
    results4 = qlambda4.execute(parameters=params)
    return HELLO_HTML.format(
                year,
                str(results1["results"][0]),
                str(results1["results"][1]),
                str(results1["results"][2]),
                str(results1["results"][3]),
                str(results1["results"][4]),
                str(results1["results"][5]),
                str(results1["results"][6]),
                str(results1["results"][7]),
                str(results1["results"][8]),
                str(results1["results"][9]),
                str(results2["results"][0]),
                str(results2["results"][1]),
                str(results2["results"][2]),
                str(results2["results"][3]),
                str(results2["results"][4]),
                str(results2["results"][5]),
                str(results2["results"][6]),
                str(results2["results"][7]),
                str(results2["results"][8]),
                str(results2["results"][9]),
                str(results3["results"][0]),
                str(results3["results"][1]),
                str(results3["results"][2]),
                str(results3["results"][3]),
                str(results3["results"][4]),
                str(results3["results"][5]),
                str(results3["results"][6]),
                str(results3["results"][7]),
                str(results3["results"][8]),
                str(results3["results"][9]),
                str(results4["results"][0]),
                str(results4["results"][1]),
                str(results4["results"][2]),
                str(results4["results"][3]),
                str(results4["results"][4]),
                str(results4["results"][5]),
                str(results4["results"][6]),
                str(results4["results"][7]),
                str(results4["results"][8]),
                str(results4["results"][9]))

HELLO_HTML = """
    <html><body>
        <h1>Most Popular Movies in {0}!</h1>
        {1}<br>
        {2}<br>
        {3}<br>
        {4}<br>
        {5}<br>
        {6}<br>
        {7}<br>
        {8}<br>
        {9}<br>
        {10}<br>
	<br>
	<h1>Highest Grossing Movies in {0}!</h1>
        {11}<br>
        {12}<br>
        {13}<br>
        {14}<br>
        {15}<br>
        {16}<br>
        {17}<br>
        {18}<br>
        {19}<br>
        {20}<br>
        <h1>Most Popular Genre in {0}!</h1>
        {21}<br>
        {22}<br>
        {23}<br>
        {24}<br>
        {25}<br>
        {26}<br>
        {27}<br>
        {28}<br>
        {29}<br>
        {30}<br>
        <h1>Largest producers of most popular genre in {0}!</h1>
        {31}<br>
        {32}<br>
        {33}<br>
        {34}<br>
        {35}<br>
        {36}<br>
        {37}<br>
        {38}<br>
        {39}<br>
        {40}<br>
    </body></html>"""

app.run()
