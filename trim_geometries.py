import json
import shapely
from shapely.wkt import dumps, loads
from shapely.geometry import mapping, shape

# Trims the geometries so that they only include the filter geometry
geojson_file = 'ca.geojson'
with open(geojson_file) as f:
  geojson_geometry = json.loads(f.read())['geometry']

with open('results.json','r') as f:
	result = json.loads(f.read())
features = result['features']
ca_geom = shape(geojson_geometry)

for feat in features:
  geom = shape(feat['geometry'])
  feat['properties']['centroid_x'] = geom.centroid.x
  feat['properties']['centroid_y'] = geom.centroid.y
  geom = geom.intersection(ca_geom)
  feat['geometry'] = mapping(geom)


# Write results to a file 
with open('results_new.json', 'w') as f:
  f.write(json.dumps(result, indent = 4))