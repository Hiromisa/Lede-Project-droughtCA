# Lede-Project-droughtCA
---
This is a project for Lede week3. I analyzed the current California drought situation.

I've updated my project for week2 with Jupyter/pandas data analysis. I've modified/changed some graphs based on my research.


---
## Project: Every Californian life in a Drought area

https://docs.google.com/document/d/116q_W8dOJqqMwvCnesG1kMMALefLzvQBVX5WhUBlwt8/edit?usp=sharing

---
## Data

ca.csv and droughtCAnow.csv come from [The U.S. Drought Monitor](https://droughtmonitor.unl.edu/DmData/DataDownload/ComprehensiveStatistics.aspx)

ca.csv contains a table that shows California's drought level between June 2011 to June 2021.

droughtCAnow.csv is a table of each county's drought level as of June 15, 2021.

I merged/filtered some data on them with Jupyter/pandas, 
then created new CSV files called fca.csv, fdrought.csv, worst10.csv to illustrate a graph, a map, and a table.

I re-used the graph, which I created last week for the previous project. It shows California's wildfire trend since 1988. 
I got data from [Cal Fire](https://www.fire.ca.gov/stats-events/)

---
## Analysis

The droughtca.ipynb notebook contains my analysis, written in Python. Relevant outputs can be found there.

I analyzed how many counties face extreme/exceptional drought.

However, I decided to create a map and a table with just the percent area of exceptional drought (= most critical level).

I also calculated some numbers and quoted them in my article.

---
## Reproducibility

The code running the analysis is written in Python 3 and requires pandas．

pandas for data loading and analysis

Jupyter to run the notebook infrastructure


