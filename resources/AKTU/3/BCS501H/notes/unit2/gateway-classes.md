
## Page 1

# Database Management System

**UNIT 2**
**Relational data model and language**
**Lecture-1**

By PRAGYA RAJVANSHI
B.Tech, M.Tech( C.S.E.)

**Today's Target**
* Constraints in DBMS
* AKTU PYQs

## Page 2

# Constraints in DBMS

**Relational constraints** are the restrictions imposed on the database contents and operations.

They ensure the **correctness of data** in the database.

---

### Types of Constraints in DBMS-
* Domain constraint.
* Tuple Uniqueness constraint.
* Key constraint.
* NOT NULL
* UNIQUE
* DEFAULT
* CHECK

## Page 3

# 1. Domain Constraint

* Domain constraint defines the domain or set of values for an attribute.
* It specifies that the value taken by the attribute must be the atomic value from its domain.

**Student**

| STU_ID | Name | Age |
| :--- | :--- | :--- |
| S001 | Akshay | 20 |
| S002 | Abhishek | 21 |
| S003 | Shashank | 20 |
| S004 | Rahul | A |

---

# 2. Tuple Uniqueness Constraint-

* Tuple Uniqueness constraint specifies that all the tuples must be necessarily unique in any relation.

**Student**

| TU_ID | Name | Age |
| :--- | :--- | :--- |
| S001 | Akshay | 20 |
| S002 | Abhishek | 21 |
| S003 | Shashank | 20 |
| S004 | Rahul | 20 |

* This relation satisfies the tuple uniqueness constraint since here all the tuples are unique.

## Page 4

# 3. Key Constraint-

Key constraint specifies that in any relation-
$\text{➢}$ All the values of primary key must be unique.
$\text{➢}$ The value of primary key must not be null.

## Student Table 1
| TU ID | Name | Age |
| :--- | :--- | :--- |
| S001 | Akshay | 20 |
| S001 | Akshay | 20 |
| S003 | Shashank | 20 |
| S004 | Rahul | 20 |

$\text{➢}$ This relation does not satisfy the tuple uniqueness constraint since here all the tuples are not unique.

## Student Table 2
**P.K.**
| STU ID | Name | Age |
| :--- | :--- | :--- |
| S001 | Akshay | 20 |
| S001 | Abhishek | 21 |
| S003 | Shashank | 20 |
| S004 | Rahul | 20 |

## Page 5

# 4 NOT NULL:

* NOT NULL constraint makes sure that a column does not hold NULL value
* When we do not provide value for a particular column while inserting a record into a table, it takes NULL value by default.
* By specifying NULL constraint, we make sure that a particular column cannot have NULL values

# 5. UNIQUE:

* UNIQUE constraint enforces a column or set of columns to have unique values.
* If a column has a unique constraint, it means that particular column cannot have duplicate values in a table

# 6. DEFAULT

The DEFAULT constraint provides a default value to a column when inserting a record into a table there is no value provided while inserting record into table

## Page 6

# 7. CHECK:

* The CHECK constraint is used to limit the value range that can be placed in a column.
* If you define a CHECK constraint on a column it will allow only certain values for this column.

***

# Integrity constraints

* It provide a way of ensuring the changes made by the authorized user do not result into the loss of data.
* Domain constraint
* Key constraint
* Entity Integrity constraint
* Referential Integrity constrain

## Page 7

# Student

**1. Entity Integrity Constraint-**

* It specifies that **no attribute of primary key must contain a null value** in any relation.
* This is because the presence of **null value** in the primary key violates **the uniqueness property**.

| TU_ID | Name | Age |
| :--- | :--- | :--- |
| S001 | Akshay | 20 |
| S002 | Abhishek | 21 |
| S003 | Shashank | 20 |
| | Rahul | 2 |

This relation does not satisfy **the entity integrity constraint** as here the primary key contains a **NULL value**

## Page 8

# 2. Referential Integrity Constraint

* This constraint is enforced when a foreign key references the primary key of a relation.
* It specifies that all the values taken by the foreign key must either be available in the relation of the primary key or be null.

---

**Student (Referencing)**

| STU_ID | Name | Dept_no |
| :--- | :--- | :--- |
| S001 | Akshay | D10 |
| S002 | Abhishek | D10 |
| S003 | Shashank | D11 |
| S004 | Rahul | <span style="color:green">D14</span> |

---

**Department (Referenced Relation)**

| Dept no | Dept_name |
| :--- | :--- |
| D10 | ASET |
| D11 | ALS |
| D12 | ASFL |
| D13 | ASHS |

---

**Diagram Text:**
* Student ( Stu_ID , Name , **Dept_no** ) $\rightarrow$ ( Referencing Relation )
* Department ( **Dept_no** , Dept_name ) $\rightarrow$ ( Referenced Relation )
* **Foreign Key** (pointing to Dept_no in Student table)

## Page 9

# Referential Integrity Constraint Violation-

There are following three possible causes of violation of referential integrity constraint-
**Cause-01:** Insertion in a referencing relation.
**Cause-02:** Deletion from a referenced relation.
**Cause-03:** Updation in a referenced relation.

---

# Cause-01: Insertion in a Referencing Relation

$\text{➢}$ It is allowed to insert only those values in the referencing attribute which are already present in the value of the referenced attribute.

Inserting a value in the referencing attribute which is not present in the value of the referenced attribute violates the referential integrity constraint.

## Page 10

# Branch
| Branch_Code | Branch_Name |
| :--- | :--- |
| CS | Computer Science |
| EE | Electronics Engineering |
| IT | Information Technology |
| CE | Civil Engineering |

---

# Student
| Roll_no | Name | Age | Branch_Code |
| :--- | :--- | :--- | :--- |
| 1 | Rahul | 22 | CS |
| 2 | Anjali | 21 | CS |
| 3 | Teena | 20 | IT |
| 4 | Rahul | 20 | ME |

---

### Diagram Text
* **Student** (Roll_no, Name, Age, Branch_Code) (Referencing Relation)
* **Branch** (Branch_Code, Branch_Name) (Referenced Relation)
* **Foreign Key** (Arrow pointing from Student to Branch)

### Notes
* In relation “Student”, we can not insert any student having branch code **ME (Mechanical Engineering)**.
* This is because branch code **ME** is not present in the relation “Branch”.

## Page 11

# Cause-02: Deletion from a Referenced Relation-

* It is not allowed to delete a row from the referenced relation if the referencing attribute uses the value of the referenced attribute of that row.
* Such a deletion violates the referential integrity constraint.

### student(referencing relation)

| Roll_no | Name | Age | Branch_Code |
| :--- | :--- | :--- | :--- |
| 1 | Rahul | 22 | CS |
| 2 | Anjali | 21 | CS |
| 3 | Teena | 20 | IT |

### branch(referenced Relation)

| Branch_Code | Branch_Name |
| :--- | :--- |
| CS | Computer Science |
| EE | Electronics Engineering |
| IT | Information Technology |
| CE | Civil Engineering |

## Page 12

# Handling violation

* We can not delete a tuple from the relation "Branch" having branch code 'CS'.
* This is because the referencing attribute "Branch_Code" of the referencing relation "Student" references the value 'CS'.
* However, we can safely delete a tuple from the relation "Branch" having branch code 'CE'.
* This is because the referencing attribute "Branch_Code" of the referencing relation "Student" does not uses this value

1. On Delete Cascade.
2. Aborting or deleting the request for a deletion from the referenced relation if the value is used by the referencing relation.
3. The value being deleted from the referenced relation to NULL or some other value in the referencing relation if the referencing attribute uses that value.

## Page 13

# STUDENT
| Sid | Sname |
| :--- | :--- |
| S101 | A |
| S102 | B |
| S103 | C |

**Referenced Relation**

**Insert** – easily insert new tuple

**Delete-**
1. On delete cascade
(S101 ,A) simultaneously (b101,x,s101)
2. On delete set null –
S101 ,A) simultaneously (b101,x, NULL)
3. ON DELETE SET DEFAULT
S101 ,A) simultaneously (b101,x, 0)

---

# Book
| Bid | Sname | Sid |
| :--- | :--- | :--- |
| b101 | X | S101 |
| b102 | Y | S102 |
| b103 | Z | S103 |
| b104 | W | - |

**Referencing Relationship**

**Insert** no easily not possible (referential intregity constraints must be maintained

**Delete-** easily delete

## Page 14

# Cause-03: Updation in a student(referencing relation)

## Referenced Relation-

* It is not allowed to update a row of the referenced relation if the referencing attribute uses the value of the referenced attribute of that row.
* Such an updation violates the referential integrity constraint

| Roll_no | Name | Age | Branch_Code |
| :--- | :--- | :--- | :--- |
| 1 | Rahul | 22 | CS |
| 2 | Anjali | 21 | CS |
| 3 | Teena | 20 | IT |

**branch(referenced Relation)**

| Branch_Code | Branch_Name |
| :--- | :--- |
| CS | Computer Science |
| EE | Electronics Engineering |
| IT | Information Technology |
| CE | Civil Engineering |

## Page 15

# Handling violation

* We can not update a tuple in the relation "Branch" having branch code 'CS' to the branch code 'CSE'.
* This is because referencing attribute "Branch_Code" of the referencing relation "Student" references the value 'CS'.

1. On Update Cascade
2. aborting or deleting the request for an updation of the referenced relation if the value is used by the referencing relation.

## Page 16

# STUDENT
| Sid | Sname |
| :--- | :--- |
| S101 | A |
| S102 | B |
| S103 | C |

**Referenced Relation**

**UPDATE**
S-101 updated in place of S101

Then this update done simultaneously on book table also

---

# Book
| Bid | Sname | Sid |
| :--- | :--- | :--- |
| b101 | X | S101 |
| b102 | Y | S102 |
| b103 | Z | S013 |
| b104 | W | - |

**Referencing Relationship**

**Update**
Not possible due to referential integrity constraints

## Page 17

# AKTU PYQS

| Question No. | Question | Year |
| :--- | :--- | :--- |
| Q1 | What are the different integrity constraints. | AKTU 2021-22<br>AKTU 2022-23<br>AKTU 2020-21 |
| Q.3 | What is entity integrity constraints. | AKTU 2017-18 |
| Q.2 | Define constraints with its type. | AKTU 2018-19 |

## Page 18

# Database Management System

**UNIT 2**
**Relational data model and language**
**Lecture-2**

**Today's Target**
* Relational Algebra
* AKTU PYQs

By PRAGYA RAJVANSHI
B.Tech, M.Tech( C.S.E.)

## Page 19

| A (PRIMARY KEY) | C (FOREIGN KEY) |
| :--- | :--- |
| 2 | 4 |
| 3 | 4 |
| 4 | 3 |
| 5 | 2 |
| 7 | 2 |
| 9 | 5 |
| 6 | 4 |

(CAKTU)

ON delete cascade (2,4) how many tuple further deleted

(5,2) (7,2) (9,5)

## Page 20

# Relational Algebra

* Relational Algebra is a procedural query language.
* Relational algebra mainly provides a theoretical foundation for relational databases and SQL.
* The main purpose of using Relational Algebra is to define operators that transform one or more input relations into an output relation.

## Fundamental Operators

These are the basic/fundamental operators used in Relational Algebra.

* Selection($\sigma$) (Unary operator)
* Projection($\pi$) (Unary operator)
* Union(U)
* Set Difference(-)
* Set Intersection($\cap$)
* Rename($\rho$)
* Cartesian Product(X)

## Page 21

# 1.Selection($\sigma$)

* The SELECT operation is used to select a subset of the tuples from a relation that satisfy a selection condition.
* The SELECT operation can also be visualized as a horizontal partition of the relation into two sets of tuples
    1. Those tuples that satisfy the condition and are selected.
    2. Those tuples that do not satisfy the condition and are discarded.

---

### SYNTAX
$\sigma_c(R)$

* The symbol $\sigma$ (sigma) is used to denote the SELECT operator.
* $c$ is the selection condition which is a Boolean expression (condition), we can have a single condition like $\text{Roll} = 3$ or a combination of conditions like $X > 2 \text{ AND } Y < 1$
* $R$ is a relational algebra expression, whose result is a relation.

## Page 22

Based on the image provided, here is the extracted text in markdown format:

**Student**

| Roll | Name | Marks |
| :--- | :--- | :--- |
| 1 | A | 60 $\checkmark$ |
| 2 | B | 70 $\checkmark$ |
| 3 | C | 23 |
| 4 | D | 60 $\checkmark$ |
| 5 | E | 25 |

$\text{Marks} > 60$

$\sigma_{\text{Marks} > 60}(\text{Student})$

$\sigma_{\text{Roll}=3}(\text{Student})$

---

**O/P** (Output tables)

**Table 1:**
| Roll | Name | Marks |
| :--- | :--- | :--- |
| 1 | A | 60 |
| 4 | D | 60 |
| 2 | B | 70 |

**Table 2:**
| Roll | Name | Marks |
| :--- | :--- | :--- |
| 3 | C | 23 |
| 5 | E | 25 |

**Table 3:**
| Roll | Name | Marks |
| :--- | :--- | :--- |
| 3 | C | 23 |

## Page 23

# Student Table

| Roll | Name | Department | Fees | Team |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Bikash | CSE | 22000 | A |
| 2 | Josh | CSE | 34000 | A |
| 3 | Kevin | ECE | 36000 | C |
| 4 | Ben | civil | 56000 | |
| 5 | Rani | ECE | 500 | E |

---

**1. Select all the students of Team A :**
$\sigma_{Team = 'A'} (Student)$

| Roll | Name | Department | Fees | Team |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Bikash | CSE | 22000 | A |
| 2 | Josh | CSE | 34000 | A |

**2. Select all the students of department ECE whose fees are greater than and equal to 10000 and belong to a Team other than A.**

## Page 24

The selection operation is commutative that is,

$\sigma_{c1}(\sigma_{c2}(R)) = \sigma_{c2}(\sigma_{c1}(R))$

$\sigma \text{ Department} = \text{'ECE' and Fees } >= 10000(\sigma \text{Team} != \text{'A' (Student)})$

$\sigma \text{ Team} != \text{'A'}(\text{Department} = \text{'ECE' and Fees } >= 10000 \text{ (Student)})$

| Roll | Name | Department | Fees | Team |
| :--- | :--- | :--- | :--- | :--- |
| 3 | Kevin | ECE | 36000 | C |

**Note:**
It is also called unary operator, which means it is applied to a single relation only

## Page 25

# 2.Projection($\pi$)

* PROJECT operation, selects certain columns from the table and discards the other columns.
* The result of the PROJECT operation can hence be visualized as a vertical partition of the relation into two relations:
    1. One has the needed columns (attributes) and contains the result of the operation.
    2. the other contains the discarded columns

---

**Syntax:**
$\pi_A(R)$

* 'A' is the attribute list, it is the desired set of attributes from the attributes of relation(R),
* symbol '$\pi$(pi)' is used to denote the Project operator,
* R is generally a relational algebra expression, which results in a relation.

## Page 26

(Duplicate values not allowed)

**Student**
| Roll | Name | Mobile | Gender |
| :--- | :--- | :--- | :--- |
| 1 | A | 23 | M |
| 2 | B | 42 | M |
| 3 | C | 73 | M |
| 4 | D | 63 | F |
| 5 | C | 29 | M |

$\pi_{Roll, Name}(\text{Student}) \rightarrow$
| Roll | Name |
| :--- | :--- |
| 1 | A |
| 2 | B |
| 3 | C |
| 4 | D |
| 5 | E |

$\pi_{Gender}(\text{Student})$
| Gender | (this is Non-P.K.) or we can not with P.K.) |
| :--- | :--- |
| M | |
| F | |

$\pi_{Roll, Gender}$
| Roll | Gender |
| :--- | :--- |
| 1 | M |
| 2 | F |
| 3 | M |
| 4 | F |
| 5 | M |

**Gateway classes** (Watermark text)

## Page 27

# Student

| Roll | Name | Gender |
| :--- | :--- | :--- |
| 1 | A | M |
| 2 | A | M |
| 3 | B | F |
| 4 | C | F |
| 5 | B | M |

$\pi_{\text{Name, Gender}}$

| Name | Gender |
| :--- | :--- |
| A | M |
| B | F |
| B | M |
| C | F |

(Main list tuple) = < Output Relation tuples

## Page 28

# Employees

| Employee ID | Name | Department | Salary |
| :--- | :--- | :--- | :--- |
| 1 | Alice | HR | 60000 |
| 2 | Bob | IT | 70000 |
| 3 | Charlie | IT | 75000 |
| 4 | David | HR | 62000 |
| 5 | Eva | Finance | 80000 |

***

Select the **name and salary** of the all employee

$\pi_{\text{Name, Salary}}(\text{Employees})$

**SQL :** `SELECT Name, Salary FROM Employees;`

| Name | Salary |
| :--- | :--- |
| Alice | 60000 |
| Bob | 70000 |
| Charlie | 75000 |
| David | 62000 |
| Eva | 80000 |

## Page 29

# Left Panel

**Select all the data of the IT department employee**

$\sigma_{\text{Department='IT'}}$ (Employees)

**SQL: SQL Query : SELECT * FROM Employees WHERE Department = 'IT';**

| Employee ID | Name | Department | Salary |
| :--- | :--- | :--- | :--- |
| 2 | Bob | IT | 70000 |
| 3 | Charlie | IT | 75000 |

---

# Right Panel

**Both projection and selection are used**

$\pi_{\text{Name}} (\sigma_{\text{Department='IT'}} (\text{Employees}))$

| EmployeeID | Name | Department | Salary |
| :--- | :--- | :--- | :--- |
| 2 | Bob | IT | 70000 |
| 3 | Charlie | IT | 75000 |

| Name |
| :--- |
| Bob |
| Charlie |

**Final Ans**

## Page 30

# Student

| Roll | Name | Marks |
| :--- | :--- | :--- |
| 1 | A | 60 |
| 2 | A | 60 |
| 3 | B | 70 |
| 4 | C | 20 |
| 5 | D | 30 |

$\pi_{Name}(\sigma_{Marks \ge 60}(Student))$

| Roll | Name | Marks |
| :--- | :--- | :--- |
| 1 | A | 60 |
| 2 | A | 60 |
| 3 | B | 70 |

| Name |
| :--- |
| A |
| B |

$\pi_{Roll, Name}(\sigma_{Marks \ge 60}(Student))$

| Roll | Name |
| :--- | :--- |
| 1 | A |
| 2 | A |
| 3 | B |

## Page 31

# Employee

## Table 1: Employee
| Employee ID | Name | Department | Salary |
| :--- | :--- | :--- | :--- |
| 1 | Alice | HR | 60000 |
| 2 | Bob | IT | 70000 |
| 3 | Charlie | IT | 75000 |
| 4 | David | HR | 62000 |
| 5 | Eva | Finance | 75000 |
| 6 | Charl | IT | 75000 |

---

## Query: $\pi_{\text{Department, Salary}}$ (Employees)

## Result Table
| Department | Salary |
| :--- | :--- |
| HR | 60000 |
| IT | 70000 |
| IT | 75000 |
| HR | 62000 |
| Finance | 75000 |

## Page 32

# Employee
$\pi_{\text{Salary}} (\text{Employees})$

| Salary |
| :--- |
| 60000 |
| 70000 |
| 75000 |
| 62000 |

* If the attribute list includes only nonkey attributes of R, duplicate tuples are likely to occur.

***

* The PROJECT operation removes any duplicate tuples, so the result of the PROJECT operation is a set of tuples
* The number of tuples in a relation resulting from a PROJECT operation is always less than or equal to the number of tuples in R.

## Page 33

# Employee

| Employee ID | Name | Department | Salary |
| :--- | :--- | :--- | :--- |
| 1 | Alice | HR | 60000 |
| 2 | Bob | IT | 70000 |
| 3 | Charlie | IT | 75000 |
| 4 | David | HR | 62000 |
| 5 | Eva | Finance | 75000 |
| 6 | Charl | IT | 75000 |

---

$\pi_{\text{Department}} (\pi_{\text{Department, Salary}} (\text{Employees}))$

| Department | Salary |
| :--- | :--- |
| HR | 60000 |
| IT | 70000 |
| IT | 75000 |
| HR | 62000 |
| Finance | 75000 |

| Department |
| :--- |
| HR |
| IT |
| Finance |

## Page 34

# Employee

| Employee ID | Name | Department | Salary |
| :--- | :--- | :--- | :--- |
| 1 | Alice | HR | 60000 |
| 2 | Bob | IT | 70000 |
| 3 | Charlie | IT | 75000 |
| 4 | David | HR | 62000 |
| 5 | Eva | Finance | 75000 |
| 6 | Charl | IT | 75000 |

$\pi_{\text{Department, salary}} (\pi_{\text{Department}} (\text{Employees}))$

| Department |
| :--- |
| HR |
| IT |
| Finance |

Not able to get the answer that shows, projection operator is not commutative

## Page 35

| Category | Selection | Projection |
| :--- | :--- | :--- |
| **Other Names** | The selection operation is also known as horizontal partitioning. | The Project operation is also known as vertical partitioning. |
| **Use** | It is used to choose the subset of tuples from the relation that satisfies the given condition mentioned in the syntax of selection. | It is used to select certain required attributes, while discarding other attributes. |
| **Partitioning** | It partitions the table horizontally. | It partitions the table vertically. |

## Page 36

| Category | Selection | Projection |
| :--- | :--- | :--- |
| **Operator Symbol** | Select operator is denoted by Sigma symbol. | Project operator is denoted by Pi symbol. |
| **Commutative** | Selection is commutative. | Projection is not commutative. |
| **Column Selection** | Select is used to select all columns of a specific tuple. | Project is used to select specific columns. |
| **Which used first** | The selection operation is performed before projection (if they are to be used together). | The projection operation is performed after selection (if they are to be used together). |

## Page 37

# Student

| Name | Roll | Mobile | Address | Marks |
| :--- | :--- | :--- | :--- | :--- |
| A | 1 | 9263 | A1 | 70 |
| A | 2 | 9263 | A1 | 60 |
| B | 3 | 4279 | A2 | 70 |
| C | 4 | 4478 | A3 | 80 |
| D | 5 | 5867 | A4 | 90 |

| marks | Name |
| :--- | :--- |
| 70 | A |
| 60 | A |
| 70 | B |

| Name | Marks |
| :--- | :--- |
| A | 70 |
| A | 60 |
| B | 70 |

| | |
| :--- | :--- |
| 70 | |
| 60 | |

---

1. Select those address, Whose Name is A And mark <= 60
   $\Pi_{Address}(\sigma_{Name='A' \text{ and marks } <= 60}(Student))$

2. Select Marks of all Student Whose marks <= 70
   $\Pi_{Marks}(\sigma_{marks <= 70}(Student))$

3. Select Name & Marks of all Student, Whose marks <= 70
   $\Pi_{Name, Marks}(\sigma_{marks <= 70}(Student))$
   $\Pi_{Marks, Name}(\sigma_{marks <= 70}(Student))$

## Page 38

# Database Management System

**UNIT 2**
**Relational data model and language**
Lecture-3

**Today's Target**
* Relational Algebra
* AKTU PYQs

By PRAGYA RAJVANSHI
B.Tech, M.Tech( C.S.E.)

## Page 39

# Union compatible

Two relations $\text{R}(\text{A1, Az, ..., An})$ and $\text{S}(\text{B 1, Bz, ..., Bn})$ are said to be union compatible if they have

1. the same degree n
2. If $\text{dom}(\text{A}_i) = \text{dom}(\text{B}_i) \text{ 1<=i<=n}$

This means that the two relations have the same number of attributes, and each corresponding pair of attributes has the same domain.

***

We can define the three operations **UNION**, **INTERSECTION**, and **SET DIFFERENCE** on two union-compatible relations R and S follows-

**1. union:**

* The result of this operation, denoted by $\text{R} \cup \text{S}$,
* It is a relation that includes all tuples that are either in R or in S or in both R and S.
* Duplicate tuples are eliminated

## Page 40

```markdown
R
| A1 | A2 | ... | An |
|---|---|---|---|
|   |   |   |   |
10

S
| B1 | B2 | ... | Bn |
|---|---|---|---|
|   |   |   |   |

Gateway classes
```

## Page 41

| Depositor | |
| :--- | :--- |
| **CUSTOMER_NAME** | **ACCOUNT_NO** |
| Johnson | A-101 |
| Smith | A-121 |
| Mayes | A-321 |
| Turner | A-176 |
| Johnson | A-273 |
| Jones | A-472 |
| Lindsay | A-284 |

| BORROW | |
| :--- | :--- |
| **CUSTOMER_NAME** | **LOAN_NO** |
| Jones | L-17 |
| Smith | L-23 |
| Hayes | L-15 |
| Jackson | L-14 |
| Curry | L-93 |
| Smith | L-11 |
| Williams | L-17 |

## Page 42

$\pi_{\text{CUSTOMER\_NAME}}(\text{Depositor}) \cup \pi_{\text{CUSTOMER\_NAME}}(\text{Borrower}) =$
$\pi_{\text{CUSTOMER\_NAME}}(\text{Borrower}) \cup \pi_{\text{CUSTOMER\_NAME}}(\text{Depositor})$

(2) $\pi_{\text{CUSTOMER\_NAME}}(\text{Borrower}) \cap \pi_{\text{CUSTOMER\_NAME}}(\text{Depositor}) - \text{Intersection}$

(3) $\pi_{\text{CUSTOMER\_NAME}}(\text{Borrower}) \setminus \pi_{\text{CUSTOMER\_NAME}}(\text{Depositor}) - \text{Set Difference / Minus}$

(4) $\pi_{\text{CUSTOMER\_NAME}}(\text{Depositor}) - \pi_{\text{CUSTOMER\_NAME}}(\text{Borrower})$

## Page 43

# Gateway classes

| CUSTOMER NAME |
| :--- |
| Johnson |
| Mayes |
| Turner |
| Lindsay |

## Page 44

# CUSTOMER_NAME
* Johnson
* Smith
* Hayes
* Turner
* Jones
* Lindsay
* Jackson
* Curry
* Williams
* Mayes
* Johnson

(1) (Union)

# CUSTOMER_NAME
* Smith
* Jones

(2) (Intersection)

# CUSTOMER_NAME
* Jackson
* Hayes
* Williams
* Curry

(3)

## Page 45

# Left Column

**2.Intersection:**

The result of this operation, denoted by $R \cap S$, is a relation that includes all tuples that are in both R and S.

**3. set difference (or MINUS):**

The result of this operation, denoted by $R - S$, is a relation that includes all tuples that are in R but not in S.

---

# Right Column

**Q.1 To retrieve the social security numbers...**
of all employees who either work in department 5 or directly supervise an employee who works in department 5.

$\text{DEPS\_EMP} \leftarrow \sigma_{\text{DNO}=5}(\text{EMPLOYEE})$
$\text{Result1} \leftarrow \pi_{\text{SSN}}(\text{DEPS\_EMP})$
$\text{Result2(ssn)} \leftarrow \pi_{\text{supSSN}}(\text{DEPS\_EMP})$
$\text{Result} \leftarrow \text{Result1} \cup \text{Result2}$

## Page 46

| Result 1 | Result 2 | SS N |
| :--- | :--- | :--- |
| SSN | SSN | 1234 567 87 |
| 123456789 | 333445555 | 33344 55 5 |
| 333445555 | 888665555 | 666 8 84444 |
| 666 88 4444 | | 4+ 36 1345 3 |
| 453453437 | | 88866 555 |

Gateway Classes

## Page 47

| EMPLOYEE | FNAME | MINIT | LNAME | SSN | BDATE | ADDRESS | SEX | SALARY | SUPERSSN | DNO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | John | B | Smith | 123456789 | 1965-01-09 | 731 Fondren, Houston, TX | M | 30000 | 333445555 | 5 |
| | Franklin | T | Wong | 333445555 | 1955-12-08 | 638 Voss, Houston, TX | M | 40000 | 888665555 | 5 |
| | Alicia | J | Zelaya | 999887777 | 1968-01-19 | 3321 Castle, Spring, TX | F | 25000 | 987654321 | 4 |
| | Jennifer | S | Wallace | 987654321 | 1941-06-20 | 291 Berry, Bellaire, TX | F | 43000 | 888665555 | 4 |
| | Ramesh | K | Narayan | 666884444 | 1962-09-15 | 975 Fire Oak, Humble, TX | M | 38000 | 333445555 | 5 |
| | Joyce | A | English | 453453453 | 1972-07-31 | 5631 Rice, Houston, TX | F | 25000 | 333445555 | 5 |
| | Ahmad | V | Jabbar | 987987987 | 1969-03-29 | 980 Dallas, Houston, TX | M | 25000 | 987654321 | 4 |
| | James | E | Borg | 888665555 | 1937-11-10 | 450 Stone, Houston, TX | M | 55000 | null | 1 |

## Page 48

# Cartesian Product

* **CARTESIAN PRODUCT** operation-also known as **CROSS PRODUCT** or **CROSS JOIN**-which is denoted by x.
* This is also a **binary set operation**, but the **relations** on which it is applied do not have to be **union compatible**.
* This operation is used to **combine** tuples from **two relations** in a combinatorial fashion.

---

* The operation applied by itself is generally meaningless.
* It is useful when followed by a **selection** that matches values of attributes coming from the **component relations**.

## Page 49

# EMPLOYEE

| EMP_ID | EMP_NAME | EMP_DEPT |
| :--- | :--- | :--- |
| 1 | Smith | A |
| 2 | Harry | C |
| 3 | John | B |

# DEPARTMENT

| DEPT_NO | DEPT_NAME |
| :--- | :--- |
| A | Marketing |
| B | Sales |
| C | Legal |

**EMPLOYEE X DEPARTMENT**

## Page 50

| EMP_ID | EMP_NAME | EMP_DEPT | DEPT_NO | DEPT_NAME |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Smith | A | A | Marketing |
| 1 | Smith | A | B | Sales |
| 1 | Smith | A | C | Legal |
| 2 | Harry | C | A | Marketing |
| 2 | Harry | C | B | Sales |
| 2 | Harry | C | C | Legal |
| 3 | John | B | A | Marketing |
| 3 | John | B | B | Sales |
| 3 | John | B | C | Legal |

## Page 51

| EMPLOYEE | FNAME | MINIT | LNAME | SSN | BDATE | ADDRESS | SEX | SALARY | SUPERSSN | DNO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | John | B | Smith | 123456789 | 1965-01-09 | 731 Fondren, Houston, TX | M | 30000 | 333445555 | 5 |
| | Franklin | T | Wong | 333445555 | 1955-12-08 | 638 Voss, Houston, TX | M | 40000 | 888665555 | 5 |
| | Alicia | J | Zelaya | 999887777 | 1968-01-19 | 3321 Castle, Spring, TX | F | 25000 | 987654321 | 4 |
| | Jennifer | S | Wallace | 987654321 | 1941-06-20 | 291 Berry, Bellaire, TX | F | 43000 | 888665555 | 4 |
| | Ramesh | K | Narayan | 666884444 | 1962-09-15 | 975 Fire Oak, Humble, TX | M | 38000 | 333445555 | 5 |
| | Joyce | A | English | 453453453 | 1972-07-31 | 5631 Rice, Houston, TX | F | 25000 | 333445555 | 5 |
| | Ahmad | V | Jabbar | 987987987 | 1969-03-29 | 980 Dallas, Houston, TX | M | 25000 | 987654321 | 4 |
| | James | E | Borg | 888665555 | 1937-11-10 | 450 Stone, Houston, TX | M | 55000 | null | 1 |

## Page 52

| DEPENDENT | ESSN | DEPENDENT_NAME | SEX | BDATE | RELATIONSHIP |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | 333445555 | Alice | F | 1986-04-05 | DAUGHTER |
| | 333445555 | Theodore | M | 1983-10-25 | SON |
| | 333445555 | Joy | F | 1958-05-03 | SPOUSE |
| | 987654321 | Abner | M | 1942-02-28 | SPOUSE |
| | 123456789 | Michael | M | 1988-01-04 | SON |
| | 123456789 | Alice | F | 1988-12-30 | DAUGHTER |
| | 123456789 | Elizabeth | F | 1967-05-05 | SPOUSE |

## Page 53

# Q.2 we want to retrieve a list of names of each female employee's dependent

$\text{FemaleEmp} \leftarrow \sigma_{\text{Sex}='F'}(\text{EMPLOYEE})$

$\text{EMPNAME} \leftarrow \pi_{\text{FName, LName, SSN}}(\text{Female\_Emp})$

$\text{EMPDEPEND} \leftarrow \text{EMPNAME} \times \text{DEPENDENT}$

$\text{ACTUAL\_DEPENDENT} \leftarrow \pi_{\text{SSN=ESSN}}(\text{EMPDEPENDENT})$

$\text{Result} \leftarrow \pi_{\text{FName, LName, DependentName}}(\text{ACTUAL\_DEPENDENT})$

## Page 54

| EMP_DEPENDENTS | FNAME | LNAME | SSN | ESSN | DEPENDENT_NAME | SEX | BDATE | ... | ... |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | Alicia | Zelaya | 9998877777 | 3334455555 | Alice | F | 1986-04-05 | . | . |
| | Alicia | Zelaya | 9998877777 | 3334455555 | Theodore | M | 1983-10-25 | . | . |
| | Alicia | Zelaya | 9998877777 | 3334455555 | Joy | F | 1958-05-03 | . | . |
| | Alicia | Zelaya | 9998877777 | 987654321 | Abner | M | 1942-02-28 | . | . |
| | Alicia | Zelaya | 9998877777 | 123456789 | Michael | M | 1988-01-04 | . | . |
| | Alicia | Zelaya | 9998877777 | 123456789 | Alice | F | 1988-12-30 | . | . |
| | Alicia | Zelaya | 9998877777 | 123456789 | Elizabeth | F | 1967-05-05 | . | . |
| | Jennifer | Wallace | 987654321 | 3334455555 | Alice | F | 1986-04-05 | . | . |
| | Jennifer | Wallace | 987654321 | 3334455555 | Theodore | M | 1983-10-25 | . | . |
| | Jennifer | Wallace | 987654321 | 3334455555 | Joy | F | 1958-05-03 | . | . |
| | Jennifer | Wallace | 987654321 | 987654321 | Abner | M | 1942-02-28 | . | . |
| | Jennifer | Wallace | 987654321 | 123456789 | Michael | M | 1988-01-04 | . | . |
| | Jennifer | Wallace | 987654321 | 123456789 | Alice | F | 1988-12-30 | . | . |
| | Jennifer | Wallace | 987654321 | 123456789 | Elizabeth | F | 1967-05-05 | . | . |
| | Joyce | English | 453453453 | 3334455555 | Alice | F | 1986-04-05 | . | . |
| | Joyce | English | 453453453 | 3334455555 | Theodore | M | 1983-10-25 | . | . |
| | Joyce | English | 453453453 | 3334455555 | Joy | F | 1958-05-03 | . | . |
| | Joyce | English | 453453453 | 987654321 | Abner | M | 1942-02-28 | . | . |
| | Joyce | English | 453453453 | 123456789 | Michael | M | 1988-01-04 | . | . |
| | Joyce | English | 453453453 | 123456789 | Alice | F | 1988-12-30 | . | . |
| | Joyce | English | 453453453 | 123456789 | Elizabeth | F | 1967-05-05 | . | . |

## Page 55

### Table 1
| ACTUAL_DEPENDENTS | FNAME | LNAME | SSN | ESSN | DEPENDENT_NAME | SEX | BDATE | ... |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| | Jennifer | Wallace | 987654321 | 987654321 | Abner | M | 1942-02-28 | ... |

### Table 2
| RESULT | FNAME | LNAME | DEPENDENT_NAME |
| :--- | :--- | :--- | :--- |
| | Jennifer | Wallace | Abner |

## Page 56

# Branch
| Branch_name | Branch_city | Assests |
| :--- | :--- | :--- |

# Account
| Account_no | Branch_name | balance |
| :--- | :--- | :--- |

# Loan
| Loan_no | Branch_name | amount |
| :--- | :--- | :--- |

# Customer
| Customer_name | Cust_street | Cust_city |
| :--- | :--- | :--- |

## Page 57

| Depositor | |
| :--- | :--- |
| Customer name | Account no |

| Borrower | |
| :--- | :--- |
| Customer name | Loan no |

## Page 58

# Left Column

**Q.3** Find the details of account having balance >= 1000
$\sigma_{balance \ge 1000} (\text{Account})$
NOTE: $\wedge$ - and, $\vee$ - OR

**Q.4** Find the details of the customers who lives in Delhi.
$\sigma_{cust\_city = 'Delhi'} (\text{Customer})$

**Q.5** Find the details of those loan having amount <= 500 and from north Delhi
$\sigma_{amount \le 500 \wedge Branch\_name = 'North Delhi'} (\text{Loan})$

---

# Right Column

**Q.6** Find those branch details which are in Delhi and having assets more than 10,00,00.
$\sigma_{Branch\_city = 'Delhi' \wedge Assets > 10,00,00} (\text{Branch})$

**Q.7** Find those branch details which are in Delhi or having assets more than 10,00,00.
$\sigma_{Branch\_city = 'Delhi' \vee Assets > 10,00,00} (\text{Branch})$

## Page 59

**Q.8 Find those account number where balance is less than 1000.**

$\Pi_{account\_no}(\sigma_{balance < 1000}(Account))$

---

**Q.9 Find the loan number which are from CP Branch plus amount > 1000.**

$\Pi_{loan\_no}(\sigma_{Branch\_name = 'CP' \wedge amount > 1000}(Loan))$

---

**Q.10 Find all branch name of bank.**

$\Pi_{Branch\_name}(Branch)$

---

**Q.11 Find the name of all customers who have loan**

$\Pi_{customer\_name}(Borrower)$

---

**Q.12 Find all the name of the Customer, who are depositor or Borrower Loan**

$\Pi_{customer\_name}(Borrower) \cup \Pi_{customer\_name}(Depositor)$

## Page 60

Q Find the customer name Who are Depositer but not having any Loan
$\pi_{customer\_name}(Depositer) - \pi_{customer\_name}(Borrower)$

Q Find the customer name Who borrow Loan but not depositor
$\pi_{(Customername)}(Borrower) - \pi_{Customer\_name}(Depositer)$

---

Q Find the Branch name Who have account not having Loan
$\pi_{Branch\_name}(Account) - \pi_{Branchname}(Loan)$

## Page 61

# Database Management System

**UNIT 2**
**Relational data model and language**
**Lecture-4**

**Today's Target**
* Relational Algebra
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 62

# Gateway classes

**Derived Operator**
* Inner
    1. Join $\leftarrow$ Outer
    2. Division

## Page 63

# CARTESIAN PRODUCT

**Join**

* Join is a combination of a Cartesian product followed by a selection process.
* A Join operation pairs two tuples from different relations, if and only if a given join condition is satisfied.

**R1**

| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

**R2**

| D | E | F |
|---|---|---|
| 6 | 7 | 2 |
| 4 | 5 | 8 |
| 7 | 6 | 2 |

## Page 64

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 6 | 7 | 2 |
| 1 | 2 | 3 | 4 | 5 | 8 |
| 1 | 2 | 3 | 7 | 6 | 2 |
| 4 | 5 | 6 | 6 | 7 | 2 |
| 4 | 5 | 6 | 4 | 5 | 8 |
| 4 | 5 | 6 | 7 | 6 | 2 |
| 7 | 8 | 9 | 6 | 7 | 2 |
| 7 | 8 | 9 | 4 | 5 | 8 |
| 7 | 8 | 9 | 7 | 6 | 2 |

Cartesian product $R_1 \times R_2$

## Page 65

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| 4 | 5 | 6 | 4 | 5 | 8 |
| 7 | 8 | 9 | 6 | 7 | 2 |
| 7 | 8 | 9 | 4 | 5 | 8 |
| 7 | 8 | 9 | 7 | 6 | 2 |

$R_1 \bowtie_{C > D} R_2$

Cartesian product + selection (those tuple in which c>d)
$\sigma_{C > D}(R_1 \times R_2)$

## Page 66

# JOIN

**1. Inner join (Matching tuples)**
* theta join
* Equi join
* Natural join
* Semi join
* Anti join

**2. Outer join (Matching and non matching tuples)**
* Left outer join
* Right outer join
* Full outer join

---

**Theta ($\theta$) Join** $\quad$ R1 $\bowtie_\theta$ R2
$(\theta) = \{ <, <=, >, >=, ==, \neq \}$

**R1**
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

**R2**
| D | E | F |
|---|---|---|
| 6 | 7 | 2 |
| 4 | 5 | 8 |
| 7 | 6 | 2 |

## Page 67

# Text Extraction

**Top Left Logo:** GW GATEWAY CLASSES
**Top Right Logo:** GW GATEWAY CLASSES

**Top Center (Handwritten):** (Equality)

**Main Content:**

**Left Table:**
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| 4 | 5 | 6 | 4 | 5 | 8 |
| 7 | 8 | 9 | 6 | 7 | 2 |
| 7 | 8 | 9 | 4 | 5 | 8 |
| 7 | 8 | 9 | 7 | 6 | 2 |

**Bottom Left Text:**
R1 $\bowtie_{C>D}$ R2

---

**Right Section:**

**Header:**
EQUI JOIN R1 $\bowtie_{C=D}$ R2

**Right Table:**
| A | B | C | D | E | F |
|---|---|---|---|---|---|
| 4 | | 6 | 6 | 7 | 2 |

**Text:**
When Theta join uses only equality comparison operator, it is said to be equijoin

## Page 68

# Degree and cardinality

$|R_1|_{d} + |R_2|_{d} = |R_1 + R_2|_{d}$ (theta join)

$|R_1|_{d} + |R_2|_{d} = |R_1 + R_2|_{d}$ (Equi join)

Cardinality (No of tuples in a Relation) $\text{degree} = \text{no of attribute in a Relation}$

$0 \le |R_1 \bowtie_{\theta} R_2|_{c} \le |R_1| \times |R_2|$

Equijoin
$0 \le |R_1 \bowtie R_2|_{c} \le |R_1| \times |R_2|$

| R1 | |
| :--- | :--- |
| **A** | **B** |
| 1 | .. 2 |
| 3 | .. 4 |

| R2 | |
| :--- | :--- |
| **C** | **D** |
| .. 5 | 6 |
| 7 | 8 |

$\begin{array}{|c|c|c|c|} \hline \text{A} & \text{B} & \text{C} & \text{D} \\ \hline 1 & 2 & 5 & 6 \\ \hline 1 & 2 & 7 & 8 \\ \hline 3 & 4 & 5 & 6 \\ \hline 3 & 4 & 7 & 8 \\ \hline \end{array}$

## Page 69

# Degree and cardinality

| Cardno | name | bid | DOI |
| :--- | :--- | :--- | :--- |
| 1 | A | 23 | 6 Jun |
| 2 | abc | 26 | JJ |
| 2 | abc | 27 | 87 |

| Cardno |
| :--- |
| 1 |

---

# QUERIES

1. **book**(bid, title, year_pub)
2. **User**(card_no, name)
3. **Borrow**(bid, card_no, DOI)
4. **Supply**(bid, sname, price, dos)

**Q.1 Find the bid of all books issued to 'abc'**

$\pi_{bid} (\sigma_{name = 'abc'} (User \bowtie_{User.cardno = Borrow.cardno} Borrow))$

## Page 70

# Natural join $\bowtie$

* Natural join does not use any comparison operator.
* It does not concatenate the way a Cartesian product does.
* We can perform a Natural Join only if there is at least one common attribute that exists between two relations.
* In addition, the attributes must have the same name/similar and domain.

### Course
| ID | Course | Dept |
| :--- | :--- | :--- |
| CS01 | Database | CS |
| ME01 | Mechanics | ME |
| EE01 | Electronics | EE |

### HoD
| Dept | Head |
| :--- | :--- |
| CS | Alex |
| ME | Maya |
| EE | Mira |

## Page 71

# Courses $\bowtie$ HoD

| Dept | CID | Course | Head |
| :--- | :--- | :--- | :--- |
| CS | CS01 | Database | Alex |
| ME | ME01 | Mechanics | Maya |
| EE | EE01 | Electronics | Mira |

***

# R1

| A | B | C |
| :--- | :--- | :--- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

***

# Difference Between-
Natural Join

# R2

| C | D | E |
| :--- | :--- | :--- |
| 3 | 6 | 9 |
| 9 | 5 | 4 |
| 8 | 7 | 6 |

***

# $R_1 \bowtie R_2$

| A | B | C | D | E |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 2 | 3 | 6 | 9 |
| 7 | 8 | 9 | 5 | 4 |

***

# $R_1 \bowtie_{R1.C = R2.C} R_2$ {Equijoin}

| A | B | R1.C | R2.C | D | E |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 2 | 3 | 3 | 6 | 9 |
| 7 | 8 | 9 | 9 | 5 | 4 |

## Page 72

# Text Extraction

**Left Panel:**
If two attribute are same

**R1**
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

**R2**
| B | C | D |
|---|---|---|
| 2 | 3 | 9 |
| 6 | 5 | 4 |
| 8 | 9 | 6 |

---

**Right Panel:**
| A | B | C | D |
|---|---|---|---|
| 1 | 2 | 3 | 9 |
| 7 | 8 | 9 | 6 |

Natural join work as intersection/ALL three attribute are same
$R_1 \bowtie R_2 = R_1 \cap R_2$

**R1**
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

**R2**
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 6 | 5 | 4 |
| 8 | 9 | 6 |

## Page 73

# Gateway Classes

| A | B | C |
|---|---|---|
| 1 | 2 | 3 |

---

| R2 | | |
|---|---|---|
| **D** | **E** | **F** |
| 1 | 2 | 3 |
| 6 | 5 | 4 |

---

When natural join work as Cartesian product or when no attribute are same
$R_1 \bowtie R_2 = R_1 \times R_2$

---

**R1**
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |

---

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 1 | 2 | 3 |
| 1 | 2 | 3 | 6 | 5 | 4 |
| 4 | 5 | 6 | 1 | 2 | 4 |
| 4 | 5 | 6 | 6 | 5 | 4 |

## Page 74

# Gateway Classes

## R1
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

## R2
| C | D | E |
|---|---|---|
| 3 | 6 | 9 |
| 9 | 8 | 2 |
| 7 | 6 | 3 |

## Table (Top Right)
| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 6 | 9 |
| 7 | 8 | 9 | 8 | 2 |

**Notation:** $R_1 \bowtie R_2$

**Note:** Green colored $\rightarrow$ Dangling tuples

## Page 75

# Degree and cardinality

$|R_1|_d + |R_2|_d - m = |R_1 \bowtie R_2|_d$
$\text{No of common tuples}$ — degree

$0 \le |R_1 \bowtie R_2| \le |R_1 \times R_1|_c$
(Cardinality)

$R_1 \bowtie R_2$

| R1 | | |
| :--- | :--- | :--- |
| **A** | **B** | **C** |
| 1 | 2 | 3 |

| R2 | | |
| :--- | :--- | :--- |
| **C** | **D** | **E** |
| 6 | 7 | 8 |

---

| R1 | | |
| :--- | :--- | :--- |
| **A** | **B** | **C** |
| 1 | 2 | 3 |
| 1 | 6 | 3 |
| 8 | 9 | 3 |

| R2 | | |
| :--- | :--- | :--- |
| **C** | **D** | **E** |
| 3 | 6 | 9 |
| 3 | 5 | 2 |
| 3 | 8 | 2 |

## Page 76

| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 6 | 9 |
| 1 | 2 | 3 | 5 | 2 |
| 1 | 2 | 3 | 8 | 2 |
| 1 | 6 | 3 | 6 | 9 |
| 1 | 6 | 3 | 5 | 2 |
| 1 | 6 | 3 | 8 | 2 |
| 8 | 9 | 3 | 6 | 9 |
| 8 | 9 | 3 | 5 | 2 |
| 8 | 9 | 3 | 8 | 2 |

**Cartesian product**

## Page 77

# QUERIES

1. `book(bid, title, year_pub)`
2. `User(card_no, name, city)`
3. `Borrow(bid, card_no, DOI)`
4. `Supply(bid, sname, price, dos)`

**Q.1 Find titles of all books supplies by abc.**
$$\Pi_{title} \left( \sigma_{Sname = 'abc'} (book \bowtie Supply) \right)$$

**Q.2 Find bookid of all books issue abc.**
$$\Pi_{bookid} \left( \sigma_{name = 'abc'} (User \bowtie Borrow) \right)$$

**Q.3 Find title of all books issue to abc.**
$$\Pi_{title} \left( \sigma_{name = 'abc'} (book \bowtie Borrow \bowtie User) \right)$$

## Page 78

# QUERIES

1. **book**(bid, title, year_pub)
2. **User**(card_no, name, city)
3. **Borrow**(bid, card_no, DOI)
4. **Supply**(bid, sname, price, dos)

**Q.4 Find the name of all those supplier who have supplied book issue to 'abc'.**

$\Pi_{sname}(\sigma_{name = 'abc'}(Borrow \bowtie Supply \bowtie User))$

## Page 79

# QUERIES

1. book(**bid**, title ,year_pub)
2. User(**card_no**,name,city)
3. Borrow(**bid,card_no**, DOI)
4. Supply(**bid**,sname,price,dos)

**Q. 5** Find the name of all those supplier who have supplies book of same title as issue to abc.

$\Pi_{sname} ( \Pi_{title} ( \sigma_{name='abc'} (book \bowtie borrow \bowtie User) ) \bowtie (\Pi_{title, sname} (Supply \bowtie book)) )$

## Page 80

# QUERIES

1. book(bid, title, year_pub)
2. User(card_no, name, city)
3. Borrow(bid, card_no, DOI)
4. Supply(bid, sname, price, dos)

**Q.6** Find the name of all user who lives in same city as that of abc.

$\pi_{name}(\pi_{city}(\sigma_{name = 'abc'}(User)) \bowtie \pi_{name, city}(\sigma_{name \neq 'abc'}(User)))$

## Page 81

# QUERIES

1. **book(bid, title, year_pub)**
2. **User(card_no, name, city)**
3. **Borrow(bid, card_no, DOI)**
4. **Supply(bid, sname, price, dos)**

**Q. 7** find the name of all those borrowers who have issued book on same date as issued by abc.

$\pi_{name}(\sigma_{DOI = \pi_{DOI}(\sigma_{name='abc'}(User \bowtie Borrow))}(User \bowtie Borrow))$

$\pi_{name, DOI}(\sigma_{name \neq 'abc'}(User \bowtie Borrow))$

## Page 82

# SEMI JOIN $\Join$
$R_1 \Join R_2$

| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |

# ANTI JOIN $\text{⊳}$

| C | D | E |
|---|---|---|
| 3 | 6 | 9 |
| 6 | 7 | 3 |

---

# R1

| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

# R2

| D | E | F |
|---|---|---|
| 3 | 6 | 9 |
| 4 | 5 | 2 |
| 6 | 7 | 3 |

$R_1 \Join R_2$

| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 6 | 9 |
| 4 | 5 | 6 | 7 | 3 |

## Page 83

# Outer Joins

* Theta Join, Equijoin, and Natural Join are called inner joins.
* An inner join includes only those tuples with matching attributes and the rest are discarded in the resulting relation.
* Therefore, we need to use outer joins to include all the tuples from the participating relations in the resulting relation. There are three kinds of outer joins – left outer join, right outer join, and full outer join.

**R1**
| A | B | C |
|---|---|---|
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

**R2**
| C | D | E |
|---|---|---|
| 3 | 6 | 7 |
| 8 | 5 | 4 |
| 6 | 3 | 2 |

## Page 84

# NATURAL JOIN $R_1 \bowtie R_2$

| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 6 | 7 |
| 4 | 5 | 6 | 3 | 2 |

# Left outer join $R_1 \left outerjoin \right. R_2$

| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 6 | 7 |
| 4 | 5 | 6 | 3 | 2 |
| 7 | 8 | 9 | - | - |

# Right outer join $R_1 \right outerjoin R_2$

| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 6 | 7 |
| 4 | 5 | 6 | 3 | 2 |
| - | - | 8 | 5 | 2 |

# Full outer join $\bowtie$

| A | B | C | D | E |
|---|---|---|---|---|
| 1 | 2 | 3 | 6 | 7 |
| 4 | 5 | 6 | 3 | 2 |
| 7 | 8 | 9 | - | - |
| - | - | 8 | 5 | 2 |

## Page 85

# Database Management System

**UNIT 2**
**Relational data model and language**
**Lecture-5**

**Today's Target**
* Relational Algebra Numericals
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 86

# Left Panel

**Give the following queries in the relational algebra using the relational schema :**

**student(id, name)**
**Enrolled (id, code)**
**subject(code, lecturer) (AKTU 2019-20)**

**1. What are the names of students enrolled in cs3020**

$\Pi_{name}(\sigma_{code = 'cs3020'}(Student \bowtie Enrolled))$

---

# Right Panel

**2 Which subjects is Hector taking**

$\Pi_{code}(\sigma_{nam = 'Hector'}(Student \bowtie Enrolled))$

## Page 87

# Gateway Classes

Give the following queries in the relational algebra using the relational schema :

**student(id, name)**
**Enrolled (id, code)**
**subject(code, lecturer)**

**3. Who teaches cs1500 ?**
$\Pi_{lecturer}(\sigma_{code=cs1500}(Subject))$

**4. Who teaches cs1500 or cs3020**
$\Pi_{lecturer}(\sigma_{code=cs1500 \lor code=cs3020}(Subject))$

## Page 88

# Relational Algebra Queries

**Give the following queries in the relational algebra using the relational schema:**

**student**(id, name)
**Enrolled**(id, code)
**subject**(code, lecturer)

---

**5. Who teaches at least two different subjects?**

$\Pi_{S1.lecturer} ( \rho_{S1}(\text{Subject}) \bowtie_{S1.lecturer = S2.lecturer \wedge S1.code \neq S2.code} \rho_{S2}(\text{Subject}) )$

---

**6. What are the names of students in cs1500 or cs307?**

$\Pi_{name} ( \sigma_{\text{Code} = \text{'CS1500'}} (\text{Student} \bowtie \text{Enrolled}) ) \cup \Pi_{name} ( \sigma_{\text{Code} = \text{'CS307'}} (\text{Student} \bowtie \text{Enrolled}) )$

## Page 89

Give the following queries in the relational algebra using the relational schema :

**student(id, name)**
**Enrolled (id, code)**
**subject(code, lecturer)**

7. What are the names of students in both cs 1500 and cs1200

$\Pi_{name}(\sigma_{Code = CS1500}(Student \bowtie Enrolled))$
$\cap$
$\Pi_{name}(\sigma_{code = CS1200}(Student \bowtie Enrolled))$

## Page 90

# Consider the following relations :

**Student** (ssn, name, address, major)
**Course** (code, title)
**Registered** (ssn, code)

Use relational algebra to answer the following :

1. List the codes of courses in which at least one student is registered (registered courses).

$\pi_{code} (Course \bowtie Registered)$
or
$\pi_{code} (Registered)$

2. List the title of registered courses

$\pi_{title} (Course \bowtie Registered)$

## Page 91

Consider the following relations :

Student (**ssn**, name, address, major)
Course (**code**, title)
Registered (**ssn, code**)(AKTU 2015-16/2017-18)

Use relational algebra to answer the following :

3. List the codes of courses for which no student is registered.
$\Pi_{code}(Course) - \Pi_{code}(Course \bowtie Registered)$

4. The titles of courses for which no student is registered
$\Pi_{title}(Course) - \Pi_{title}(Course \bowtie Registered)$

## Page 92

Consider the following relations :

Student (**ssn**, name, address, major)
Course (**code**, title)
Registered (**ssn**, **code**)

Use relational algebra to answer the following

**5. Name of students and the titles of courses they registered to**

$\Pi_{name, (Course \bowtie Registered \bowtie Student) title}$

## Page 93

Consider the following relations :

Student (**ssn**, name, address, major)
Course (**code**, title)
Registered (**ssn**, **code**)

Use relational algebra to answer the following

6. SSNs of students who are registered for both database systems and analysis of algorithms

$\Pi_{SSN}(\sigma_{title = \text{Database System}}(Course \bowtie Registered \bowtie Student))$
$\cap$
$\Pi_{SSN}(\sigma_{title = \text{Analysis of Algorithms}}(Course \bowtie Registered \bowtie Student))$

## Page 94

# Left Panel

**Consider the following relations :**

Student (**ssn**, name, address, major)
Course (**code**, title)
Registered (**ssn**, **code**)

Use relational algebra to answer the following

**7 The name of students who are registered for both database systems and analysis of algorithms.**

---

# Right Panel (Handwritten Notes)

$\Pi_{name} (\sigma_{title = \text{'Database Systems'}} (Student \bowtie Course \bowtie Registered))$

$\cap$

$\Pi_{name} (\sigma_{title = \text{'Analysis of Algos'}} (Student \bowtie Course \bowtie Registered))$

## Page 95

# Division operator

| R1(R) | |
| :--- | :--- |
| **W** | **X** |
| P | A |
| P | B |
| Q | A |
| Q | B |
| P | C |
| Q | D |
| M | A |
| R | B |
| Q | C |

| R2(S) | |
| :--- | :--- |
| X | |
| X | |
| | |
| | |

| W | |
| :--- | :--- |
| P | |
| Q | |

$R_1 \div R_2$  $S \subset R$  $R = \{w_1, x\}$
$R_1 - R_2 = R - S$  $S = \{x\}$

## Page 96

**Consider the following relations :**

Student (**ssn**, name, address, major)
Course (**code**, title)
Registered (**ssn**, code)

Use relational algebra to answer the following
8. List of course in which all students are registered .

$\pi_{code, ssn}(Registered) \div \pi_{ssn}(Student)$

## Page 97

**Consider the following relations :**

**Student (ssn, name, address, major)**
**Course (code, title)**
**Registered (ssn, code)**

Use relational algebra to answer the following

9. List of course in which all ECMP major students are registered

$\Pi_{ssn, code}(Registered) \div \Pi_{ssn}(\sigma_{major = 'ECMP'}(Student))$

## Page 98

# Database Management System

**UNIT 2**
**Relational data model and language**
**Lecture-6**

**Today's Target**
* Modification on database and division numerical

By PRAGYA RAJVANSHI
B.Tech, M.Tech( C.S.E.)

## Page 99

# Modification of database(tuple by tuple)

**1. Deletion**
$R \leftarrow R - E$
$E \{$ Relation algebra expression whose output is union compatible with $R \}$

**2. Insertion**
$R \leftarrow R \cup E$

**3. Updation**

---
**Handwritten Notes:**

$\text{Assignment Operator}$
$A \leftarrow A \cup B$

$\text{NOTE}$
$\text{Division operator}$
$\text{Don't prefer } \text{ (symbol) } \rightarrow \text{ prefer } \div$
$R_1 \div R_2$

## Page 100

# QUERIES

1. book(**bid**, title, year_pub)
2. User(**card_no**, name, city)
3. Borrow(**bid**, **card_no**, DOI)
4. Supply(**bid**, sname, price, dos)

**Q.1** Delete all the entries of borrow relation.

$\text{Borrow} \leftarrow \text{Borrow} - \text{Borrow}$

***
*Watermark: Gateway classes*

## Page 101

# QUERIES

1. book(bid, title, year_pub)
2. User(card_no, name, city)
3. Borrow(bid, card_no, DOI)
4. Supply(bid, sname, price, dos)

**Q.2** Delete all the entries from borrow relation corresponding to cardn0= c101.

$\text{Borrow} \leftarrow \text{Borrow} - \sigma_{\text{cardno} = \text{c101}}(\text{Borrow})$

## Page 102

# QUERIES

1. book(bid, title, year_pub)
2. User(card_no, name, city)
3. Borrow(bid, card_no, DOI)
4. Supply(bid, sname, price, dos)

**Q.3 Abc has return all the books.**

$\text{Borrow} \leftarrow \text{Borrow} - \pi_{(\sigma_{\text{name='Abc'}} (\text{User} \bowtie \text{borrower}))}$
$\text{bid,}$
$\text{card\_no, DOI}$

Gateway classes

## Page 103

# QUERIES

1. book(**bid**, title, year_pub)
2. User(**card_no**, name, city)
3. Borrow(**bid**, **card_no**, DOI)
4. Supply(**bid**, sname, price, dos)

**Q.4 Abc has return all DBMS book.**

$\text{Borrow} \rightarrow \text{Borrow} \rightarrow \Pi_{\text{bid, Card no, DOI}} (\sigma_{\text{name='Abc' } \wedge \text{ title='DBMS'}} (\text{User} \bowtie \text{borrow} \bowtie \text{book}))$

## Page 104

# QUERIES

1. book(bid, title, year_pub)
2. User(card_no, name, city)
3. Borrow(bid, card_no, DOI)
4. Supply(bid, sname, price, dos)

**Q.5** Abc has return all book issue on 12-12-19.

$\pi_{bid, card\_no, DOI} (\sigma_{name = 'Abc' \wedge DOI = 12-12-19} (User \bowtie Borrow))$

Gateway classes

## Page 105

# QUERIES

1. book(bid, title, year_pub)
2. User(card_no, name, city)
3. Borrow(bid, card_no, DOI)
4. Supply(bid, sname, price, dos)

**Q.6 Delete all the entries of book having price more than 1000 from book table.**

$\text{book} \leftarrow \text{book} - \pi_{\text{bid, title, year\_pub}} (\sigma_{\text{Price} > 1000} (\text{book} \bowtie \text{Supply}))$

## Page 106

# QUERIES

1. book(**bid**, title, year_pub)
2. User(**card_no**, name, city)
3. Borrow(**bid**, **card_no**, DOI)
4. Supply(**bid**, sname, price, dos)

**Q.7** Insert an entry into book having bid=101 year_pub =Y, title=DBMS

$\text{book} \leftarrow \text{book} \cup \{ 101, \text{DBMS}, Y \}$

***

*Watermark text: Gateway classes*

## Page 107

# QUERIES

1. book(**bid**, title, year_pub)
2. User(**card_no**, name, city)
3. Borrow(**bid**, **card_no**, DOI)
4. Supply(**bid**, sname, price, dos)

**Q.8** Abc has issued a book on 21-2-18 having bid=b101

$\text{Borrow} \cup \{b101, R, 21-2-18\}$

$R \leftarrow \pi_{\text{Card no}} (\sigma_{\text{name='Abc'}} (\text{User}))$

## Page 108

# QUERIES

1. book(**bid**, title, year_pub)
2. User(**card_no**, name, city)
3. Borrow(**bid**, **card_no**, DOI)
4. Supply(**bid**, sname, price, dos)

**Q.9** Give 5% discount on all books.

$\text{Supply} \leftarrow \Pi_{\text{(Supply)}}$
$\text{bid, Sname, price * .95 as price, dos}$

## Page 109

# QUERIES

1. **book**(bid, title, year_pub)
2. **User**(card_no, name, city)
3. **Borrow**(bid, card_no, DOI)
4. **Supply**(bid, sname, price, dos)

**Q.10 Give 5% discount on all books supplied by Abc having price > 1000.**

$\text{Supply} \left( \text{Supply} - \sigma_{\text{name} = \text{"Abc"} \wedge \text{price} > 1000} (\text{Supply}) \right)$

$\Pi_{\text{bid, sname, price * 0.95 as price, dos}} \left( \sigma_{\text{name} = \text{"Abc"} \wedge \text{price} > 1000} (\text{Supply}) \right)$

## Page 110

# QUERIES

1. book(bid, title, year_pub)
2. User(card_no, name, city)
3. Borrow(bid, card_no, DOI)
4. Supply(bid, sname, price, dos)

**Q.1 Find the name of that supplier who has supplied <u>all the books issued to abc</u>**

$\Pi_{bid, sname}(\text{Supply})$
$\div$
$\sigma_{\text{name='abc'}}(\text{User} \bowtie \text{Borrow})$
$\Pi_{bid}$

## Page 111

# QUERIES

1. book(**bid**, title, year_pub)
2. User(**card_no**, name, city)
3. Borrow(**bid**, **card_no**, DOI)
4. Supply(**bid**, sname, price, dos)

**Q.2** Find the names of those supplier who have supplied all the books of same title issue to abc

$\Pi_{sname, (\text{Supply} \bowtie \text{Book})}$
$\div$
$\Pi_{title} (\sigma_{name = 'abc'} (\text{User} \bowtie \text{Borrow} \bowtie \text{book}))$

## Page 112

# AKTU QUESTION

**Q.1** Consider the following schema for institute library:
Student (**RollNo**, Name, Father_Name, Branch)
Book (**ISBN**, Title, Author, Publisher)
Issue (**RollNo, ISBN**, Date-of-Issue)

Write the following queries in SQL and relational algebra:
(i) List roll number and name of all students of the branch 'CSE'.
(ii) Find the name of student who has issued a book published by 'ABC' publisher.
(iii) List title of all books and their authors issued to a student 'RAM'.
(iv) List title of all books issued on or before December 1, 2020.
(v) List all books published by publisher 'ABC'

**AKTU**
**2023-24/**
**2022-23**

## Page 113

# AKTU QUESTION

**Q.2**
Consider the following Scheme:
SUPPLIER (**SUPPLIER ID**, SUPPLIER_NAME, SUPPLIER_ADDRESS)
PARTS (**PART ID**, PART_NAME, COLOR)
CATALOG (**SUPPLIER ID, PART ID**, COST)

Write the following queries in Relational Algebra
(i) Find the name of the suppliers who supply Black Parts.
(ii) Find the name of suppliers who supply both Blue and Black Parts.
(iii) Find the name of suppliers who supply all Parts.

**AKTU 2018-19**

## Page 114

# Database Management System

**UNIT 2**
**Relational data model and language**
Lecture-7

**Today's Target**
* Relational calculus
* PYQs

By PRAGYA RAJVANSHI
B.Tech, M.Tech( C.S.E.)

## Page 115

# Relational Calculus

* Relational calculus is a non-procedural query language.
* Relational Algebra has same power as Relational calculus.

They are of two types-
1. Tuple relational Calculus.
2. Domain relational Calculus.

---

# 1. TUPLE Relational calculus

* $\{t \mid \text{COND}(t)\}$

where $t$ is a tuple variable and $\text{COND}(t)$ is a conditional expression involving $t$. The result of such a query is the set of all tuples $t$ that satisfy $\text{COND}(t)$.

## Page 116

Many of the calculus expressions involves the use of Quantifiers. There are two types of quantifiers:

1. **Universal Quantifiers:** The universal quantifier denoted by $\forall$ is read as for all which means that in a given set of tuples exactly all tuples satisfy a given condition.

2. **Existential Quantifiers:** The existential quantifier denoted by $\exists$ is read as for all which means that in a given set of tuples there is at least one occurrences whose value satisfy a given condition.

## Page 117

**Employee**( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**(Dname, Dnumber, MGRSSN, MGRST ARTDATE)

**Dept_location**(Dnumber, Dlocation)

**Project**(Pname, Pnumber, Plocation, Dnum)

**Works_on**(EESN, Pno, Hours)

**Dependent**(Essn, Dependent_name, sex, Bdate, Reationship)

---

**Q.1** list all the employee details.
$\{t \mid Employee(t)\}$

## Page 118

**Employee**( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**(Dname, Dnumber, MGRSSN, MGRST ARTDATE)

**Dept_location**(Dnumber, Dlocation)

**Project**(Pname, Pnumber, Plocation, Dnum)

**Works_on**(EESN, Pno, Hours)

**Dependent**(Essn Dependent_name, sex, Bdate, Reationship)

***

**Q.2** find all employees whose salary is above 50,000.

$\{t \mid Employee(t) \text{ AND } t.Salary > 50,000\}$

## Page 119

**Employee**( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**(Dname, Dnumber, MGRSSN, MGRST ARTDATE)

**Dept_location**(Dnumber, Dlocation)

**Project**(Pname, Pnumber, Plocation, Dnum)

**Works_on**(EESN, Pno, Hours)

**Dependent**(Essn Dependent_name, sex, Bdate, Relationship)

***

**Q.3 find first name and last name employees whose salary is above 50,000.**

$\{\text{t.Fname, t.Lname} \mid \text{Employee}(t) \text{ AND } t.\text{Salary} > 50,000\}$

## Page 120

**Employee**( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**( Dname, Dnumber, MGRSSN, MGRST ARTDATE) Research

**Dept_location**( Dnumber, Dlocation)

**Project**( Pname, Pnumber, Plocation, Dnum)

**Works_on**( EESN, Pno, Hours)

**Dependent**( Essn Dependent_name, sex, Bdate, Reationship)

***

**Q.4** Retrieve the birth date and address of the employee (or employees) whose name is 'John B. Smith.

$\{\text{t.Bdate, t.Address} \mid \text{Employee(t) AND Fname='John' AND Minit='B' AND Lname='Smith'}\}$

## Page 121

# Example Queries Using the Existential Quantifier

**Q.5** Retrieve the name and address of all employees who work for the 'Research' department.

$\{\ t.Fname, t.Minit, t.Lname / Employee(t) \text{ AND } (\exists k)( \text{ t.Address}$
$\text{Department}(k) \text{ AND } k.Dname = \text{'Research'}$
$\text{t.Dno} = k.Dnumber) \}$

*Watermark: Gateway classes*

## Page 122

# QUERIES

1. book(bid, **title**, year_pub)
2. User(card_no, name, city)
3. Borrow(bid, card_no, DOI)
4. Supply(bid, sname, price, dos)

**Q.6 All the books Available in library.**
$\{ t \mid \text{book}(t) \}$

---

**Q.7 Give all the information about all Dbms books**
$\{ t \mid \text{book}(t) \text{ AND } t.\text{title} = \text{'Dbms'} \}$

| bid | title | year_pub |
| :--- | :--- | :--- |
| 1 | DBMS | 2016 |
| 2 | A2 | 2017 |
| 3 | DBMS | 2018 |
| 4 | RL | 2019 |

| 1 | DBMS | 2016 |
| :--- | :--- | :--- |
| 3 | DBMS | 2018 |

## Page 123

# QUERIES

1. book(**bid**, title, year_pub)
2. User(**card_no**, name, city)
3. Borrow(**bid**, **card_no**, DOI)
4. Supply(**bid**, sname, price, dos)

**Q.8** Give all the information about all the all user who lives in Delhi.
$\{ t \mid \text{User}(t) \text{ AND } t.\text{city} = \text{'Delhi'} \}$

---

*(Handwritten section on the right)*

$Q \quad \text{title} = \text{'DBMS'} \quad \text{year\_pub} = \text{'2018'}$
$\{ t \mid \text{book}(t) \text{ AND } t.\text{title} = \text{'DBMS'} \text{ AND } t.\text{Yearpub} = 2018 \}$

## Page 124

# QUERIES

1. **book**(bid, title, year_pub)
2. **User**(card_no, name, city)
3. **Borrow**(bid, card_no, DOI)
4. **Supply**(bid, sname, price, dos)

**Q.9 Find All book supplied by Abc**

$\{t \mid \text{book}(t) \text{ AND } (\exists S)(\text{Supply}(S) \text{ AND } S.\text{sname} = \text{'Abc' AND } S.\text{bid} = t.\text{bid})\}$

## Page 125

# Database Management System

**UNIT 2**
**Relational data model and language**
Lecture-8

**Today's Target**
$\text{>}$ Relational calculus
$\text{AKTU PYQs}$

By PRAGYA RAJVANSHI
B.Tech, M.Tech( C.S.E.)

## Page 126

# Text Extraction

**Left Column (Schema Definitions):**

*   **Employee**( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)
*   **Department**(Dname, Dnumber, MGRSSN, MGRST ARTDATE)
*   **Dept_location**(Dnumber, Dlocation)
*   **Project**(Pname, Pnumber, Plocation, Dnum)
*   **Works_on**(EESN, Pno, Hours)
*   **Dependent**( Essn, Dependent_name, sex, Bdate, Reationship)

**Right Column (Problem and Solution):**

**Q.1 Find the names of employees who have no dependents.**

$\{\text{e.Fname, e.Lname} \mid \text{Employee(e) AND (NOT } (\exists d)(\text{Dependent(d) AND (e.SSN = d.ESSN)))} \}$

$\downarrow \text{formula's}$

$\{\text{e.Fname, e.Lname} \mid \text{Employee(e) AND } (\text{NOT } (\forall d)(\text{NOT(Dependent(d) OR (NOT(essN = d.ESSN)))})) \}$

## Page 127

$((\forall x) P(x)) \rightarrow \text{NOT}(\exists x) (\text{NOT } P(x))$

$((\exists x) (P(x)) \rightarrow \text{NOT}(\forall x) (\text{NOT } P(x))$

$(\forall x) (P(x) \text{ and } Q(x)) \rightarrow \text{NOT}(\exists x) (\text{NOT } P(x) \text{ OR}(\text{NOT}(Q(x))))$

$(\forall x) (P(x) \text{ OR } Q(x)) \rightarrow \text{NOT}(\exists x) (\text{NOT } P(x)) \text{ AND } (\text{NOT}(Q(x)))$

$(\exists x) (P(x) \text{ OR } Q(x)) \rightarrow \text{NOT}(\forall x) ((\text{NOT } P(x)) \text{ AND } (\text{NOT } Q(x))$

$(\exists x) (P(x) \text{ and } Q(x)) \rightarrow \text{NOT}(\forall x) ((\text{NOT } P(x)) \text{ OR } (\text{NOT } Q(x))$

## Page 128

# Text Extraction

**GW GATEWAY CLASSES**

**Employee**(Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**(Dname, Dnumber, MGRSSN, MGRST ARTDATE)

**Dept_location**(Dnumber, Dlocation)

**Project**(Pname, Pnumber, Plocation, Dnum)

**Works_on**(EESN, Pno, Hours)

**Dependent**(Essn, Dependent_name, sex, Bdate, Relationship)

---

**Q.2 List the names of managers who have at least one dependent.**

$\{\text{e.Fname, e.Lname} \mid \text{Employee(e) AND } (\exists d)(\exists p) (\text{department}(d) \text{ And } (\text{dependent}(p) \text{ And } d.MGRSSN = e.SSN \text{ AND } p.ESSN = e.SSN))\}$

**GW GATEWAY CLASSES**

## Page 129

```markdown
**Employee**( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**(Dname, Dnumber, MGRSSN, MGRST ARTDATE)

**Dept_location**(Dnumber, Dlocation)

**Project**(Pname, Pnumber, Plocation, Dnum)

**Works_on**(EESN, Pno, Hours)

**Dependent**(Essn, Dependent_name, sex, Bdate, Relationship)

**Q.3 Find the names of employees who work on all the projects controlled by department number 5.**

$\{\text{e.Fname, e.Lname} \mid \text{Employee(e)} ((\forall x) (\text{No7 Project}(x) \text{ OR } (\text{NOT } (x.\text{DUM} = 5))) \text{ OR } ((\exists w)) (\text{Work on}(w) \text{ AND } w.\text{SSN} = e.\text{SSN AND } x.\text{Pnumbe} = w.\text{PNO}))) \}$

$\{\text{e.Fname, e.Lname} \mid \text{Employee(e)} ((\forall x) (\exists w) (\text{project}(x) \text{ AND } \text{Work on}(w) \text{ AND } x.\text{DNum} = 5 \text{ AND } w.\text{ESSN} = e.\text{SSN AND } x.\text{PNumber} = w.\text{PNO})) \}$
```

## Page 130

Employee( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)
Department(Dname, Dnumber, MGRSSN, MGRST, ARTDATE)
Dept_location(Dnumber, Dlocation)
Project(Pname, Pnumber, Plocation, Dnum)
Works_on(EESN, Pno, Hours)
Dependent(Essn, Dependent_name, sex, Bdate, Reationship)

**Q.4 Make a list of project numbers for projects that involve an employee whose last name is 'Smith', either as a worker or as manager of the controlling department for the project**

$\{ P.Pnumber \mid Project(P) \text{ AND } ((\exists e)(\exists w) (Employee(e) \text{ AND } Works\_on(w) \text{ AND } e.Lname = 'smith' \text{ AND } e.SSN = w.ESSN \text{ AND } P.Pnumber = w.ESSN)) \text{ OR } ((\exists m)(\exists d) (department(d) \text{ AND } Employee(m) \text{ AND } m.Lname = 'Smith' \text{ AND } m.SSN = d.MGRSSN \text{ AND } d.Dnumber = P.Dnum)))\}$

## Page 131

# Safe Expressions

* Whenever we use universal quantifiers, existential quantifiers, or negation of predicates in a calculus expression, we must make sure that the resulting expression makes sense.
* A safe expression in relational calculus is one that is guaranteed to yield a finite number of tuples as its result; otherwise, the expression is called unsafe.

For example, the expression $\{t \mid \text{NOT (EMPLOYEE(t))}\}$

$\text{It is unsafe because it yields all tuples in the universe that are not EMPLOYEE tuples, which are infinitely numerous.}$

$\{t \mid \text{NOT Employee(t)}\}$

## Page 132

# Database Management System

**UNIT 2**
**Relational data model and language**
**Lecture-9**

**Today's Target**
* Domain Calculus
* AKTU PYQs

By PRAGYA RAJVANSHI
B.Tech, M.Tech( C.S.E.)

## Page 133

# Domain relational calculus

* Domain calculus differs from tuple calculus in the type of variables used in formulas.
* Rather than having variables range over tuples, the variables range over single values from domains of attributes.
* An expression of the domain calculus is of the form
* {a1,a2,a3 | P}

## Page 134

# Left Column

**Employee**( **Fname**, Minit, **Lname**, **SSN**, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**(Dname, **Dnumber**, MGRSSN, MGRSTARTDATE)

**Dept_location**(**Dnumber**, **Dlocation**)

**Project**(Pname, **Pnumber**, Plocation, Dnum)

**Works_on**(**EESN**, **Pno**, Hours)

**Dependent**(**Essn**, **Dependent_name**, sex, Bdate, Relationship)

---

# Right Column

**Q.1** Retrieve the birthdate and address of the employee whose name is 'John B. Smith.

$\{U, V \mid (\exists q)(\exists r)(\exists s) (\text{Employee}(q, r, s, t, U, V, w, x, y, z) \text{ AND } q = \text{'John' AND } r = \text{'B' AND } s = \text{'Smith'})\}$

## Page 135

```markdown
# Left Panel
**Employee**( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**(Dname, Dnumber, MGRSSN, MGRSTARTDATE)

**Dept_location**(Dnumber, Dlocation)

**Project**(Pname, Pnumber, Plocation, Dnum)

**Works_on**(EESN, Pno, Hours)

**Dependent**( Essn, Dependent_name, sex, Bdate, Relationship)

# Right Panel
**Q.2 Retrieve the name and address of all employees who work for the 'Research' department.**

$\{\pi_{name, address} (\sigma_{Dname='Research'} (Employee \bowtie Department))\}$
*(Note: The handwritten part contains a relational algebra expression attempting to solve the query)*
```

## Page 136

**Employee**( Fname, Minit, Lname, **SSN**, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**( Dname, **Dnumber**, MGRSSN, MGRSTARTDATE)

**Dept_location**( **Dnumber**, **Dlocation**)

**Project**( Pname, **Pnumber**, Plocation, Dnum)

**Works_on**( **EESN**, **Pno**, Hours)

**Dependent**( Essn, Dependent_name, sex, Bdate, Relationship)

***

**Q.3** For every project located in 'Stafford' list the project number, the controlling department number, and the department manager's last name, birth date, and address.

## Page 137

**Employee**( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)

**Department**(Dname, Dnumber, MGRSSN, MGRSTARTDATE)

**Dept_location**(Dnumber, Dlocation)

**Project**(Pname, Pnumber, Plocation, Dnum)

**Works_on**(EESN, Pno, Hours)

**Dependent**( Essn, Dependent_name, sex, Bdate, Relationship)

***

**Q.4 Find the names of employees who have no dependents.**

$\{ q \mid \exists r, s \ ( \exists t) (\text{Employee}(q, r, s, t, u, v, w, x, y, z) \text{ AND } \neg (\exists a) (\text{Dependent}(a, b, c, d, e) \text{ AND } a = t)) \}$

<u>having dependency</u>
$\{ q, r, s \mid (\exists t) (\exists a) (\text{Employee}(q, r, s, t, u, v, w, x, y, z) \text{ AND } \text{Dependent}(a, b, c, d, e) \text{ AND } a = t) \}$

## Page 138

# Text Extraction

**Left Panel:**
* Employee( Fname, Minit, Lname, SSN, Bdate, Address, Sex, Salary, SuperSsn, Dno)
* Department(Dname, Dnumber, MGRSSN, MGRSTARTDATE)
* Dept_location(Dnumber, Dlocation)
* Project(Pname, Pnumber, Plocation, Dnum)
* Works_on(EESN, Pno, Hours)
* Dependent( Essn, Dependent_name, sex, Bdate, Relationship)

**Right Panel:**
* **Q.5** List the names of managers who have at least one dependent.
* $\text{Gateway classes}$ (Watermark)
* $\{ q \text{ r s } \mid (\exists t) (\exists w) (\exists a) (\text{Employee } e \text{ cares } s + \text{ upwxy})$
* $\text{AND Department (Lm no)}$
* $\text{AND Dependent ( a b c d e )}$
* $\text{AND } t = n \text{ AND } t = a ) \}$
* $\{ n \mid (\exists L) (\text{Department (Lm no) ANDL = 'ALML'})$

## Page 139

# Thank you
