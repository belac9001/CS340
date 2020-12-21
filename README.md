# README

## About the Project

The purpose of this dashboard is to allow for visualization from the AAC animals database collection. The data from the database is listed into a dataframe on the dashboard, filterable based on rescue types (criteria provided by Grazioso). Below the dataframe is a geolocation chart. The location of the animal selected in the dataframe is pinpointed and shown to the user. Finally, there is a pie chart that displays each rescue type category, divided by breeds.

## Motivation

The purpose of this dashboard is to allow for visualization from the AAC animals database collection. Another goal of the project was to provide data interactivity for the users, which is done through the filtering dropdown box and row selection.

## Getting Started

To use the dashboard, simply run the code in the FinalProject.ipynb file. The default filtering criteria loaded is water\_rescue, however this can be changed with the dropdown box.

## Tool Used/Installation

Python and PyMongo must be installed to run these scripts. See:

**Python** -- [https://www.python.org/downloads/](https://www.python.org/downloads/)

Backend language for the dashboard

**PyMongo** --[https://pymongo.readthedocs.io/en/stable/installation.html](https://pymongo.readthedocs.io/en/stable/installation.html)

MongoDB and Python were used in combination as it allows us to work with databases without the use of SQL. PyMongo was used as it has extensive documentation and a fleshed-out API available for developers.

**Dash** -- [https://dash.plotly.com/installation](https://dash.plotly.com/installation)

The Dash framework also has great documentation and allowed us to get the data very easily from the MongoDB database onto the frontend of the website. Dash allowed for easy interactivity between the HTML/CSS and Python code.

**Pandas** -- [https://pandas.pydata.org/](https://pandas.pydata.org/)

Pandas was used for visual display of the data, namely with the dynamic pie chart.

## Usage

Upon running:

![image](https://user-images.githubusercontent.com/53846457/102739046-ce971180-4300-11eb-9172-25d4ed588dec.png)

To filter the data, simply click the dropdown box for filter options.

![image](https://user-images.githubusercontent.com/53846457/102739072-e40c3b80-4300-11eb-8734-eb04ee98e0b9.png)

To select an animal, click the radio button on the left hand side of the data table. This will also show the location of the animal.

![image](https://user-images.githubusercontent.com/53846457/102739090-f1c1c100-4300-11eb-8f93-6486b270ed9b.png)

Filtering the data will also display the breed breakdown in the pie chart.

![image](https://user-images.githubusercontent.com/53846457/102739105-fedeb000-4300-11eb-934d-83c0eebd7eb6.png)

## Final Submission Prompts

**Readable Code**
For writing readable code, I try to keep naming conventions and indentation consistent. Commenting on functions or methods explaining the purpose, parameters, and return values can be helpful, however comments should only be added if necessary (a function named getAddress doesn't need a comment explaining functionality). Another thing that I try to do that really helps code be readable is avoiding deep nesting. 

**Problem Solving**
For moments when I'm stuck, I like to break every aspect of the problem down and try to work it out. An example with the dashboard, I was having trouble getting a pie chart to display properly. I created a temporary div to display data returned from the pie chart function. In the pie chart function, I returned several types of data just to see how it could be manipulated, what the type of each object was, and what each object contained. Doing this allowed me to pinpoint exactly what I needed to do to get the pie chart working properly.

**What do computer scientists do**
Computer scientists, in my opinion, essentially create solutions to problems. For the Grazioso Salvare company, they needed a better way to work with and visualize their data. The solution to this problem was to create an interactive dashboard that allows filtering, viewing, and geolocation of the data types. I feel like problem solving is essentially what computer science boils down to (albeit in different scopes depending on the project). 

## Contact 

Your name: Caleb Dederick, [caleb.dederick@snhu.edu](mailto:caleb.dederick@snhu.edu)
