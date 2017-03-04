#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# How many data points (people) are in the dataset?
print "Length of Enron Data: ", len(enron_data)
print "number of keys in Enron Data: ", len(enron_data.keys())

# For each person, how many features are available?
print "How many features does each person have? ", len(enron_data[enron_data.keys()[0]].keys())

# How many POIs in data set
pois = 0
for person in enron_data:
    if enron_data[person]['poi'] == True:
        pois += 1
print "This many pois: ", pois

# How many POIs in text file
f = open("../final_project/poi_names.txt")
contents = f.read()
print "How many open parens? ", contents.count('(')
print "How many yesses? ", contents.count('(y')
f.close()

# What is the total value of the stock belonging to James Prentice?
print "James Prentice has this much stock: ", enron_data["PRENTICE JAMES"]["total_stock_value"]

# How many email messages do we have from Wesley Colwell to persons of interest?
print "Wesley Colwell has sent this many emails to POIs: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# What's the value of stock options exercised by Jeffrey K Skilling?
print "Value of stock options exercised by Jeffrey K Skilling?: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Who took home most money
print "Total Payments Jeffrey K Skilling?: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Total Payments Ken Lay?: ", enron_data["LAY KENNETH L"]["total_payments"]
print "Total Payments Andrew Fastow?: ", enron_data["FASTOW ANDREW S"]["total_payments"]

# How many in data set have a quantified salary
salaries = 0
for person in enron_data:
    if enron_data[person]['salary'] != "NaN":
        salaries += 1
print "This many salaries: ", salaries

# How many in data set have email addresses
emails = 0
for person in enron_data:
    if enron_data[person]['email_address'] != "NaN":
        emails += 1
print "This many with email addresses: ", emails

# How many in data set have no total payments
no_totals = 0
for person in enron_data:
    if enron_data[person]['total_payments'] == "NaN":
        no_totals += 1
print "This many with no total payments: ", no_totals
print "That is this percent of total: ", float(no_totals)/len(enron_data)*100, "%"

# How many POIs don't have total payments
pois_no_totals = 0
for person in enron_data:
    if enron_data[person]['total_payments'] == "NaN" and enron_data[person]['poi'] == True:
        pois_no_totals += 1
print "This many POIs with no total payments: ", pois_no_totals
print "That is this percent of total: ", float(pois_no_totals)/len(enron_data)*100, "%"
