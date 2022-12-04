# team163
Understanding CSE6242 Project Repository

## DESCRIPTION

DOC folder includes final project report and final poster <br />
CODE folder includes one .twb file showing our final product and a few .ipynb files showing how we scraped and cleaned data

## INSTALLATION - How to install and setup our code

### Install Jupyter Notebook:
`pip install notebook`

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

### Run School Data Jupyter Notebooks to scrape and clean data regarding school rating:
`Open scrape_census_school_districts.ipynb  and click Run All Cells`
`Open combine_niche_and_census.ipynb and click Run All Cells`

### Download demographics data from the American Community Survey website using their API. 
`ACS_data_collection_using_API_call.py`
1. The API key can be created at https://api.census.gov/data/key_signup.html. The key created for the user pkalan3 is included in the code. 
2. It takes a lot of time to download the entire dataset due to slow API response, so the parameters were separated into 5 different groups (mentioned in the script), each group was added to a separate instance of the same script and then all the instances were ran in parallel to reduce overall time. The downloaded tables were joined in the last step given below.

### Each dataset was cleaned in OpenRefine to remove the missing values issue.

### Integrating all datasets in a single database.
1. Each dataset has different granularity in terms of GEOID. The demographics datasets are till Block Group level while some other datasets are till Tract or County levels. So they are integrate by running following Jupyter Notebook:
`Process_database_notebook_ver2.ipynb`
