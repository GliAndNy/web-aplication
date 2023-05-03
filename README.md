# web-aplication
This application is a tool for primary data analysis. To run this program, you need to run the following code from the command line: py project.py or python3 project.py. Next, follow the link:
http://127.0.0.1:8050/
On the main page of the dashboard, there are 3 main pages for analysis: 1) Initial Data; 2) Analytical Graphs; 3) Table 1.

1.Initial Data
This page displays the uploaded dataset. In this case, the “Houses” data is examined (link: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data). The initial data set is too large, so only a few indicators were selected for analysis:
1) Neighborhood - areas of the city of Ames, Iowa, where the house for sale is located;
2) GarageType - type of parking space, garage (attachd - attached, detchd - separate, BuiltIn - connected to the house);
3) HouseStyle - number of floors and type of house;
4) LotArea - lot area in feet;
5) OverallQual - assessment of the quality of the repair (from 0 to 10);
6) YearBuilt - year of construction;
7) SalePrice - the price of the site.
This first page allows the user to view the available data and filter it if necessary.

2. Analytical Graphs
This page is an interactive interface for building analytical charts of various types. The first graph is a scatter plot showing the relationship between two variables - X and Y. You can select variables from the corresponding cells. For example, let's choose the area of the plot along the X axis, and the cost of the plot along the Y axis.

   All these conclusions can be obtained by the user by selecting the appropriate variables.
The application user also has the opportunity to study the histograms by selecting the desired variable (an example with years of construction):
You can also build graphs on which you can see obvious deviations:

 
The same can be done for other variables.
The next type of chart is the bar charts:

 
3.Table 1
On the next page of Table 1, the user can explore the data for writing text reports.
It is more convenient to draw semantic conclusions based on the page with analytical graphs, but here it is more convenient to give specific values for a detailed description of the results.
