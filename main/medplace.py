import requests

KEY = ' AIzaSyBaqFHGf54KrU01tNhjb3vT4JRjnhR5t3s '

lat_lng = {"lat" : "28.6", "lng" : "77.2"}

def get_places( lat_lng=lat_lng, doctor_type='doctor', radius=20000,):

    places_link = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ str(lat_lng['lat']) + ',' + str(lat_lng['lng']) + '&radius=' + str(radius) + '&name=' + doctor_type + '&key='+ KEY
    
    query_out = requests.get(places_link)
    query_result = query_out.json()['results']
    
    i = 0
    doc_list = []
    for place in query_result:
        # Returned places from a query are place summaries.
        doc = {}

        doc['name'] = place['name']
        #doc['rating'] = place['rating']
        doc['place_id'] = place.get('place_id')
        doc['vicinity'] = place.get('vicinity')

        place_detail_link = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place['place_id'] + '&key=' + KEY
        place_detail = requests.get(place_detail_link)        
        detail_out = place_detail.json()
        detail_dict = detail_out.get('result')
        doc['ph'] = detail_dict.get('formatted_phone_number')
        doc['website'] = detail_dict.get('website')
        doc['place_url'] = detail_dict.get('url')

        doc_list.append(doc)
    
    return doc_list
    
#a = get_places()
#print a
