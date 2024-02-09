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
        response_json = json.loads(response_text)
        if response_json['status_code'] != 200:
            raise Exception(f'Worldpop query returned {response_text}')

    task_id = response_json['taskid']

    results_url = 'https://api.worldpop.org/v1/tasks/' + task_id
    results_df = None

    with urllib.request.urlopen( results_url ) as results_response:
        results_text = results_response.read()
        age_json = json.loads(results_text)
        agesexpyramid_list = age_json['data']['agesexpyramid']
        agesexpyramid_df = pd.DataFrame(agesexpyramid_list)

        return agesexpyramid_df
