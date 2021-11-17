from rockset import Client, ParamDict
import sys
import re
import pprint

args = {}
args['pythonFile'] =  sys.argv[0]
pp = pprint.PrettyPrinter(indent=0,width=240)

for arg in sys.argv[1:]:
  variable = re.search('\-\-(.*)\=',arg)
  variable = variable.group(1)
  value = re.search('\=(.*)',arg)
  value = value.group(1)
  args[variable] = value

rs = Client(api_key= args["api_key"],
          api_server='https://api.use1a1.rockset.com')

# retrieve Most Popular Movies
qlambda = rs.QueryLambda.retrieve(
    '1_most_popular_movies_v1',
    version='5d8550b3715b792d',
    workspace='commons')

params = ParamDict()
params['cal_year'] = args["cal_year"]
results = qlambda.execute(parameters=params)
print(" ")
print("Most Popular Movies in " + args["cal_year"])
pp.pprint(results["results"])
print(" ")

# retrieve Highest Grossing Movies
qlambda = rs.QueryLambda.retrieve(
    '2_highest_grossing_movies_v1',
    version='b93d66b47afa985a',
    workspace='commons')

params = ParamDict()
params['cal_year'] = args["cal_year"]
results = qlambda.execute(parameters=params)
print(" ")
print("Highest Grossing Movies in " + args["cal_year"])
pp.pprint(results["results"])
print(" ")

# retrieve Most Popular Genre
qlambda = rs.QueryLambda.retrieve(
    '3_most_popular_genres_v1',
    version='f7d2fecb99564cbf',
    workspace='commons')

params = ParamDict()
params['cal_year'] = args["cal_year"]
results = qlambda.execute(parameters=params)
print(" ")
print("Most Popular Genres in " + args["cal_year"])
pp.pprint(results["results"])
print(" ")

# retrieve Largest Producers
qlambda = rs.QueryLambda.retrieve(
    '4_most_popular_genres_v1',
    version='cf1873eef4391a0a',
    workspace='commons')

params = ParamDict()
params['cal_year'] = args["cal_year"]
results = qlambda.execute(parameters=params)
print(" ")
print("Largest Producers of Most Popular Genre in " + args["cal_year"])
pp.pprint(results["results"])
print(" ")
