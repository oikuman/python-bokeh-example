from datetime import datetime
from bokeh.plotting import figure, show, output_file
import pprint as pp

from name_month_data import name_month_data
from name_birth_data import name_birth_data
pp.pprint(name_birth_data)
pp.pprint(name_month_data)

months = list(name_month_data.values())

year_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months_occurancies = dict().fromkeys(year_months)


for month in year_months:
	c = months.count(month)
	months_occurancies[month] = c
	
print(months_occurancies)
occurancies = list(months_occurancies.values())

output_file('vbar.html')

p = figure(plot_width=600, plot_height=600)

p.vbar(x = year_months, width = 1, bottom = 0, top = occurancies, color = "firebrick")

show(p)