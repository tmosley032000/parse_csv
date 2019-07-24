# parse_csv
Simple code that opens a csv file and loops through producing a dictionary for output

The input file(test.csv) contains the info to be parsed.

Notice that there are multiple URL's, dates and values in the input file.

The excersize is to produce a report (in this instance its a dict) that contains 
the URL with the greatest value for a particular date.  If there are multiple duplicate dates, select the highest value.

Sample output:
{'www.foo.com/foo4': {'10-23': 600}, 'www.foo.com/foo1': {'10-23': 600, '10-22': 600}, 'www.foo.com/foo2': {'10-23': 600, '10-22': 500, '10-21': 50}}
