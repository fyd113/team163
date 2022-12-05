# Team163
Understanding CSE6242 Project Repository

## DESCRIPTION

DOC folder includes final project report and final poster <br />
CODE folder includes one .twb file showing our final product and a few .ipynb files showing how we scraped and cleaned data

## INSTALLATION - How to install and setup our code

### Install Jupyter Notebook:
`pip install notebook`
`pip install geopandas`

### Install required packages for Jupyter Notebook:
`pip install requests`
`pip install regex`
`pip install python-csv`
`pip install beautifulsoup4`
`pip install pandas`
`pip install pandas`
`pip install python-csv`
`pip install pyspark`

### Install Chrome Instant Data Scraper:
`refer this link https://chrome.google.com/webstore/detail/instant-data-scraper/ofaokhiedipichpaobibbnahnkdoiiah?hl=en-US`

## EXECUTION - How to run a demo on our code
### A. Download all datasets:
#### School rating data: 
1. Run scrape_census_school_districts.ipynb to scrape and clean data about school districts within each county from https://www.census.gov/geographies/reference-maps/2020/geo/2020pl-maps/2020-schdist-map.html <br />
`Open scrape_census_school_districts.ipynb and click Run All Cells`
2. Use Chrome Instant Data Scraper to extract school district rating data for each state from https://www.niche.com/k12/search/best-school-districts/  
3. Run ombine_niche_and_censu.ipynb to clean school rating data and combine it with school districts data <br />
`Open combine_niche_and_census.ipynb and click Run All Cells`

#### Demographics data: 
Downloaded from the American Community Survey website using their API through a python script. This API call provides us with majority of the datasets used in our dashboard such as Age, Population, Housing Prices, Race Information, Male/Famale population, housing prices and other demographic related variables. 
`ACS_data_collection_using_API_call.py`
1. The API key can be created at https://api.census.gov/data/key_signup.html. The key created for the user pkalan3 is included in the code. 
2. It takes a lot of time to download the entire dataset due to slow API response, so the parameters were separated into 5 different groups (mentioned in the script), each group was added to a separate instance of the same script and then all the instances were ran in parallel to reduce overall time. The downloaded tables were joined in the last step given below.

#### Grocery availability data: 
Downloaded from https://www.openicpsr.org/openicpsr/project/123001/version/V1/view?path=/openicpsr/123001/fcr:versions/V1.4/NaNDA_Grocery_Stores_by_Census_Tract_2003-2017_v1-1.pdf&type=file

#### Parks availability data: 
Downloaded from https://www.openicpsr.org/openicpsr/project/117921/version/V1/view

#### Crime data: 
Downloaded from the following website: https://crime-data-explorer.app.cloud.gov/pages/explorer/crime/crime-trend

#### Geojson file with polygon information for each geoid:
This file can be downloaded from the following website after free account creation: https://docs.safegraph.com/docs/geometry-data

### B. Clean the datasets:
Each dataset was cleaned in OpenRefine to remove the missing values issue and create a common key to join them later as given below.

### C. Integrate all the datasets in a single database.
Each dataset has different granularity in terms of GEOID. For example, the demographics datasets are till Block Group level while some other datasets are till Tract or County levels. We have decided to use the granularity till the Block Group level for our project because it is the smallest geographical unit for which the census bureau publishes sample data. So the individual datasets are integrated by running following Jupyter Notebook:
`Process_database_notebook_ver2.ipynb`


### D. Conversion of merged dataset into geopandas object
After each single dataset was merged and integrated into one database, they were converted to geopandas dataframe using geopandas library in python. Additionally, in this step, a geoid master dataset was used to obtain exact polygon locations of each geoid in the integrated dataset. Also, school rating data was added to our final dataset in this step as well. The python script for this step is named "lonlat_to_geoid_polygonspy.py". 
The output of this step is a geopandas object which can be stored and later become imported by Tableau as a Spatial object. 

### E. Importing of Geopandas object to Tableau and Visualization
After step D was performed, the output geopandas dataset was imported in Tableau as a Spatial object and the final dashboard was created. The Tableau file for this step is called "House Hunting Dashboard_Final.twb" and contains the visualization and dashboard for this tool. After the dashboard was built, it was published to Teablau Public which is the cloud environmen for deploying Tableau dashboards to the web. From there, an embedded link was obtained and used in creation of https://neighborhoodsearch.net webpage where our application can be used online!







