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

## EXECUTION - How to run a demo on our code
### A. Download all datasets:
#### School rating data: 
Run School Data Jupyter Notebooks to scrape and clean data:
`Open scrape_census_school_districts.ipynb  and click Run All Cells`
`Open combine_niche_and_census.ipynb and click Run All Cells`

#### Demographics data: 
Downloaded from the American Community Survey website using their API through a python script. 
`ACS_data_collection_using_API_call.py`
1. The API key can be created at https://api.census.gov/data/key_signup.html. The key created for the user pkalan3 is included in the code. 
2. It takes a lot of time to download the entire dataset due to slow API response, so the parameters were separated into 5 different groups (mentioned in the script), each group was added to a separate instance of the same script and then all the instances were ran in parallel to reduce overall time. The downloaded tables were joined in the last step given below.

#### Grocery availability data: 
Downloaded from https://www.openicpsr.org/openicpsr/project/123001/version/V1/view?path=/openicpsr/123001/fcr:versions/V1.4/NaNDA_Grocery_Stores_by_Census_Tract_2003-2017_v1-1.pdf&type=file

#### Parks availability data: 
Downloaded from https://www.openicpsr.org/openicpsr/project/117921/version/V1/view

#### Crime data: Downloaded from the FBI website.

### B. Clean the datasets:
Each dataset was cleaned in OpenRefine to remove the missing values issue and create a common key to join them later as given below.

### C. Integrate all the datasets in a single database.
Each dataset has different granularity in terms of GEOID. For example, the demographics datasets are till Block Group level while some other datasets are till Tract or County levels. We have decided to use the granularity till the Block Group level for our project because it is the smallest geographical unit for which the census bureau publishes sample data. So the individual datasets are integrated by running following Jupyter Notebook:
`Process_database_notebook_ver2.ipynb`


### D. Conversion of merged dataset into geopandas object
After each single dataset was merged and integrated into one database, they were converted to geopandas dataframe using geopandas library in python. Additionally, in this step, a geoid master dataset was used to obtain exact polygon locations of each geoid in the integrated dataset. Also, school rating data was added to our final dataset in this step as well. The python script for this step is named "lonlat_to_geoid_polygonspy.py". 
The output of this step is a geopandas object which can be stored and later become imported by Tableau as a Spatial object. 

### E. Importing of Geopandas object to Tableau and Visualization
After step D was performed, the output geopandas dataset was imported in Tableau as a Spatial object and the final dashboard was created. The Tableau file for this step is called







