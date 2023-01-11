<!-- Book-Data-Generator -->
<!--
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">


  <h3 align="center">Book-Data-Generator</h3>

  <p align="center">This project is a part of making a system that suggests queries. Here, we mostly worked on making the data set that will be   used in the project.
    <br />
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This project is a part of making a system that suggests queries. Here, we focused mostly on assembling the dataset that will be utilized for the project.

Here's why we created four types of dataset here:
* A relational table populated with tuples. The table is expressed as a CSV file, where each row is a tuple, and the first row contains the names of the fields (attributes). You can assume that there are no NULL values. All the fields of all the tuples have a value. 
* A user set. The set of users is nothing more than a set of ids. This is provided as a file, one user id per line. The file may be empty. 
* A query set, which is a set of queries that have been posed in the past. Each query has a unique query id and its definition (i.e., the set of conditions). The query set is expressed as a CSV file where each line contains the conditions attribute=value separated by comma. The first element of each row is a query id. For example, a row in the query set is: 
Q1821, author=John, genre=fantasy
* A utility matrix User-Query that has for certain combinations of user and query, a value from 1 to 100  indicating how happy that user is with the answer set of that query. This is provided also as a CSV file, where the first row contains a list of query ids separated by comma. Any other row starts with a userId, followed by a set of comma separated fields (as many as the number of query names of the first row). These fields could be empty or have a value between 0 and 100. For example, the first row can be: 
q1, q4, q625, q81671
	and an example of one of the following rows 
user36182, 3,,88,3
Note that the example above has one value missing (the one for the q4 (see the two consecutive commas)


### Built With
* [![Python][https://www.python.org/]][ Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

