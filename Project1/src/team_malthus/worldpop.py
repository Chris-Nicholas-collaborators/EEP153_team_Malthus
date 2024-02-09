import urllib
import json
import pandas as pd

from urllib.request import urlopen
from typing import Any
import urllib.parse

def population_by_area(year: str, polygon: str) -> Any:
    """Get a population pyramid for an arbitrary polygon.
       Variables:
           year: year of interest
           polygon: a geojson polygon of interest
    """

    safe_url = urllib.parse.urlencode({'year': year, 'dataset': 'wpgpas', 'geojson': polygon})

    complete_url = "https://api.worldpop.org/v1/services/stats?" + safe_url

    with urllib.request.urlopen( complete_url ) as response: 
        response_text = response.read() 
        print( response_text )
        response_json = json.loads(response_text)
        if response_json['status_code'] != 200:
            raise Exception(f'Worldpop query returned {response_text}')

    task_id = response_json['taskid']

    results_url = 'https://api.worldpop.org/v1/tasks/' + task_id
    results_df = None

    with urllib.request.urlopen( results_url ) as results_response:
        results_text = results_response.read()
        print(results_text)
        results_json = json.loads(results_text)
        agesexpyramid_list = results_json['data']['agesexpyramid']
        agesexpyramid_df = pd.DataFrame(agesexpyramid_list)

        print('done')
        return agesexpyramid_df



year = '2020'
polygon = """{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{ "type": "Polygon", "coordinates": [ [ [ 16.496742359554229, -19.872651217111134 ], [ 19.883257497523321, -19.872651217111134 ], [ 19.883257497523321, -21.948257269414771 ], [ 16.514949430188473, -21.893636057512044 ], [ 16.496742359554229, -19.872651217111134 ] ] ] }}]}"""

area_df = population_by_area(year, polygon)

print('done')
