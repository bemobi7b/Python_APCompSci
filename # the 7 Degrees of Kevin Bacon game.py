# the 7 Degrees of Kevin Bacon game
# import requests
import csv

allCountries1 = ["United States", "Canada", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Cape Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Eswatini", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Democratic Republic of the Congo", "Zambia", "Zimbabwe"]

yearsList = []

moviesBechdelList = []
passFailsList = []
movieYearsBechdelList = []

topMoviesList = []

netflixContentList = []
netflixCountryList = []
netflixReleaseYearsList = []

topMoviesStar1 = []
topMoviesStar2 = []
topMoviesStar3 = []
topMoviesStar4 = []
starLists = [topMoviesStar1, topMoviesStar2, topMoviesStar3, topMoviesStar4]

baconMoviesfromTop = []

coStarsOfBacon = []
coStarsWithBacon = []

for yearsIndex in range(126):
    #make a list of all years between 1900-2025
    yearsList.append(yearsIndex + 1900)
    yearsIndex += 1

# this function is used later to remove all the instances of Kevin Bacon from a list of actors
# I used the website https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/
def remove_items(test_list, item): 
   res = [i for i in test_list if i != item]
   return res

#https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
# I used this website to learn how to traverse .csv files 
# The next line opens the file with a list of movies and their performance on the Bechdel Test among other data
# It also puts the file in read mode ('r') and keeps it open until 
with open('bechdelTest.csv', 'r') as csvfile:
  # Create a reader object
  csv_reader = csv.reader(csvfile)
  for row in csv_reader:
      moviesBechdelList.append(row[2])
      passFailsList.append(row[3])
      movieYearsBechdelList.append(row[1])

with open('netflixContent.csv', 'r') as csvfile:
   csv_reader = csv.reader(csvfile)
   for row in csv_reader:
      netflixContentList.append(row[2])
      netflixCountryList.append(row[3])
      if row[0] != "id":
         netflixReleaseYearsList.append(float(row[5]))

for count in range(len(netflixReleaseYearsList) - 1):
   netflixReleaseYearsList[count] = int(netflixReleaseYearsList[count])
#converts all years into int values because they had a .0 at the end in the csv file

with open('imdbTopThousandMovies.csv', 'r', encoding="utf8") as csvfile:
  csv_reader2 = csv.reader(csvfile)
  for row in csv_reader2:
      topMoviesList.append(row[2])
      topMoviesStar1.append(row[11])
      topMoviesStar2.append(row[12])
      topMoviesStar3.append(row[13])
      topMoviesStar4.append(row[14])

for i in range(4):
    tempList = starLists[i]
    for j in range(len(tempList) - 1):
        if tempList[j] == "Kevin Bacon":
            baconMoviesfromTop.append(topMoviesList[j])
            coStarsWithBacon.append(topMoviesStar1[j])
            coStarsWithBacon.append(topMoviesStar2[j])
            coStarsWithBacon.append(topMoviesStar3[j])
            coStarsWithBacon.append(topMoviesStar4[j])
# if Kevin Bacon is in a movie, add all the stars of that movie to a list of his costars, then remove all the instances of Kevin Bacon

coStarsOfBacon = remove_items(coStarsWithBacon, "Kevin Bacon")
            


#Setup ends here ________________________________________________________________________________________________




print(baconMoviesfromTop)
print(coStarsOfBacon)
print(netflixReleaseYearsList[4])

# Kevin bacon is in the 1994 film, The River Wild, on Netflix

#Alison Bechdel created the Bechdel test in 1985, the same year in which Kevin Bacon starred in the movie, "The Little Sister"









































































#import pip._vendor.requests 

# name = 'Michael Jordan'
# api_url = "http://wishiy.com/api/today".format(name)
# response = pip._vendor.requests.get(api_url)
# if response.status_code == pip._vendor.requests.codes.ok:
#     print(response.text)
# else:
#     print("Error:", response.status_code, response.text)
