# About this project

**_MoneyDog_** is a project I started as a tool myself needed to have a lighter, easier to use interface to monitor my finances. At the beginning I used to do this with a spreadsheet but I had a laptop with very limited resources that struggled to load and manage 'large' spreadsheet files. I thought of using my development + data science skills to build an application that could help me get more juice out of my data without having to depend on a spreadsheet software. This is the result.

### Installation

To install it or play around with:

1. Clone this repository

2. On the cloned directory, setup a virtual environment and activate it:

`$ python3 -m venv venv`
`$ source venv/bin/activate`

3. Install the requirements:

`pip install -r requirements.xt`

4. Run the source file using the python interpreter:

`python3 main.py`

### On this version

Currently, this version has a CLI minimal interface to register new movements of money with 'Concept' and 'Partition' tags. These tags will be useful for the implementation of very nice features later on. 

The new movement entries are saved on a .csv file named by the current month and year by default. A feature will be implemented to provide more flexibility and connection to a SQL database later on.

For now, one gets a result of their current total balance everytime a new movement is added to the 'database' but new exciting query features will be added later along with automated visual reports.

Down below you will encounter the product vision as defined for now.

------------------------------------------------

# Product Vision

A product for young adults who have interest in finance administration but do not have a formal education in finance, they want to have a monitoring center where they can observe and analyze their spendings in order to keep their finances healthy. This means keeping their debts and budgeting under control and detect and suggest areas of improvement according to goal setting. Our customers experience increase in their savings, financial security and financial goals accomplishments.

**Target group**: Young adults with no formal education in finance

**Goals**: Create a fast-paced, minimal solution with realistic recommendations based on personal evidence.

**Needs**: An automatized partner to assist with finance administration

**Value**: It is easier and convenient to have a partner that automatically detects your finance administration areas of opportunity rather than spending time in studying them and analyzing them yourself.

**Key features**: Learn about your highest spendings and debts, get pay-plan automatized solutions and have an observation room of your historical and current detailed balance.
