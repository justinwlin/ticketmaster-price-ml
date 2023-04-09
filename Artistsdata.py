import TMdataRYAN
import json
import csv


artists=['Post Malone', 'Drake',
'Childish Gambino', 'Imagine Dragons', 'Cardi B',
'Shinedown', 'Leon Bridges',
'Ed Sheeran', 'Shawn Mendes', 'Luke Combs',
'Camila Cabello', 'Kendrick Lamar', 'The Weeknd', 'Jason Aldean',
#'Lake Street Dive',
'Bruno Mars', 'Dua Lipa','Taylor Swift', 'Maroon','Migos','Keith Urban',
'Kane Brown', #'Ariana Grande',
'Nicki Minaj','Chris Stapleton','Charlie Puth', 'Florida Georgia Line',
'Khalid','Kenny Chesney','YoungBoy Never Broke Again','Thomas Rhett', 'Halsey',
'Bazzi','SZA','Marshmello','P!nk', 'Travis Scott','Justin Timberlake',
'Bebe Rexha','Rich The Kid', 'Demi Lovato','BlocBoy JB','Brett Young',
'Luke Bryan','Dan + Shay', #'Royce da' ,
'Ella Mai', 'Rae Sremmurd', 'Metallica', #'Blake Shelton', #'Rihanna',
'Eminem','Maren Morris','J Balvin', 'Portugal. The Man', 'Meghan Trainor',
'Zedd','Ty Dolla $ign', 'Parkway Drive', 'Carrie Underwood', 'G-Eazy',
'Daddy Yankee', 'Lil Dicky', 'Chris Brown', 'Kanye West',
'Ozuna', 'Bad Bunny', 'NF', 'Adele', 'Kelly Clarkson',
'Janelle Monae', 'Darius Rucker', 'Godsmack', 'Grey',
'Bad Wolves', 'Foster The People', 'The Chainsmokers', 'MercyMe', 'Anne-Marie',
'Sam Smith', 'Lil Pump','Logic','Niall Horan', 'Bon Jovi', 'Lil Uzi Vert',
'Lynyrd Skynyrd', 'Dustin Lynch', 'Savage', 'Jordan Davis', 'Sam Hunt', 'Panic! At The Disco',
'Famous Dex', 'Maluma'

]

masterlist = {}

# loop through the list of artists and collect event data using the eventer function
for artist in artists:
    event_dict = TMdataRYAN.eventer(artist)
    masterlist.update(event_dict)

# write the collected data to a CSV file
with open('dang2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # write the header row to the CSV file
    header_row = ['artist', 'city', 'venue', 'showName', 'genre', 'weekend', 'month', 'maxprice', 'minprice', 'id', 'score', 'pop']
    writer.writerow(header_row)
    print(masterlist.values())
    # write the data rows to the CSV file
    # {'artist': 'Post Malone', 'city': 'Cologne',
    #   'venue': 'NA', 'showName': 'Post Malone | Logen-Package', 
    #   'genre': 'Rock', 'weekend': 1, 'month': '05', 'maxprice': 90.0, 
    #   'minprice': 90.0, 'id': 'Z698xZC2Z17feA4', 'score': 89, 'pop': 'FAKE'}
    for event_data in masterlist.values():
        data_row = [
            event_data.get('artist', 'NA'),
            event_data.get('city', 'NA'),
            event_data.get('venue', 'NA'),
            event_data.get('showName', 'NA'),
            event_data.get('genre', 'NA'),
            event_data.get('weekend', 'NA'),
            event_data.get('month', 'NA'),
            event_data.get('maxprice', 'NA'),
            event_data.get('minprice', 'NA'),
            event_data.get('id', 'NA'),
            event_data.get('score', 'NA'),
            event_data.get('pop', 'NA')
        ]
        writer.writerow(data_row)

    #writer.writerow(masterlist.get(ln).get(ln))
