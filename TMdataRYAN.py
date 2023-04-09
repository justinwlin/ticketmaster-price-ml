import requests
import json
import datetime
import TMsales
import dataCollection
import location

def eventer(artist):
    print(artist)
    link = f'https://app.ticketmaster.com/discovery/v2/events.json?size=20&keyword={artist}&sort=relevance,desc&apikey=sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o'
    resp = requests.get(link)

    if resp.status_code != 200:
        return {'NA': 'Bad Response'}

    response = resp.text
    jsonresp = resp.json()
    events = {}
    if not jsonresp.get('_embedded'):
        print(artist + " has no shows")
        return events

    for i, event in enumerate(jsonresp.get('_embedded').get('events', [])):
        price_ranges = event.get('priceRanges')
        if price_ranges:
            showw = {}
            local_date = event.get('dates', {}).get('start', {}).get('localDate', '')
            year, month, day = local_date.split('-')

            d = datetime.date(int(year), int(month), int(day))
            eventdaynum = d.weekday()
            weekend = 0
            if eventdaynum == 0 or eventdaynum >= 5:
                weekend = 1

            eventids = event.get('id', 'NA')
            eventcity = event.get('_embedded', {}).get('venues', [{}])[0].get('city', {}).get('name', 'NA')
            populat = location.locator(eventcity)
            eventvenue = event.get('_embedded', {}).get('venues', [{}])[0].get('name', 'NA')
            pricemax = price_ranges[0].get('max', 'NA')
            pricemin = price_ranges[0].get('min', 'NA')
            Showname = event.get('name', 'NA')
            eventgenre = event.get('classifications', [{}])[0].get('genre', {}).get('name', 'NA')
            artistscore = dataCollection.getArtistPopularity(artist)
            eventid = artist + str(i)

            showw.update({'artist': artist, 'city': eventcity, 'venue': eventvenue, 'showName': Showname, 'genre': eventgenre,
                          'weekend': weekend, 'month': month, 'maxprice': pricemax, 'minprice': pricemin, 'id': eventids,
                          'score': artistscore, 'pop': populat})
            events.update({eventid: showw})
    return events
