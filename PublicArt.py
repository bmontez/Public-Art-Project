
print "+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +""\n"
print "WELCOME TO SAN FRANCISCO'S PUBLIC ART TOUR""\n"
print "The following neighborhoods feature amazing public artwork for everyone to enjoy."
print "To begin your self-guided tour, enter the number for the neighborhood that you'd like to explore.""\n"


import csv

civic_art_file= open('SF_Civic_Art_Collection.csv')
csv_file = csv.reader (civic_art_file)
all_artworks =[]
for row in csv_file:
	all_artworks.append(row)


neighborhoods = ["Civic Center", "SoMa", "Mission", "Embarcadero", "Hayes Valley"]

for index, district in enumerate(neighborhoods):
	print str(index)+ ") " + district

select_neighborhood = raw_input("Which neighborhood would you like to tour?" "\n")

def art_search():

	select_index = int (select_neighborhood)

	selected_artwork = [artwork for artwork in all_artworks if artwork[4] == neighborhoods [select_index]]

	for index, artwork in enumerate (selected_artwork):
		print str(index)+ ") " + artwork[0]+  ", " + artwork[3] + ", " + artwork[1] + ", " + artwork[5]


art_search()
#git commands for the future
#git add filename_thatchanged
#git commit -m "describe changes here"
#git push origin master


while (True):
	select_neighborhood = raw_input("\n" "Which new neighborhood would you like to explore? 0 = Civic Center, 1 = SoMa, 2 = Mission, 3 = Embarcadero, 4 = Hayes Valley, 5 = Exit Program. Answer: " "\n")
	if select_neighborhood == "5": 
		break
	else:
		art_search()	
















