title: Beginning SQL cont. 
date: 2021-01-12
modified: 2021-01-17
category: SQL
tags: sql, Udemy,
slug: sql-practice
author: cmsato09
status: published

## Post #10 Udemy MySQL bootcamp course

Continuing from the previous post, I got through most of [The Ultimate MySQL Bootcamp: Go from SQL Beginner to Expert](https://www.udemy.com/course/the-ultimate-mysql-bootcamp-go-from-sql-beginner-to-expert/). In the previous post, I went through some of the basic SQL commands on creating, inserting, and viewing data.

### Other topics
* Logical operators -- these were similar to all python logical operators so easy to understand. 
* Table relations by `JOIN`
    * One-to-Many -- one column in one table related to many columns in another table
    * Many-to-Many -- one table connecting at least two different tables together and acting as a bridge

Logical operators section had some functions that I hadn't seen in python like the `BETWEEN` operator and `CASE` statements (which are similar to if-else statements).
Join tables was interesting to learn as the course used more real-world examples. For the one-to-many tables example, a customers table and orders table was created to show that a customer can have multiple orders, but a order can't usually have multple customers. I learned about `FOREIGN KEY` for creating these tables and I learned how to use `INNER JOIN`, `LEFT JOIN`, and `RIGHT JOIN` to print out info from two different tables. 
In the many-to-many tables example, I worked with a tv series data table and reviewers table that was connected by a reviews table. It was a code-along with exercises to print out specific outputs from the tables provided. 

Finally, a instagram clone with very basic features was created with multiple tables (users, photos, comments, likes, followers, and hashtags) to do more exercises with `JOIN`. Exercises consisted of getting certain outputs like 'find the most liked photo and the user who posted it' and 'top 5 commonly used hashtags.' 

I have not done the last 3 sections of this course since it is about making a webapp using Node.js. I don't know any javascript and I would still like to focus primarily on one programming language, python. I think I'll try doing the last few sections later after becoming more proficient in python or when I have more interest in front-end. 

### Verdict
The Ultimate MySQL Bootcamp was a good introductory course in SQL. I did learn how to use SQL, but I wouldn't call myself a expert on it (definitely still a beginner), but I feel more confident about writing SQL code for datatables I may see in the future. I didn't feel like I learned about MySQL though. The set-up was already sort of taken care of by goormIDE and the only command I used was `mysql-ctl cli`. I think the last 3 sections with Node.js would've covered more on MySQL set-up and using it together with a different programming language. 
I still think this was a good $11-12 investment. The course was easy to understand and the exercises were helpful. I think I now know enough to branch out and look for how to use SQL with python. 