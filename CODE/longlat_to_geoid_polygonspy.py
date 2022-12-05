#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:25:01 2022

@author: mortezamaleki
"""

import geopandas as gpd
import pandas as pd
import numpy as np


geojson_master = gpd.read_file("database/geoid.geojson")
main = pd.read_csv('database/main_table_geoid.csv')
school = pd.read_csv('Data Sources/sates_county_level_school_district_school_rating.csv')


school['County_code'] = school['County_code'].apply(lambda x: x.split('c')[1])

main['geoid'] = main['geoid'].astype(str)
main['geoid'] = main['geoid'].apply(lambda x: "0" + x if len(x) == 11 else x)
main['geoid_county'] = main['geoid_county'].astype(str)
main['geoid_county'] = main['geoid_county'].apply(lambda x: "0" + x if len(x) == 4 else x)

school['geoid_county'] = school['County_code']
main_school_merged = main.merge(school, on = 'geoid_county', how = 'left')
geojson_master['geoid'] = geojson_master['CensusBlockGroup']
school_geojson_merged = main_school_merged.merge(geojson_master, on='geoid', how='left')
school_geojson_merged  = gpd.GeoDataFrame(school_geojson_merged)

school_geojson_merged.to_file("Data Sources/school_geojson_merged.geojson", driver="GeoJSON")


























