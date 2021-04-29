from bs4 import BeautifulSoup 
import requests
import pandas as pd
url = "https://www.basketball-reference.com/friv/mvp.html"

#gets the required data from the url in text format
data = requests.get(url).text

#reads the Top Candidates table
table = pd.read_html(data)

#drops the empty column between PTS and Prob%
del table[0]["Unnamed: 31"]

#exports the table to excel
table[0].to_excel(r"the path of your excel file", index = False)
