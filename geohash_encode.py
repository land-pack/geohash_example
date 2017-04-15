import Geohash

geo_hash_str = Geohash.encode(39.92324, 116.3906, 5)
print(geo_hash_str)

# looking for the corne

corne_list = Geohash.decode('wx4g0')

print(corne_list)

# exactly point information
exactly_point = Geohash.decode_exactly('wx4g0')
print(exactly_point)