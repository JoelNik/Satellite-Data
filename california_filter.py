# Define our filter geometry from a geojson file
import json

geojson_file = 'ca.geojson'
with open(geojson_file) as f:
  geojson_geometry = json.loads(f.read())['geometry']

# Define geometry filter
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geojson_geometry
}

# Define date range filter
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2017-04-15T12:00:00.000Z",
    "lte": "2017-04-16T12:00:00.000Z"
  }
}

# Combine it all together into a single filter
california = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter]
}