import os
import json 
import requests
from requests.auth import HTTPBasicAuth

# Define our filter geometry from attached file (CA state boundary)
geojson_file = 'ca.geojson'
with open(geojson_file) as f:
  geojson_geometry = json.loads(f.read())['geometry']

# Define geometry filter
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geo_json_geometry
}

# Define date range filter
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2017-03-01T00:00:00.000Z",
    "lte": "2017-04-15T00:00:00.000Z"
  }
}

# Combine it all together into a single filter
san_jose = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter]
}


# Builds the API request
search_endpoint_request = {
  "item_types": ["Landsat8L1G"],
  "filter": san_jose
}

# Sends POST request to the search endpoint and store the result 
result = \
  requests.post(
    'https://api.planet.com/data/v1/quick-search',
    auth=HTTPBasicAuth(os.environ['PLANET_API_KEY'], ''),
    json=search_endpoint_request)

# Write results to a file 
with open('results.json', 'w') as f:
  f.write(result.text)