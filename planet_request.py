import os
import json 
import requests
from requests.auth import HTTPBasicAuth

# Define our filter geometry (box cover general vicinity of San Jose)
geo_json_geometry = {
  "type": "Polygon",
  "coordinates": [
    [
      [
        -122.12352161593165,
        36.931073271363616
      ],
      [
        -121.54673938936914,
        36.931073271363616
      ],
      [
        -121.54673938936914,
        37.85843432353896
      ],
      [
        -122.12352161593165,
        37.85843432353896
      ],
      [
        -122.12352161593165,
        36.931073271363616
      ]
    ]
  ]
}

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
    "gte": "2017-04-01T00:00:00.000Z",
    "lte": "2017-04-03T00:00:00.000Z"
  }
}

# Combine with a single AndFilter
san_jose = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter]
}


# Builds the API request
search_endpoint_request = {
  "item_types": ["PSScene4Band"],
  "filter": san_jose
}

# Sends POST request to search endpoint
result = \
  requests.post(
    'https://api.planet.com/data/v1/quick-search',
    auth=HTTPBasicAuth(os.environ['PLANET_API_KEY'], ''),
    json=search_endpoint_request)

print(result.text)