from pygal import Bar
#Create a chart
chart = Bar(title='Olympic games')

# Add data to the chart
us = ['United States', 2399]
ru = ['Russia', 1413]
gb = ['Great Britain', 1304]
fr = ['France', 780]
de = ['Germany', 671]

chart.add(us[0], us[1])
chart.add(ru[0], ru[1])
chart.add(gb[0], gb[1])
chart.add(fr[0], fr[1])
chart.add(de[0], de[1])

#Display chart - Note this will go last to print data on chart
chart.render_in_browser()