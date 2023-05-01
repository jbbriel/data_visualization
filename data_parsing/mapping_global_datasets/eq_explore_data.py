import json

# Explore the Structure of the data.
filename = 'data\eq_data_1_day_m1.json'

with open(filename, encoding='utf-8') as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
    mags.append(mag)


print(mags[:10])
print(f"First 5 longitudes:\n{lons[:5]}")
print(f"First 5 latitudes:\n{lats[:5]}")