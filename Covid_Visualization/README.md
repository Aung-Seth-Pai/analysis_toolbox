# Covid-19 Data Exploration

#### Overview 
   A Covid-19 information dashboard using data from 2020 Jan to 2022 Feb period using Tableau Public. Current visualization shows the pandemic situations and vaccination efforts with historical aggregates of fatality rates, cases, tests and vaccinations globally.
    
Link To Dashboard: https://public.tableau.com/app/profile/aung.seth.pai/viz/Covid_Dashboard_16437951240240/Dashboard1_1
        
#### The Data
   Two datasets containing information about the daily Covid-19 cases across the world, deaths, hospitalization, vaccinations, infection rates, and population demographics are used. Data is available at https://ourworldindata.org/coronavirus. 

#### Workflow
   I am using the free browser version of Tableau currently, and therefore, the data pipeline is somewhat manual. Data aggregations are done in the JupyterNotebook environment using the sqlite3 Python library. It connects to the local SQLite database and displays the query results using Pandas' data frame. The results are then saved as CSV files and uploaded to my Tableau Public account for visualizations. Since the query results are also available as Pandas data frame, one can use Matplotlib or Seaborn visualization libraries instead of the browser version of Tableau.
   
#### References
1. https://www.youtube.com/watch?v=qfyynHBFOsM&list=PLUaB-1hjhk8H48Pj32z4GZgGWyylqv85f&index=1
2. https://ourworldindata.org/covid-deaths