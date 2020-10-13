# 14.1 Final Program Instructions

The Final Program lets you analyze data acquired from different sources in the common comma-separated-vaues format.  

- The main program is provided for you and cannot be modified.
- You must write two different modules that the main program imports.  
- One module analyzes the data.
- One module reports the analysis of the data.

You only need to complete one of the available programs.
You are welcome to complete others for practice, but only the highest score on the individual programs will count towards the grade.  We do not add the scores from multiple programs.

## 14.2 Know your population

Many of you will need to analyze some data. The final project is based on that premise.

In this assignment, you will write the code to analyze a data set and produce reports. The provided main program implements a simple command-line interpreter that requests the name of the file containing the data and the reports you wish to generate, one report at a time. You must write one module to analyze the data, diversityanalysis.py, and another module that prints a report from an analysis, diversityreport.py.

## Grading

There are multiple labs to choose from for the final program. You only need to complete one of the labs from this chapter for the final program. If you attempt more than one lab, only the highest lab score will be used for grading purposes.

Grading for this lab is based on five report test cases worth 20 points each. You can only see the output from the first test case when you submit. You must compute the results from the input data in your program. You cannot simply print strings containing values you obtained by other means since we will be using a different file for testing.

## Assignment

Are you curious about registration trends at Colorado State University? The university analyzes demographic information to understand trends in the student population so it can better focus its efforts to recruit and retain students. This demographic information could include gender and ethnicity. The data for this lab only includes gender information, so we would like to report the gender registration trends at CSU for these categories.

- Total
- College
- Department
- Major
- Term

The reports will look something like this. The lines should be sorted by the text in the last column. Each line of data contains the following columns:

- the number of female students.
- the number of male students.
- the ratio of female to male students.
- the category (college, department, major, term, or gender)

The data shown here is obviously for illustration and not the correct values. Some data has been omitted

```python
file?

report?
total

     F      M  F/M Total
 12345  12345 1.00 Gender

report?
college

     F      M  F/M College
 12345  12345 1.00 Natural Sciences
 12345  12345 1.00 Walter Scott College of Engr

report?
department

     F      M  F/M Department
...

report?
major

     F      M  F/M Major
...

report?
term

     F      M  F/M Term
...

report?
```

## Data file

The gender diversity dataset looks at major enrollment at Colorado State University. It's a large file, with 1 header line and 26854 lines of data. The gendertestdata.csv file contains a subset of the data (2675 lines) for recent semesters that you may use for development. We will use a different database for grading. Here are the first few lines from the start and end of the file.

```python
PRIMARY_COLLEGE,PRIMARY_COLLEGE_DESC,PRIMARY_DEPARTMENT_DESC,PRIMARY_MAJOR_DESC,TERM,GENDER
EG,Walter Scott College of Engr,Mechanical Engineering,Mechanical Engineering,201790,M
EG,Walter Scott College of Engr,Civil and Environmental Engr,Civil Engineering,201790,M
NS,Natural Sciences,Psychology,Psychology,201790,M
NS,Natural Sciences,Physics,Physics,201790,M
NS,Natural Sciences,Psychology,Psychology,201790,F
..26844 lines omitted
NS,Natural Sciences,Biology,Biological Science,201910,M
EG,Walter Scott College of Engr,Walter Scott College of Engr,Biomedical Engineering with ME,201910,M
EG,Walter Scott College of Engr,Civil and Environmental Engr,Environmental Engineering,201910,F
EG,Walter Scott College of Engr,Electrical and Computer Engr,Electrical Engineering,201910,M
EG,Walter Scott College of Engr,Walter Scott College of Engr,Biomedical Engineering with ME,201910,M
```

The following columns are set up in the CSV.

- PRIMARY COLLEGE
- This has a value of either NS or EG
- PRIMARY COLLEGE DESC
- Paired with Natural Science or Engineering
- PRIMARY DEPARTMENT DESC
- The department in which the major is hosted, for example, the Computer Science department has both Applied Computing Technology and Computer Science majors
- PRIMARY MAJOR DESC
- The name of the major. This does not include concentrations (just some major labs are very descriptive in engineering)
- TERM
- The term in which this data is pulled. It is the year, term (by start month), and 0 - For example:
- 201890 - Is Fall (September) 2018
- 201610 - Is Spring 2016
- 201760 - Is Summer 2017
- GENDER
- M or F. It is safe to assume all of them have an M or F due to how CSU currently handles the data. For those interested, there is an effort to support non-binary gender in future years, but as this is ‘historic' data, it is still stored as the binary descriptors.

## Programming

This program will require you to work with modules, global variables, CSV files, and nested dictionaries. The assignment has three files:

- `diversity.py` is a script containing the main program and all printing. It is provided for you and you may not change it. There are several calls to functions in the diversityanalysis.py and diversityreport.py modules that you must implement.
- `diversityanalysis.py` is a module that you must write to analyze the file and return the requested analyses.
- `diversityreport.py` is a module that you must write to print a report for the different analyses available. The file is very large so you should only read it once. It is expected that you will complete the analysis as you read the file and place the results in dictionaries during the init function. The other functions can simply return the dictionaries you created in the init() function.

You will be writing two modules. The modules should not have a main or call any of their functions at the top level. The module should only define global variables and functions. Hint: a global variable is useful in diversityanalysis.py.

The function specifications for this assignment are intentionally vague, as it's largely up to you to decide how to implement this code, though you're welcome to ask the TA's for advice. You may implement extra helper functions to further break down the assignment, if you'd like.

You must implement these functions in diversityanalysis.py:

- `init(filename)` - Parse the CSV file and read all the lines. Lines read by this function should be reused by the rest of the functions. In this way, you avoid reading the file multiple times for each of the other functions.

- `total()` - Return a dictionary containing for entire M and F population in the school.

- `college()` - Return a nested dictionary for each of the colleges in the school with it's respective M and F population.

- `department()` - Return a nested dictionary for each of the departments in the school with it's respective M and F population.

- `major()` - Return a nested dictionary for each of the majors in the school with it's respective M and F population.

- `term()` - Return a nested dictionary for each term in the school with it's respective M and F population.

You must implement this function in diversityreport.py:

- `gender(title, data)` - Print a report in the format shown above, with the last column sorted alphabetically.
The key to this assignment is creating dictionaries for analysis as you read the data. The dictionaries must all have the same format since there is a single routine used to print the different reports.
