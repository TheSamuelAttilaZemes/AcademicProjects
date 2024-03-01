from pygal import Bar
#Create a chart
chart = Bar(title='Olympic games')

file_path = 'pop.csv'
# Add data to the chart
with open(file_path) as f:
    for line in f:
        pieces = line.split(',')  # Breaks the string into a list
        print(pieces)  # Print each list

#Display chart - Note this will go last to print data on chart
chart.render_in_browser()