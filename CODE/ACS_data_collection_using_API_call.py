# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:29:34 2022

@author: pkalan3
"""

#%% Import Libraries
import http.client
import json
import csv
import urllib.request
import sqlite3
from sqlite3 import Error
import sys
import os
import ctypes  # For message box


#%% Functions #################################################################

#%% Create a Messagebox    e.g. Mbox('Your title', 'Your text', 1)
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

#%% Create a list of State and Counties   e.g. fn_state_county_combos()
def fn_state_county_combos():
    year = '2019'
    dataset = '/acs/acs5/profile'
    variables = 'DP05_0001E' # list of variables separated by comma
    geography = 'county:*&in=state:*'
    url = 'https://api.census.gov/data/' + year + dataset + '?get=' + variables + '&for=' + geography
    url_handle = urllib.request.urlopen(url).read()
    data = json.loads(url_handle)
    state_county_combos = [[b, c] for a,b,c in data] # [[state_id, county_id]]
    return state_county_combos

#%% Check if the table exists in the database (returns 1/0)     e.g. fn_chktable(con, 'acs_data')
def fn_chktable(con, name):
    return con.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" + name + "'").fetchone()[0]

#%% Create the main table in database     e.g. fn_create_table(state_county_combos)
def fn_create_table(state_county_combos):
    con.execute("CREATE TABLE table_ver2(name text, state integer, county integer, tract integer, block_group integer, geoid int);")
    year = '2020'
    dataset = '/acs/acs5'
    variables = 'NAME'
    for combo in state_county_combos[1:]: ##1191-1192 gave error
        try:
            geography = 'block%20group:*&in=state:' + combo[0] + '&in=county:' + combo[1] + '&in=tract:*'
            url = 'https://api.census.gov/data/' + year + dataset + '?get=' + variables + '&for=' + geography + '&key=' + acs_api_key
            url_handle = urllib.request.urlopen(url).read()
            data = json.loads(url_handle)
            for row in data[1:]:
                con.execute("INSERT INTO table_ver2 VALUES (?, ?, ?, ?, ?, ?\
                                   )",(row[0],row[1],row[2],row[3], row[4], row[1] + row[2] + row[3] + row[4]))
            con.commit()
        except:
            print('Error for value of ', combo)

#%% Print the schema of the table     e.g. fn_schema(con, 'acs_data')
def fn_schema(con, name):
    print("Schema for the table " + name + ":")
    for row in con.execute("pragma table_info('table_ver2')").fetchall():
        print (row)

#%% Add new variable column to the main table     e.g. fn_add_variable('population', 'B01001_001E', 'integer', state_county_combos)
def fn_add_variable(name, code, datatype, state_county_combos):
    if not con.execute("SELECT COUNT(*) AS CNTREC FROM pragma_table_info('table_ver2') WHERE name='" + name + "'").fetchone()[0]:
        con.execute("ALTER TABLE table_ver2 ADD " + name + " " + datatype + ";")
    year = '2020'
    dataset = '/acs/acs5'
    for combo in state_county_combos:
        try:
#            if index%322 == 0:
#                print(name + " completed: " + str(int(index//322*100)) + "%")
            geography = 'block%20group:*&in=state:' + combo[0] + '&in=county:' + combo[1] + '&in=tract:*'
            url = 'https://api.census.gov/data/' + year + dataset + '?get=' + code + '&for=' + geography + '&key=' + acs_api_key
            url_handle = urllib.request.urlopen(url).read()
            data = json.loads(url_handle)
            for row in data[1:]:
                con.execute("UPDATE table_ver2 SET " + name + " = " + row[0] + " WHERE geoid = " + row[1] + row[2] + row[3] + row[4] + ";")
            con.commit()
        except:
            print('Error for value of ', combo)

#%% Main Program ##############################################################

#%% Set working directory
os.chdir(r'C:\Users\Pankaj\Documents\GitHub\CSE6242\Group_project')

#%% Set API Key
if 'acs_api_key'in globals():
    print("ACS API key available.")
else:
    acs_api_key = '26467d3589507925c17dbd204de33f2c98a3aef7' # Created for pkalan3
    print("ACS API key added for user pkalan3.")

#%% Create connection
try:
    con = sqlite3.connect("acs_database_ver3")
    con.text_factory = str
    print("ACS database connected.")
except Error as e:
    sys.exit("ACS database con error:" + str(e))

#%% Create a list of State and Counties
if 'state_county_combos' in globals():
    print("State and County list available.")
else:
    state_county_combos = fn_state_county_combos()
    print("State and County list created.")

#%% Create Table with Geolocation data
if fn_chktable(con, 'table_ver2'):
    print("Main Table exists")
else:
    fn_create_table(state_county_combos)

fn_schema(con, 'table_ver2')

#%% Add new variables to the table

# Completed:
fn_add_variable('population', 'B01001_001E', 'integer', state_county_combos)

fn_add_variable('median_age', 'B01002_001E', 'integer', state_county_combos)
print("median_age completed!")

# In progress:

fn_add_variable('median_income', 'B07011_001E', 'integer', state_county_combos)
print("median_income completed!")

fn_add_variable('male_pop', 'B01001_002E', 'integer', state_county_combos)
print("male_pop completed!")
#
## Remaining:
fn_add_variable('female_pop', 'B01001_026E', 'integer', state_county_combos)
print("female_pop completed!")
#
fn_add_variable('white', 'B02001_002E', 'integer', state_county_combos)
print("white completed!")
#
fn_add_variable('black', 'B02001_003E', 'integer', state_county_combos)
print("black completed!")
#
fn_add_variable('asian', 'B02001_005E', 'integer', state_county_combos)
print("asian completed!")
#
fn_add_variable('asian_with_others', 'B02011_001E', 'integer', state_county_combos)
print("asian_with_others completed!")
