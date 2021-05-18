# Project 5
# *Air Pollutants and Air Quality Index*


## Contents
 - [Problem Statement](#Problem-Statement)
 - [Executive Summary](#Executive-Summary)
 - [File Directory](#File-Directory)
 - [Data](#Data)
 - [Data Dictionary](#Data-Dictionary)
 - [Conclusions and Recommendations](#Conclusions-and-Recommendations)
 - [Areas for Further Research/Study](#Areas-for-Further-Research/Study)
 - [Sources](#Sources)
 - [Visualizations](#Visualizations)


## Problem Statement
[back to top](#Project-5)

We plan to explore the relationship between certain pollutants that are more likely to cause dangerously high air quality scores. We will be doing this using information based on EPA data from Cleveland, OH and presenting this to residents of Cleveland, OH.


## Executive Summary
[back to top](#Project-5)

### *This section should include:*
 - *a brief overview of your process*
 - *models used*
 - *important findings and/or*
 - *metrics, model performance, etc.*
 - *and a brief summary of conclusions and recommendations.*


## File Directory
[back to top](#Project-5)
### *Files should be clearly labeled with descriptive names*
05-Project<br />
|<br />
|__ code<br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 00_table_of_contents.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 01_eda_and_cleaning.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 02_technical_analysis.ipynb <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 03_conclusion.ipynb <br />
|<br />
|__ data <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_CO.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_NO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_O3.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_Pb.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_PM10.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_PM2.5.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_all_cleveland_oh_SO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_clean_cleveland_oh_CO.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_clean_cleveland_oh_NO2.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_clean_cleveland_oh_O3.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_clean_cleveland_oh_Pb.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_clean_cleveland_oh_PM10.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_clean_cleveland_oh_PM2.5.csv <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ 2017_clean_cleveland_oh_SO2.csv <br />
|<br />
|__ images <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ nothing.png <br />
|<br />
|__ presentation <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ presentation.pdf <br />
|&nbsp;&nbsp;&nbsp;&nbsp;|__ presentation.pptx <br />
|<br />
|__ README.md <br />


## Data
[back to top](#Project-5)
 - *Write a sentence or two about the source of your data. If you are not including your data in the repo share a link to your data source.*
 - *Include all features in your final cleaned csv/file*
 - *Include engineered features*


## Data Dictionary
[back to top](#Project-5)

| Feature            | Python Type | Data Type  | Descritpion   |
| ---                | ---         | ---        | ---           |
| date (index)       | datetime    | Continuous | Date when observations were made  |
| high_temp          |   int64     | Continuous | Highest Temperature measured for the day (in degrees Fahrenheit) |
| low_temp           |   int64     | Continuous | Lowest Temperature measured for the day (in degrees Fahrenheit) |
| co_max             | float64     | Continuous | Amount of Carbon Monoxide measured in ppm |
| co_aqi_val         | float64     | Continuous | AQI value of Carbon Monoxide |
| no2_max            | float64     | Continuous | Amount of Nitrogen Dioxide measured in ppb |
| no2_aqi_val        | float64     | Continuous | AQI value of Nitrogen Dioxide |
| ozone_max          | float64     | Continuous | Amount of Ozone measured in ppm |
| ozone_aqi_val      | float64     | Continuous | AQI value of Ozone |
| pm10_mean          | float64     | Continuous | Average amount of 10um Particulate Matter measured in ug/m^3 |
| pm10_aqi_val       | float64     | Continuous | AQI value of 10um Particulate Matter |
| pm2.5_mean         | float64     | Continuous | Average amount of 2.5um Particulate Matter measured in ug/m^3 |
| pm2.5_aqi_val      | float64     | Continuous | AQI value of 2.5um Particulate Matter |
| so2_max            | float64     | Continuous | Amount of Sulfur Dioxide measured in ppb |
| so2_aqi_val        | float64     | Continuous | AQI value of Sulfur Dioxide |
| cumulitive_aqi     | float64     | Continuous | Calculated AQI for the day by taking the maximum value from all pollutants |
| pct_change_aqi     | float64     | Continuous | Percent changed in AQI from previous day |
| average_daily_temp | float64     | Continuous | Calculated Average Temperature (in degrees Fahrenheit; Mean of Highest and Lowest Temperatures) |
| month              | float64     | Nominal    | Month denoted by numeric value one through twelve |
| weekday            | float64     | Nominal    | Day of the week, assuming the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6 |




## Conclusions and Recommendations
[back to top](#Project-5)


## Areas for Further Research/Study
[back to top](#Project-5)


## Sources
[back to top](#Project-5)

https://www.epa.gov/outdoor-air-quality-data/download-daily-data
https://www.cleveland.com/datacentral/2008/09/cleveland_weather_history_find.html
https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf
https://www.epa.state.oh.us/portals/27/ams/plans/NCORE-GTCraig.pdf


## Visualizations
[back to top](#Project-5)
- *Any important visualizations*
- *These can be included in the Executive Summary or Conclusions/Recommendations, or as its own section.*
- *Use good judgement! Include a few here that really highlight your findings.*


