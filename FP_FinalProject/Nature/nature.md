# 14.3 Nature

Many of you will need to analyze some data. The final project is based on that premise.

In this assignment, you will write the code to analyze a data set and produce reports. The provided main program implements a simple command-line interpreter that requests the name of the file containing the data and the reports you wish to generate, one report at a time. You must write one module to analyze the data, endangeredanalysis.py, and another module that prints a report from an analysis, endangeredreport.py.

## Grading

There are multiple labs to choose from for the final program. You only need to complete one of the labs from this chapter for the final program. If you attempt more than one lab, only the highest lab score will be used for grading purposes.

Grading for this lab is based on five report test cases worth 20 points each. You can only see the output from the first test case when you submit. You must compute the results from the input data in your program. You cannot simply print strings containing values you obtained by other means since we will be using a different file for testing.

## Assignment

Have you ever been to New York? We are studying the plants and animals of New York and reporting on their New York Listing Status (only Endangered, Rare, or Threatened). We would like to see the data organized in the following ways.

- Category
- County
- Taxonomy Group
- Taxonomy Subgroup
- Common Name

The report will look something like this. There should be a line for each item, even if it's values are all zeros. The lines should be sorted by the name in the last column. Each line of data contains the following columns:

- the number of endangered species
- the number of rare species
- the number of threatened species
- the total number of endangered, rare, and threatened species
- the category, county, taxonomy group, taxonomy subgroup, or common name

The last line of each table should contain the simple arithmetic average for each column, `(n1+n2+n3)/3`. Do not round the average.
The data shown here is for illustration. Some data has been omitted (...).

```python
filename?
endangeredtest.csv

report?
category
Endangered       Rare Threatened      Total Category
        43          0         50         93 Animal
       213         92        174        479 Plant
       128         46        112        286 Average


report?
county
Endangered       Rare Threatened      Total County
...


report?
taxonomy group
Endangered       Rare Threatened      Total Taxonomy Group
...


report?
taxonomy subgroup
Endangered       Rare Threatened      Total Taxonomy Subgroup
...


report?
common name
Endangered       Rare Threatened      Total Common Name
...

report?
```

## Data file

The endangered species dataset lists Endangered or Threatened animals and plants that have been seen in New York. It's a large file, with 1 header line and 5819 lines of data. The endangeredtest.csv file contains a subset of the data (576 lines) that you may use for development. We will use a different file for grading. The format of this data is County, Category, Taxonomic Group, Taxonomic Subgroup, Scientific Name, Common Name, Year Last Documented, NY Listing Status, Federal Listing Status, State Conservation Rank, Global Conservation Rank, Distribution Status. Here are a few lines from the start and end of the file.

```txt
County,Category,Taxonomic Group,Taxonomic Subgroup,Scientific Name,Common Name,Year Last Documented,NY Listing Status,Federal Listing Status,State Conservation Rank,Global Conservation Rank,Distribution Status
Albany,Animal,Birds,Wrens,Cistothorus platensis,Sedge Wren,1991,Threatened,not listed,S3B,G5,Recently Confirmed
Albany,Animal,Mammals,Rodents,Neotoma magister,Allegheny Woodrat,not available,Endangered,not listed,S1,G3G4,Extirpated
...
Yates,Plant,Flowering Plants,Sedges,Carex lupuliformis,False Hop Sedge,not available,Threatened,not listed,S2,G4,Historically Confirmed
Yates,Plant,Flowering Plants,Sedges,Carex sartwellii,Sartwell's Sedge,not available,Endangered,not listed,S1S2,G4G5,Historically Confirmed
```

The file contains the following columns.

- County
- Category
- Taxonomic Group
- Taxonomic Subgroup
- Scientific Name
- Common Name
- Year Last Documented
- NY Listing Status
- Federal Listing Status
- State Conservation Rank
- Global Conservation Rank
- Distribution Status

For this report, we are only concerned with the columns: County, Category, Taxonomic Group, Taxonomic Subgroup, Common Name, and NY (New York) Listing Status. The other attributes should not be reported.

## Programming

This program will require you to work with modules, global variables, CSV files, and nested dictionaries. The assignment has three files:

- `main.py` is a script containing the main program. It is provided for you and you may not change it. There are several calls to functions in the `endangeredanalysis.py` and `endangeredreport.py` modules that you must implement.
- `endangeredanalysis.py` is a module that you must write to analyze the file and return the requested analyses.
- `endangeredreport.py` is a module that you must write to print a report for the different analyses.
The file is very large so you should only read it once. It is expected that you will complete the analysis as you read the file and place the results in dictionaries during the init function. The other functions can simply return the dictionaries you created in the init function.

You will be writing two modules. The modules should only define global variables and functions. The modules should not have a main or call any of their functions at the top level.

> [!TIP]
> As a convention, you might want to start all of the global variables in the module with an _ (underscore) so they will stand out. This will be a useful place to hold the dictionaries you create during analysis.

You need to implement below functions for endangeredanalysis.py:

1. `init()` - This function should parse your CSV file and read all the lines. Lines read by this function should be reused by the rest of the functions. In this way, you avoid reading the file multiple times for each of your functions.
1. `county()` - Should return a dictionary containing an entry for each county containing a count of species in each NY Listing Category.
1. `category()` - Should return a dictionary containing an entry for each category containing a count of species in each NY Listing
1. `group()` - Should return a dictionary containing an entry for each Taxonomic Group containing a count of species in each NY Listing
1. `subgroup()` - Should return a dictionary containing an entry for each Taxonomic Subgroup containing a count of species in each NY Listing
1. `common()` - Should return a dictionary containing an entry for each Common Name containing a count of species in each NY Listing

You need to implement the below functions for endangeredreport.py:

1. `status()` - Should take an analysis dictionary as a parameter and print the tabular report for each element in the dictionary, sorted alphabetically.
The key to this assignment is creating dictionaries for analysis as you read the data. The dictionaries must all have the same format since there is a single routine used to print the different reports.
