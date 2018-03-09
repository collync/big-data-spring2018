## Extra Credit Opportunity

# Build a scraper that downloads and parses the Wikipedia [List of Countries by Greenhouse Gas Emissions page](https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions)
# using BeautifulSoup and outputs the table of countries as as a CSV.

import requests
import bs4

response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_by_greenhouse_gas_emissions')
soup = bs4.BeautifulSoup(response.text, "html.parser")
print(soup.prettify())

#check all a class
data = soup.find_all('a')

#find the context in all a
for link in data:
        print (link.string)

data2 = soup.find_all('td')
for link in data2:
        print (link.string)




# for i in data:
#     print(i.string)
#
#
#
# ```
#
#
# ```python
# # Access Data in the table (note it returns an array)
# soup.find_all('td')
# ```
# data = soup.findAll(attrs={'class':'city'})
#
#
# f = open('rat_data.txt','a') # open new file, make sure path to your data file is correct
#
# p = 0 # initial place in array
# l = len(data)-1 # length of array minus one
#
# f.write("City, Number\n") #write headers
#
# while p < l: # while place is less than length
#     f.write(data[p].string + ", ") # write city and add comma
#     p = p + 1 # increment
#     f.write(data[p].string + "\n") # write number and line break
#     p = p + 1 # increment
#
# f.close() # close file
