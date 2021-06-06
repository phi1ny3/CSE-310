# Overview
---
This software is a contact tracer app.  It uses data to feed to create a scatterplot, then using a diameter for infection,
the program ascertains who would have been infected, based on their coordinates in proximity
to the infected person.  The programming language is Python 3.9, and this uses several
external libraries, such as pandas, seaborn, and numPy.


# Development Environment
---
Make sure you have Python 3.8.0 or newer and have numPy, pandas, matplotlib, seaborn, and scikit-learn.
You can install most of these using the following command:

python -m pip install

followed by the library you need

After you've installed the required libraries, open a terminal and browse to the project's root folder. 
Start the program by running the following command.

python Contact Tracing.py

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. 
Select the main module inside the covid_warrior folder and click the "run" icon.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* ["Sumulating an epidemic"](https://www.youtube.com/watch?v=gxAaO2rsdIs)
* ["Contact Tracing Machine Learning Jupyter to API"](https://www.youtube.com/watch?v=OY43iZF0kuo)
* ["How to Specify Scatterplots in Python"](https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/)

## Authors
---
Philip Marvin (mar17118@byui.edu)

link to the demo video:
https://www.youtube.com/watch?v=ROnA3_LBBTM




# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Could implement a prompt to find a specific user, then have it checked against the json if it exists
* Could fix the clusters to show more than 2
* Could add more messages at the start to orient the reader, as well as add more commenting throughout the code