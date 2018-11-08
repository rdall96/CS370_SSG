##Ricky Dall'Armellina
####CS 350 HOMEWORK & PROJECTS

<!-- homework sections -->

<!-- HOMEWORK #1 -->
####HOMEWORK #1

 * Setup Website: DONE!
 * Create Database: db4free.dallarr_sunypoly
 * Created a table: CS350_HW1
 * Inserted data
 * Ran some search operations

Here are some images demonstrating the process.

![console_log](hw1IMG01)
![insert_data](hw1IMG02)
![search_1](hw1IMG03)
![search_2](hw1IMG04)
<br/>

<!-- HOMEWORK #2 -->
####HOMEWORK #2

__HW2_ELMASRI_DATABASE__

Company database from the textbook

 * Created Database
 ![hw2_tables](hw2IMG01)
 * Ran some queries. Tested the database in different tables
 
 ![query1_employee](hw2IMG02)
 ![query2_dependent](hw2IMG03)
 ![query3_works_on](hw2IMG04)
 ![query4_hours_employees](hw2IMG05)
 
 __HW2_RELATIONAL_MODEL__
 PROBLEM 3.19 Answers

 * a. The phone number is missing the area code and the country code
 * b. This information should be stored in local and cell phone separately, so you can be sure you have the correct values.
 * c. The main advantage of splitting this attribute into first last and middle initial is that you can the sort alphabetically by any of these. A couple disadvantages could be the need of more memery to store these extra attributes and the user needs to input more data separately.
 * d. I would keep a field single when the amount of data in it is not much, usually a single string or for example an address. I would divide the data up instead, when the contents of that attribute start to become a much longer and more complex set of data.
 * e. The easiest way to approach this would be to only allow two phone fields. The best one, however, is to create a separate table for phone numbers linked by a unique ID to each respective student.

__HW2_SQL__
PROBLEM 4.12 Answers

 * a. SELECT 'Name' FROM 'STUDENT' WHERE 'Major' = 'CS'
 * b. SELECT 'Course_name' FROM 'SECTION' WHERE 'Instructor' = 'King' AND ('Year'='07' OR 'Year'='08')
 * c. SELECT 'Course_number', 'Semester', 'Year', 'Student_number' FROM 'SECTION', 'GRADE_REPORT' WHERE 'Instructors' = 'King'
 * d. SELECT 'Name', 'Course_name', 'Course_number', 'Credit_hours', 'Semester', 'Year', 'Grade' FROM 'STUDENT', 'COURSE', 'GRADE_REPORT' WHERE 'Class' = '4' AND 'Major' = 'CS'
<br/>

<!-- HOMEWORK #3 -->
####HOMEWORK #3

Did some operations on the the company database from the textbook. Set some Dnum in 'PROJECTS' to NULL and then joined it with 'EMPLOYEE' with a specific project name to see the differences.

![productz_employees_Dnum](hw3IMG01)
![select_employee](hw3IMG02)
![select_project](hw3IMG03)
![update_null](hw3IMG04)
<br/>

<!-- HOMEWORK #4 -->
####HOMEWORK #4

Problems on book database

[SQL Commands for homework](hw4file)
<br/>

<!-- HOMEWORK #5 -->
####HOMEWORK #5

Problems on book database

[Answers and SQL Commands](hw5file)
<br/>

<!-- HOMEWORK #6 -->
####HOMEWORK #6

Problems 7.19 p.235 and 8.29 p.282

[Problem 7.19 Answers](hw6file1)

[ER Model diagram](hw6file2)
<br/>

<!-- HOMEWORK #7 -->
####HOMEWORK #7

>(to be added soon)
<br/>

<!-- MINI PROJECT -->
####MINI PROJECT

This is the Mini Project for CS 350.
Given the size of this project, it was developed in collaboration with Steven Savold.
The project consists in a web-based grocery store database (XML DB) with functionality to view, edit and delete items.

Github project page: [CS350_MiniProject](https://github.com/rdall96/CS350_MiniProject)

[Grocery Store DB](https://web.cs.sunyit.edu/~dallarr/courses/cs350/mini_project/index.html)
