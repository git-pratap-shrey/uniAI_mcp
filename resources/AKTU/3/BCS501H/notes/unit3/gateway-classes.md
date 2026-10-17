
## Page 1

# AKTU
**B.Tech III-Year** | **5th Semester** | **GW GATEWAY CLASSES**

## CS IT & CS Allied
# DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-1**

---

**Today's Target**
* Functional dependency
* AKTU PYQs

---

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 2

# (BCS-501- Database Management System)

## Unit-III : Data Base Design & Normalization

**Data Base Design & Normalization:** Functional dependencies, normal forms, first, second, 8 third normal forms, BCNF, inclusion dependence, loss less join decompositions, normalization using FD, MVD, and JDs, alternative approaches to database design

## Page 3

# AKTU : B.Tech (V-Sem)
**GATEWAY CLASSES (GW)**

| S.N. | CS IT & CS Allied COMBO PACK (3 Subjects) |
| :--- | :--- |
| 1 | BCS501-Database Management System |
| 2 | BCS502: Web Technology |
| 3 | BCS503: Design and Analysis of Algorithm |

Course Link in Description (Download the app now)
✓ Helpline No. 7819 0058 53

## Page 4

# Functional dependency

* A functional dependency, denoted by $\text{X} \rightarrow \text{Y}$ between two sets of attributes $\text{X}$ and $\text{Y}$ that are subsets of $\text{R}$ specifies a constraint on the possible tuples that can form a relation state $r$ of $\text{R}$.
* The constraint is that, for any two tuples $\text{t1}$ and $\text{t2}$ in $r$ that have $\text{t1[X]} = \text{t2[X]}$, they must also have $\text{t1[Y]} = \text{t2[Y]}$.
* The abbreviation for functional dependency is $\text{FD}$ or $\text{f.d}$.

---

**f.d.::x->y R**

| x | y |
|---|---|
| a | 1 |
| b | 2 |
| c | 3 |
| d | 4 |

$\text{x} \rightarrow \text{y}$

| x | y |
|---|---|
| a | 1 |
| a | 2 |
| c | 3 |
| d | 4 |

## Page 5

# ROLE OF FUNCTIONAL DEPENDENCY IN DATABASE DESIGN

1. **Normalization:** FDs help identify and eliminate data redundancy by guiding the decomposition of tables into smaller, related tables, which reduces anomalies (insertion, update, and deletion issues).

2. **Determining Keys:** FDs assist in identifying candidate keys in a relation, ensuring each tuple is unique and the data is properly organized.

3. **Schema Optimization:** They ensure an efficient database structure by organizing data into tables that accurately reflect real-world relationships without unnecessary duplication.

4. **Data Integrity:** FDs enforce constraints that maintain data consistency, making sure that related data entries align across tables.

## Page 6

# TEACHS

| TEACHER | COURSE | TEXT |
| :--- | :--- | :--- |
| SMITH | DS | BB |
| SMITH | DM | HH |
| HALL | COMPILER | XC |
| BROWN | DS | ZZ |

1. TEXT $\rightarrow$ COURSE (YES)
2. TEACHER $\rightarrow$ COURSE (NO)
3. TEXT $\rightarrow$ TEACHER (YES)
4. COURSE $\rightarrow$ TEXT (NO)

***

| Ssn | Pnumber | Hours | Pname | Plocation |
| :--- | :--- | :--- | :--- | :--- |
| 123456789 | 1 | 32.5 | ProductX | Bellaire |
| 123456789 | 2 | 7.5 | ProductY | Sugarland |
| 6668844444 | 3 | 40.0 | ProductZ | Houston |
| 453453453 | 1 | 20.0 | ProductX | Bellaire |
| 453453453 | 2 | 20.0 | ProductY | Sugarland |
| 3334455555 | 2 | 10.0 | ProductY | Sugarland |
| 3334455555 | 3 | 10.0 | ProductZ | Houston |
| 3334455555 | 10 | 10.0 | Computerization | Stafford |
| 3334455555 | 20 | 10.0 | Reorganization | Houston |
| 9998877777 | 30 | 30.0 | Newbenefits | Stafford |
| 9998877777 | 10 | 10.0 | Computerization | Stafford |
| 987987987 | 10 | 35.0 | Computerization | Stafford |
| 987987987 | 30 | 5.0 | Newbenefits | Stafford |
| 987654321 | 30 | 20.0 | Newbenefits | Stafford |
| 987654321 | 20 | 15.0 | Reorganization | Houston |
| 8886655555 | 20 | NULL | Reorganization | Houston |

A. Pnumber $\rightarrow$ {Pname, Plocation} Yes
B. {Ssn, Pnumber} $\rightarrow$ Hours Yes $\text{Pnumber} \rightarrow \text{Hours} \times$
$\text{SSN} \rightarrow \text{Hours} \times$

All hold true

## Page 7

| EMPLOYEE | | | | |
| :--- | :--- | :--- | :--- | :--- |
| **Ename** | **Ssn** | **Bdate** | **Address** | **Dnumber** |
| Smith, John B. | 123456789 | 1965-01-09 | 731 Fondren, Houston, TX | 5 |
| Wong, Franklin T. | 333445555 | 1955-12-08 | 638 Voss, Houston, TX | 5 |
| Zelaya, Alicia J. | 999887777 | 1968-07-19 | 3321 Castle, Spring, TX | 4 |
| Wallace, Jennifer S. | 987654321 | 1941-06-20 | 291 Berry, Bellaire, TX | 4 |
| Narayan, Ramesh K. | 666884444 | 1962-09-15 | 975 Fire Oak, Humble, TX | 5 |
| English, Joyce A. | 453453453 | 1972-07-31 | 5631 Rice, Houston, TX | 5 |
| Jabbar, Ahmad V. | 987987987 | 1969-03-29 | 980 Dallas, Houston, TX | 4 |
| Borg, James E. | 888665555 | 1937-11-10 | 450 Stone, Houston, TX | 1 |

a. Ssn $\rightarrow$ Ename
All hold true

## Page 8

# Which of the following satisfied functional dependencies

| A | B | C | D | E |
|---|---|---|---|---|
| a | 2 | 3 | 4 | 5 |
| 2 | A | 3 | 4 | 5 |
| a | 2 | 3 | 6 | 5 |
| a | 2 | 3 | 6 | 6 |

1. A->BC (yes)
2. DE->C (yes)
3. C->DE (NO)
4. BC->A (yes)

**Note x->y**
* If all values of x are unique, Irrespective of the y the functional dependencies always hold good.
* If all value of y are same the functional dependencies always good.

## Page 9

NOTE: X->Y

Y component of a tuple in r depend on, or are determined by, the values of the X component; alternatively, the values of the X component of a tuple uniquely (or functionally) determine the values of the Y component

Functional dependencies can be classified as trivial or non-trivial based on the relationship between the dependent attributes.

1. Trivial Functional Dependency:
A functional dependency X$\rightarrow$Y is trivial, if Y$\subseteq$X
This means that the dependent attributes Y are already part of the determinant X, so the dependency provides no new information.

Example: {A,B}$\rightarrow$A is trivial because A is already included in {A,B}.

(Handwritten notes: $ABC \rightarrow A$)

## Page 10

# 2 .Non-Trivial Functional Dependency:

* A functional dependency $X \rightarrow Y$ is non-trivial if $Y$ is not a subset of $X$.
* Here, the dependency implies that $Y$ depends solely on $X$ without being part of it, giving <ins>new information</ins> about data relationships.
* Example: $\text{AB} \rightarrow \text{D}$

## Page 11

# Left Table
| X | Y | Z |
|---|---|---|
| 1 | 4 | 2 |
| 1 | 5 | 3 |
| 1 | 6 | 3 |
| 3 | 2 | 2 |

**Which of the following satisfies the functional dependencies**
1. $\text{xy} \rightarrow \text{z}$ and $\text{z} \rightarrow \text{y} \rightarrow \text{False}$
2. $\text{yz} \rightarrow \text{x}$ and $\text{y} \rightarrow \text{z} \rightarrow \text{True}$
3. $\text{yz} \rightarrow \text{x}$ and $\text{x} \rightarrow \text{z} \rightarrow \text{False}$
4. $\text{xz} \rightarrow \text{y}$ and $\text{y} \rightarrow \text{z} \rightarrow \text{False}$

---

# Right Table
| A | B | C |
|---|---|---|
| 1 | 2 | 4 |
| 3 | 5 | 4 |
| 3 | 7 | 2 |
| 1 | 4 | 2 |

**Which of the following satisfies the functional dependencies**
1. $\text{A} \rightarrow \text{B}$ and $\text{BC} \rightarrow \text{A} \rightarrow \text{False}$
2. $\text{C} \rightarrow \text{A}$ and $\text{CA} \rightarrow \text{B} \rightarrow \text{False}$
3. $\text{B} \rightarrow \text{C}$ and $\text{AB} \rightarrow \text{C} \rightarrow \text{True}$
4. $\text{A} \rightarrow \text{C}$ and $\text{BC} \rightarrow \text{A} \rightarrow \text{False}$

## Page 12

# Attribute closure/closure on attribute set/closure of attribute set

Attribute closure of an attribute set can be defined as set of attributes which can be functionally determined from it.

**1. R(A,B,C)**
A->B
B->C
$(A)^+ = \{A, B, C\}$

---

**2. R(A B C D E F)**
A->B
C->DE
AC->F
D->AF
E->CF
$(DE)^+ = \{D, E, A, F, C, B\}$

---

**3. R(A B C D E F G)**
A->B
BC->DE
AEG->G
$(AC)^+ = \{A, C, B, D, E\}$

**4. R(A B C D E)**
A->BC
CD->E
B->D
E->A
$B^+ \{B, D\}$

## Page 13

# AKTU QUESTIONS

| Question No. | Question | Year |
| :--- | :--- | :--- |
| **Q.1** | What is functional dependency? Explain its role in database design. | AKTU 2018-19 |
| **Q.2** | Explain the functional dependency? Explain trivial and non trivial functional dependency. <br> $Q = (\text{functional determinant or not})$ | AKTU 2012-13/ AKTU 2021-22 |

## Page 14

# AKTU | B.Tech III-Year | 5th Semester | GW (GATEWAY CLASSES)

**CS IT & CS Allied**

## DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-2**

**Today's Target**
* Armstrong Axiom rule ✓
* Equivalence of functional dependency
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 15

# ARMSTRONG AXIOM RULE/
## INFERENCE RULE FOR FUNCTIONAL DEPENDENCY

Axiom is a statement that is taken to be true and serve as a premise or starting point for further argument.

1. **Primary rules(RAT)**

    a. **Axiom of Reflexivity:** If A is a set of attributes and B is a subset of A, then A holds B. If $B \subseteq A$ then $A \rightarrow B$.
    
    This property is trivial property.

***

The axiom states:

If B is a subset of A then . A->B

$\text{➢}$ This means if we know the values of all attributes in A, we automatically know the values of all attributes in B because B is included in A.

Consider a **Customer** table with attributes { CustomerID, Name, Age, Address }

X={CustomerID, Name}
Y={Name}

CustomerID, Name $\rightarrow$ {Name}

If you know both the CustomerID and the Name, you definitely know the Name, because it is already part of the information you have.

***
*AKTU 2018-19, 2021-22, 2022-23*

## Page 16

b. **Axiom of Augmentation**: If $\text{A} \rightarrow \text{B}$ holds and $\text{Y}$ is the attribute set, then $\text{AY} \rightarrow \text{BY}$ also holds. That is adding attributes to dependencies, does not change the basic dependencies.

Consider a table **Student**(ID, Name, Age, Grade):
* Given: $\text{ID} \rightarrow \text{Name}$ (ID uniquely determines Name).
* By Augmentation: $\text{ID, Age} \rightarrow \text{Name, Age}$.
* we augmented both sides by adding the attribute Age, and the dependency still holds.

c. **Axiom of Transitivity**: Same as the transitive rule in algebra, if $\text{A} \rightarrow \text{B}$ holds and $\text{B} \rightarrow \text{C}$ holds, then $\text{A} \rightarrow \text{C}$ also holds.

Consider a table **Employee**(ID, Department, Manager):
* Given: $\text{ID} \rightarrow \text{Department}$
* $\text{Department} \rightarrow \text{Manager}$ (Department determines Manager).
* By Transitivity: $\text{ID} \rightarrow \text{Manager}$.
* This shows that knowing the ID is enough to determine the Manager because of the chain of dependencies.

## Page 17

# Secondary Rules

These rules can be derived from the above axioms.

**a. Union:** If $\text{A} \rightarrow \text{B}$ holds and $\text{A} \rightarrow \text{C}$ holds, then $\text{A} \rightarrow \text{BC}$ holds.
If $\text{X} \rightarrow \text{Y}$ and $\text{X} \rightarrow \text{Z}$ then $\text{X} \rightarrow \text{YZ}$.

**b. Composition:** If $\text{A} \rightarrow \text{B}$ and $\text{X} \rightarrow \text{Y}$ hold, then $\text{AX} \rightarrow \text{BY}$ holds.

**c. Decomposition:** If $\text{A} \rightarrow \text{BC}$ holds then $\text{A} \rightarrow \text{B}$ and $\text{A} \rightarrow \text{C}$ hold.

**d. pseudo Transitivity:** If $\text{A} \rightarrow \text{B}$ holds and $\text{BC} \rightarrow \text{D}$ holds, then $\text{AC} \rightarrow \text{D}$ holds.

---

# Soundness and Completeness of Armstrong's Axioms

* Armstrong's axioms are a set of rules used in relational databases to infer all functional dependencies (FDs) from a given set.
* These rules help maintain data integrity and are fundamental in the process of database normalization.

***

**Header Info:**
* AKTU 2022-23
* GATEWAY CLASSES

## Page 18

# Soundness Definition:

* **Soundness** ensures that any functional dependency derived using Armstrong's axioms is logically correct and valid for the given set of FDs.

* **Explanation:** If we derive a new FD from the given set using Armstrong's axioms, that new FD must be true and consistent with the original set.

**Example: Given FDs:**
* A $\rightarrow$ B
* B $\rightarrow$ C

**Using transitivity (one of Armstrong's axioms):**
* A $\rightarrow$ B
* and B $\rightarrow$ C
* imply A $\rightarrow$ C.

Since A $\rightarrow$ C logically follows from the given FDs, the derivation is sound.

## Page 19

# Completeness

Let's consider a relation R with attributes {A, B, C, D} and the following functional dependencies:

* A $\rightarrow$ B
* B $\rightarrow$ C
* C $\rightarrow$ D

(Handwritten notes next to the list: A $\rightarrow$ C, A $\rightarrow$ D, B $\rightarrow$ D)

**Objective:** Show that using Armstrong's axioms, we can derive all possible functional dependencies that follow logically from the given set, demonstrating completeness.

---

# Using Armstrong's Axioms to Derive New FDs

**Applying Transitivity:**

From A $\rightarrow$ B and B $\rightarrow$ C, we can derive:
A $\rightarrow$ C

From A $\rightarrow$ C and C $\rightarrow$ D, we can derive:
A $\rightarrow$ D

**Applying Reflexivity:**

We can derive trivial FDs like:
A $\rightarrow$ A, B $\rightarrow$ B, C $\rightarrow$ C, D $\rightarrow$ D.

## Page 20

# Applying Augmentation:

* From $\text{A} \rightarrow \text{B}$, we can augment with attribute $\text{C}$:
    * $\text{AC} \rightarrow \text{BC}$ (though it may not always be useful in this context).
* Similarly, from $\text{B} \rightarrow \text{C}$, augment with $\text{D}$:
    * $\text{BD} \rightarrow \text{CD}$.

---

# List of All Possible Inferred FDs

**AKTU 2018-19, 2021-22, 2022-23**

From the given set and using Armstrong's axioms, we derived:

$\text{A} \rightarrow \text{C}$
$\text{A} \rightarrow \text{D}$
$\text{B} \rightarrow \text{C}$
$\text{C} \rightarrow \text{D}$
$\text{A} \rightarrow \text{B}$ (given)

Reflexive FDs like $\text{A} \rightarrow \text{A}$, $\text{B} \rightarrow \text{B}$, etc.

* These are all the possible functional dependencies that can be logically inferred.

## Page 21

Armstrong's axioms allowed us to derive every FD that follows from the original set (A $\rightarrow$ C and A $\rightarrow$ D). This shows completeness, as no FD that logically follows from the given set was left out.

$\text{Completeness}$ means that Armstrong's axioms are capable of deriving all possible functional dependencies that logically follow from the given set.

$\text{If there are any FDs that can be inferred based on the given set, Armstrong's axioms should be able to derive them. No FD should be missed.}$

## Page 22

# Equivalence of functional dependency

**R(A C D E H)**

| | |
| :--- | :--- |
| **F**<br>A $\rightarrow$ C<br>AC $\rightarrow$ D<br>E $\rightarrow$ AD<br>E $\rightarrow$ H | **G**<br>A $\rightarrow$ CD<br>E $\rightarrow$ AH |

| using G | using F | using F | using G |
| :--- | :--- | :--- | :--- |
| $A^+ = \{A, C, D\}$ | $A^+ = \{A, C, D\}$ | $A^+ = \{A, C, D\}$ | $A^+ = \{A, C, D\}$ |
| $Ac^+ = \{A, C, D\}$ | $Ac^+ = \{A, C, D\}$ | $E^+ = \{E, A, D, H, C\}$ | $E^+ = \{E, A, H, C, D\}$ |
| $E^+ = \{E, A, H, C, D\}$ | $E^+ = \{E, A, D, H, C\}$ | $G \subseteq F$ | |
| $F \subseteq G$ | | | |

**F == G**

## Page 23

# Equivalence of functional dependency

**R(P Q R S)**

| X: | Y: |
| :--- | :--- |
| P $\rightarrow$ Q | P $\rightarrow$ QR |
| Q $\rightarrow$ R | R $\rightarrow$ S |
| R $\rightarrow$ S | |

---

| using Y | using X | using X | using Y |
| :--- | :--- | :--- | :--- |
| $P^+ = \{P, Q, R, S\}$ | $P^+ = \{P, Q, R, S\}$ | $P^+ = \{P, Q, R, S\}$ | $P^+ = \{P, Q, R, S\}$ |
| $Q^+ = \{Q\}$ | $Q^+ = \{Q, R, S\}$ | | $R^+ = \{R, S\}$ |
| $R^+ = \{R, S\}$ | $R^+ = \{R, S\}$ | $R^+ = \{R, S\}$ | |
| $X \not\subset Y$ | | $Y \subset X$ | |

**Gateway Classes**

## Page 24

# Equivalence of functional dependency

**R(A, B, C)**

| F | G |
| :--- | :--- |
| A $\rightarrow$ B | A $\rightarrow$ BC |
| B $\rightarrow$ C | B $\rightarrow$ A |
| C $\rightarrow$ A | C $\rightarrow$ A |

---

| Using G | Using F | Using F | Using G |
| :--- | :--- | :--- | :--- |
| $A^+ = \{A, B, C\}$ | $A^+ = \{A, B, C\}$ | $A^+ = \{A, B, C\}$ | $A^+ = \{A, B, C\}$ |
| $B^+ = \{A, B, C\}$ | $B^+ = \{B, C, A\}$ | $B^+ = \{B, C, A\}$ | $B^+ = \{B, A, C\}$ |
| $C^+ = \{A, B, C\}$ | $C^+ = \{C, A, B\}$ | $C^+ = \{B, C, A\}$ | $C^+ = \{C, A, B\}$ |
| $F \subseteq G$ | $\boxed{F = G}$ | $G \subseteq F$ | |

## Page 25

# Equivalence of functional dependency

**R(W X Y Z)**

| F: | G: |
| :--- | :--- |
| W -> X | W -> XY |
| WX -> Y | Z -> XY |
| Z -> WY | |
| Z -> Y | |

---

**Using G**
$w^+ = \{w, x, y\}$
$(wx)^+ = \{w, x, y\}$
$z^+ = \{z, x, y\}$

$G \not\subseteq F$

**Using F**
$w^+ = \{w, x, y\}$
$wx^+ \{wx, y\}$
$z^+ = \{z, w, y\}$

$F \not\subseteq G$

**Using G**
$wt = \{w, x, y\}$
$zt = \{z, x, y\}$

$G \not\subseteq F$

## Page 26

# AKTU QUESTION

| Question No. | Question | Year |
| :--- | :--- | :--- |
| **Q.1** | Describe Armstrong axiom in detail. What is the role of these rules in database development process. | AKTU 2021-22 <br> AKTU 2022-23 |
| **Q.2** | List the Armstrong axioms for functional dependencies? What do you understand by soundness and completeness of these axioms. | AKTU 2018-19 <br> AKTU 2020-21 |
| **Q.3** | What are the RAT axioms | AKTU 2018-19 |

## Page 27

# AKTU
**B.Tech III-Year** | **5th Semester** | **GW (GATEWAY CLASSES)**

**CS IT & CS Allied**

## DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-3**

---

**Today's Target**
* Canonical cover
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 28

# Role of the axiom rules in database development process

* The Armstrong axioms are a set of rules used in database theory to infer all possible functional dependencies (FDs) in a relational database.
* They play an important role in database normalization and schema design.

### 1. Validation of Functional Dependencies:
* Armstrong axioms help in checking whether a given set of FDs logically implies another FD.
* This is crucial to ensure the database schema respects all the necessary relationships.

### 2. Normalization Process:
* They are used to decompose tables by finding candidate keys and reducing redundancy, ensuring the schema is in a higher normal form.

### 3. Schema Optimization:
* The axioms help simplify the set of FDs, making it easier to understand and optimize the schema.

## Page 29

# (MINIMAL COVER/IRREDUCIBLE SET OF F.D./ Canonical Cover)

* Whenever a user updates the database, the system must check whether any functional dependencies are violated in this process.
* If there is a violation of dependencies in the new database state, the system must roll back. Working with a huge set of functional dependencies can cause unnecessary added computational time.
* This is where the canonical cover comes into play. A canonical cover of a set of functional dependencies $F$ is a simplified set of functional dependencies with the same closure as the original set $F$.
* A canonical cover is a minimal, equivalent set of functional dependencies with no redundancy in attributes or FDs.

## Page 30

# Procedure of canonical cover

In database management systems (DBMS), a canonical cover is a set of functional dependencies that is equivalent to a given set of functional dependencies but is minimal in terms of the number of dependencies.

The process of finding the canonical cover of a set of functional dependencies involves three main steps:

**1. Reduction:**
* The first step is to reduce the original set of functional dependencies to an equivalent set that has the same closure as the original set, but with fewer dependencies.
* This is done by removing redundant dependencies and combining dependencies that have common attributes on the left-hand side.

## Page 31

# Procedure of canonical cover

**2.Elimination:** The second step is to eliminate any extraneous attributes from the left-hand side of the dependencies. An attribute is considered extraneous if it can be removed from the left-hand side without changing the closure of the dependencies.

**3.Minimization:** The final step is to minimize the number of dependencies by removing any dependencies that are implied by other dependencies in the set.

## Page 32

# 1. R(W X Y Z)
X $\rightarrow$ W
WZ $\rightarrow$ XY
Y $\rightarrow$ WXZ

Find out canonical / minimal cover

## Decomposition
1. X $\rightarrow$ W
2. WZ $\rightarrow$ X
3. WZ $\rightarrow$ Y
4. Y $\rightarrow$ W
5. Y $\rightarrow$ X
6. Y $\rightarrow$ Z

① $X^+ = \{X, W\}$
Ignore X $\rightarrow$ W
$X^+ = \{X\}$

② $Wz^+ = \{W, Z, X, Y, Z\}$
Ignore WZ $\rightarrow$ X
$Wz^+ = \{W, Z, Y, X\}$

This will be removed

---

① X $\rightarrow$ W $\checkmark$
② WZ $\rightarrow$ Y $\checkmark$
③ Y $\rightarrow$ W
④ Y $\rightarrow$ X
⑤ Y $\rightarrow$ Z

$Wz^+ = \{W, Z, Y, X\}$
Ignore WZ $\rightarrow$ Y
$Wz^+ = \{W, Z\}$

$Y^+ = \{Y, W, X, Z\}$
Ignore Y $\rightarrow$ W
$Y^+ = \{Y, X, Z, W\}$ this will be ignored

① X $\rightarrow$ W $\checkmark$
② WZ $\rightarrow$ Y $\checkmark$
③ Y $\rightarrow$ Z $\checkmark$
Ignore Y $\rightarrow$ X
$Y^+ = \{Y, Z\}$

$Y^+ = \{Y, Z, W\}$
Ignore Y $\rightarrow$ Z = $\{Y, X, W\}$

---

X $\rightarrow$ W
WZ $\rightarrow$ Y
Y $\rightarrow$ Z

$Wz^+ = \{W, Z, Y, X\}$
$Wt = \{W\}$
$Zt = \{Z\}$

$\begin{array}{|l|} \text{X} \rightarrow \text{W} \\ \text{WZ} \rightarrow \text{Y} \\ \text{Y} \rightarrow \text{XZ} \end{array} \rightarrow \text{Minimal cover}$

## Page 33

# 2. R(A B C D)

**Functional Dependencies:**
* A $\rightarrow$ B
* C $\rightarrow$ B
* D $\rightarrow$ ABC
* AC $\rightarrow$ D

**Goal:** Find canonical cover

---

### Left Column: Decomposition
1. A $\rightarrow$ B $\checkmark$ $At = \{A, B\}$
2. C $\rightarrow$ B $\checkmark$ Ignore A $\rightarrow$ B
3. D $\rightarrow$ A $\checkmark$ $At = \{A\}$
4. D $\rightarrow$ B $\times$ $Ct = \{C, B\}$
5. D $\rightarrow$ C $\checkmark$ Ignore C $\rightarrow$ B
6. AC $\rightarrow$ D $\checkmark$ $Ct = \{C\}$

---

### Middle Column: Process
$Dt = \{D, A, B, C\}$
Ignore $\times$ D $\rightarrow$ A
$Dt = \{D, B, C\}$

$Dt = \{D, A, B, C\}$
Ignore D $\rightarrow$ B
$Dt = \{D, A, C, B\}$

$\text{DA} \rightarrow \text{B}$ $Dt = \{D, A, C, B\}$
$\text{C} \rightarrow \text{B}$ Ignore D $\rightarrow$ C
$\text{D} \rightarrow \text{A}$
$\text{D} \rightarrow \text{C}$ $Dt = \{D, A, B\}$
$\text{AC} \rightarrow \text{D}$

$Act = \{A, C, D, B\}$
Ignore AC $\rightarrow$ D
$Act = \{A, C, B\}$

---

### Right Column: Final Result
**Dependencies:**
* A $\rightarrow$ B
* C $\rightarrow$ B
* D $\rightarrow$ A
* D $\rightarrow$ C
* AC $\rightarrow$ D

$Act = \{A, C, D, A\}$
$At = \{A, B\}$
$Ct = \{C, B\}$

**Minimal Cover:**
$\begin{cases} \text{A} \rightarrow \text{B} \\ \text{C} \rightarrow \text{B} \\ \text{D} \rightarrow \text{AC} \\ \text{AC} \rightarrow \text{D} \end{cases}$

## Page 34

# Text Extraction

**Top Left:**
GW
GATEWAY CLASSES
3. $R(V W X Y Z)$

$V \rightarrow W$
$VW \rightarrow X$
$Y \rightarrow VXZ$

**Middle Left:**
① $V \rightarrow W$ $\checkmark$ $Vt = \{V, W, X\}$
② $VW \rightarrow X$ $\checkmark$ Ignore $V \rightarrow W$
③ $Y \rightarrow V$ $\checkmark$ $Vt = \{V\}$
④ $Y \rightarrow X$ $\checkmark$
⑤ $Y \rightarrow Z$ $\checkmark$ $Vwt = \{V, W, X\}$
Ignore $VW \rightarrow X$
$Vwt = \{V, W\}$

$Yt = \{V, X, Z, W\}$
Ignore $Y \rightarrow V$
$Yt = \{Y, X, Z\}$

**Top Center:**
$Yt = \{Y, V, X, Z, W\}$
Ignore $Y \rightarrow X$
$Yt = \{Y, V, W, Y, Z\}$

**Middle Center:**
① $V \rightarrow W$ $Yt = \{Y, V, X, Z\}$
② $VW \rightarrow X$
③ $Y \rightarrow V$ Ignore $Y \rightarrow Z$
④ $Y \rightarrow Z$ $Yt = \{Y, V, W, X\}$

**Gateway Classes** (Diagonal Watermark)

**Top Right:**
GW
GATEWAY CLASSES

$V \rightarrow W$
$VW \rightarrow X$
$Y \rightarrow V$
$Y \rightarrow Z$

**Middle Right:**
$Vwt = \{V, W, X\}$
$Vt = \{V, W, X\}$
$Wt = \{W\}$

(Minimal Cover)

$V \rightarrow W$
$V \rightarrow X$
$Y \rightarrow V$
$Y \rightarrow Z$

$\boxed{\begin{matrix} V \rightarrow W X \\ Y \rightarrow V Z \end{matrix}}$

## Page 35

```markdown
# GW 4. R(A B C)

**Left Column:**
* A -> BC
* B -> C
* A -> B
* AB -> C

**Decomposition**
* A $\rightarrow$ B $\checkmark$  $A^+ = \{A, B, C\}$
* A $\rightarrow$ C X  Ignore A $\rightarrow$ B
* B $\rightarrow$ C  $A^+ = \{A, C\}$
* A $\rightarrow$ B  $A^+ = \{A, B, C\}$
* AB $\rightarrow$ C  Ignore A $\rightarrow$ C  $A^+ = \{A, B, C\}$

**Middle Column:**
1. A $\rightarrow$ B  $B^+ = \{B, C\}$
2. B $\rightarrow$ C  Ignore B $\rightarrow$ C
3. A $\rightarrow$ B  $B^+ = \{B\}$
4. AB $\rightarrow$ C

$A^+ = \{A, B, C\}$
3. A $\rightarrow$ B Ignore
$A^+ = \{A, B, C\}$

1. A $\rightarrow$ B  $AB^+ = \{ABC\}$
2. B $\rightarrow$ C  Ignore AB $\rightarrow$ C
3. AB $\rightarrow$  $AB^+ = \{A, B, C\}$

**Right Column:**
* A $\rightarrow$ B
* B $\rightarrow$ C
* minimal cover
* (A $\rightarrow$ C) [circled]
```

## Page 36

# WORKS_ON

| F.K. | F.K. | |
| :--- | :--- | :--- |
| Ssn | Pnumber | Hours |
| $\underbrace{\text{             }}$ | $\underbrace{\text{             }}$ | |
| | P.K. | |

***

An attribute of relation schema R is called **a prime attribute of R** if it is a member of some candidate key of R.

An attribute is called nonprime if it is not a prime attribute—that is, if it is not a member of any candidate key.

* Both Ssn and Pnumber are prime attribute
* Hours are non-prime attribute

**Handwritten Notes:**
* $P.K = SSN, Pnumber$
* $\text{SSN} \rightarrow \text{Prime attribute}$
* $\text{Pnumber} \rightarrow \text{Prime attribute}$
* $\text{Work on (SSN, Pnumber, Hours)}$
* $\text{Hours} \rightarrow \text{Non-prime attribute}$

## Page 37

$R(A B C D E F G)$
$\{ AB \quad C.k.1 \implies \{ \text{Non-prime } F, G \}$
$\{ C D E \quad C.k.2$
$A, B, C, D, E \rightarrow \text{Prime attributes}$

**Gateway classes**

## Page 38

# AKTU QUESTION

| Question No. | Question | Year |
| :--- | :--- | :--- |
| **Q.1** | Explain the procedure of calculating of the canonical cover of a given functional dependency with example | AKTU 2021-22 |
| **Q.2** | Find the canonical cover/minimal cover <br> X $\rightarrow$ W <br> WZ $\rightarrow$ XY <br> Y $\rightarrow$ WXZ | AKTU 2022-21 |
| **Q.3** | A set of FDs for the relation R{A, B, C, D, E, F} is AB $\rightarrow$ C, C $\rightarrow$ A, BC $\rightarrow$ D, ACD $\rightarrow$ B, BE $\rightarrow$ C, EC $\rightarrow$ FA, CF $\rightarrow$ BD, D $\rightarrow$ E. Find a minimum cover forth is set of FDs | AKTU 2022-23 |

## Page 39

# AKTU
**B.Tech III-Year** | **5th Semester** | **GW GATEWAY CLASSES**

**CS IT & CS Allied**

## DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-4**

**Today's Target**
* Find candidate key
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 40

# Find the candidate keys

## 1. $R(A\ B\ C\ D)$
$AD$ essential attributes

$A \rightarrow BC$
$AD^+ = \{A, D, B, C\}$
$(Key)^+ = R$

---

## 2. $R(A\ B\ C\ D)$
$ABC \rightarrow D$
$AB \rightarrow D$
$A \rightarrow BD$

$AC^+ = \{A, C, B, D\}$
$C.K. \text{ P.K.}$

---

## 3. $R(A\ B\ C\ D)$
$AB \rightarrow C$
$C \rightarrow BD$
$D \rightarrow A$

$A^+ = \{A\}$
$B^+ = \{B\}$
$C^+ = \{C, B, D, A\} \checkmark$
$D^+ = \{D, A\}$

$C, AB, BD - C.K.$

$\checkmark AB^+ = \{A, B, C, D\}$
$\times AD^+ = \{A, D\}$
$\checkmark BD^+ = \{B, D, A, C\}$

---

## 4. $R(A\ B\ C\ D)$
$B \rightarrow ACD$
$ACD \rightarrow B$

$A^+ = \{A\}$
$\checkmark B^+ = \{B, A, C, D\}$
$C^+ = \{C\}$
$D^+ = \{D\}$

$AC^+ = \{A, C\}$
$AD^+ = \{A, D\}$
$CD^+ = \{C, D\}$

$(ACD)^+ = \{A, C, D, B\}$

$\{B, ACD\} \text{ C.K.}$

## Page 41

# Find the candidate keys

## 5. $R(ABCD)$
**Essential**

$A \rightarrow B$
$B \rightarrow C$
$C \rightarrow A$

$D^+ = \{D\}$
$AD^+ = \{A, D, B, C\}$
$BD^+ = \{B, C, A, D\}$
$CD^+ = \{C, A, B, D\}$

$AD \quad BD \quad CD - C.k.$

---

## 6. $R(ABCD)$
$AB \rightarrow CD$
$D \rightarrow A$

$B^+ = \{B\}$
$AB^+ = \{A, B, C, D\} \checkmark$
$CB^+ = \{C, B\}$
$DB^+ = \{D, A, B, C\} \checkmark$

$AB, DB - C.k.$

---

## 7. $R(ABCDEF)$
$AB \rightarrow C$
$C \rightarrow D$
$B \rightarrow AE$

$(BF)^+ = \{B, F, A, E, C, D\} \checkmark$
$\downarrow$
$C.k.$

---

## 8. $R(ABCD)$
$AB \rightarrow CD$
$C \rightarrow A$
$D \rightarrow B$

$A^+ = \{A\} \times$
$B^+ = \{B\} \times$
$C^+ = \{C, A\} \times$
$D^+ = \{D, B\} \times$

$AB^+ = \{A, B, C, D\} \checkmark$
$AC^+ = \{A, C\} \times$
$AD^+ = \{A, D, B, C\} \checkmark$
$BC^+ = \{B, C, A, D\} \checkmark$
$BD^+ = \{B, D\} \times$
$CD^+ = \{C, D, B, A\} \checkmark$

$\underline{AB, AD, BC, CD}$
$\downarrow$
$C.k.$

## Page 42

# 9. R(A B C D E)
AB $\rightarrow$ CD
D $\rightarrow$ A
BC $\rightarrow$ DE

$B^+ = \{B\}$
$AB^+ = \{A, B, C, D, E\}$
$CB^+ = \{C, B, D, E\}$
$DB^+ = \{D, B, A, C\}$
$EB^+ = \{E, B\}$ $\times$

AB, CB, DB $\checkmark$

---

# 10. R(A B C D E F)
AB $\rightarrow$ C
DC $\rightarrow$ AE
E $\rightarrow$ F

$BD^+ = \{B, D\} \times$
$ABD^+ = \{A, B, D, C, E, F\} \checkmark$
$CBD^+ = \{C, B, D, A, E, F\} \checkmark$
$EBD^+ = \{E, B, D, F\} \times$
$FBD^+ = \{F, B, D\} \times$

$FEBD^+ = \{F, E, B, D\} \times$

ABD, CBD

---

# 11. R(W X Y Z)
Z $\rightarrow$ W
Y $\rightarrow$ XZ
XW $\rightarrow$ Y

$X^+ = \{X\}$
$Y^+ = \{Y, X, Z, W\}$
$W^+ = \{W\}$
$Z^+ = \{Z, W\}$

Y, XW, XZ - C.k.

---

# 12. R(A B C D E)
CE $\rightarrow$ D
D $\rightarrow$ B
C $\rightarrow$ A

$CE^+ = \{C, E, D, B, A\}$
$\downarrow$
C.k. P.k.

$XW^+ = \{X, W, Y, Z\}$
$XZ^+ = \{X, Z, W, Y\}$
$WZ^+ = \{W, Z\}$

## Page 43

# AKTU QUESTION

| Question | Question Text | Year |
| :--- | :--- | :--- |
| Q.1 | ANY candidate key question | AKTU 2018-19<br>AKTU 2019-20<br>AKTU 2021-22 |

**Watermark:** Gateway classes

## Page 44

# AKTU B.Tech III-Year 5th Semester
**GW GATEWAY CLASSES**

**CS IT & CS Allied**

## DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-5**

**Today's Target**
* Candidate key and canonical cover
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 45

# Left Panel

**GW GATEWAY CLASSES**
**Find the candidate key**
$\downarrow \downarrow \downarrow \downarrow \downarrow \downarrow \downarrow \downarrow \downarrow \downarrow \downarrow$
**1 R(A B C D E F G H I J)**

AB -> C
AD -> GH
BD -> EF
A -> I
H -> J

$(ABD)^+ = \{A, B, D, C, G, H, E, F, I, J\}$
$\downarrow$
CK.

---

# Right Panel

**GW GATEWAY CLASSES**
**2 R(A B C D E)**

A -> B
BC -> E
DE -> A

$CD^+ = \{C, D\}$

$ACD^+ = \{A, C, D, B, I, E\} \checkmark$
$BCD^+ = \{B, C, D, E, A\} \checkmark$
$ECD^+ = \{E, C, D, A, B\} \checkmark$

$\underline{ACD, BCD, ECD \text{ C.K.}}$

## Page 46

# Left Panel
**3. R(A B C D E)**

BC -> ADE
D -> B
C$^+$ = { C }
AC$^+$ = { A, C }
BC$^+$ = { B, C, A, D, E } $\checkmark$
DC$^+$ = { D, B, C, A, E } $\checkmark$
EC$^+$ = { E, C }

AC EC $\times$
ACE$^+$ = { A, C, E }

BC, DC
C.K.

---

# Right Panel
**4. R(A B C D E F)**

AB -> C
C -> B
D -> BF
E -> F
F -> A

DE$^+$ = { D, E, B, F, A, C }
C.K.

**Gateway classes**

## Page 47

# Text Extraction

**Top Header:**
5. R(ABCDEFGH) | 6. Find the canonical cover/minimal cover

**Left Section:**
*   CH -> G
*   A -> BC
*   B -> CFH
*   E -> A
*   F -> EG

**Center-Left Section (Calculations):**
*   $D^+ = \{D\}$
*   $AD^+ = \{A, B, C, D, F, H, E, G\}$
*   $BD^+ = \{B, D, C, F, H, E, G, A\}$
*   $CD^+ = \{C, D\} \times$
*   $ED^+ = \{E, D, A, B, C, F, H, G\}$
*   $FD^+ = \{F, D, E, G, A, B, C, H\}$
*   $GD^+ = \{G, D\} \times$
*   $HD^+ = \{H, D\} \times$

$CD, GD, HD$
$CG D^+ = \{C, G, D\} \times$
$CH D^+ = \{C, H, G, D\} \times$
$\checkmark CHGD^+ = \{C, H, G, D\}$

$AD, BD, ED, FD \checkmark$

**Center-Right Section:**
R(ABC)
(AKTU 2018-19)
*   A -> B
*   B -> C
*   A -> C
*   AB -> B
*   AB -> C
*   AC -> B

1. Decomposition
2. Extra functional

$A^+ = \{A, B, C\}$
Ignore A -> B

$A^+ = \{A, B, C\}$
Ignore A -> B

$B^+ = \{B, C\}$
A -> C
Ignore B -> C
$B^+ = \{B, C\}$
$\times A \to B$
$AB \to C$
$A \to B$
$A \to C$

$A^+ = \{A, B, C\}$
Ignore A -> C
$A^+ = \{A\}$

**Right Section:**
$AB^+ = \{A, B, C\}$
Ignore AB -> B

$AB^+ = \{A, B, C\}$
B -> C
A -> C
$AB \to C \times$
$AC \to B$
$AB^+ = \{A, B, C\}$

$AC^+ = \{A, C, B\}$
Ignore AC -> B
$AC^+ = \{A, C\}$

(Boxed area):
B -> C
A -> C
AC -> B

## Page 48

$B \rightarrow C$
$A \rightarrow C$
$AC \rightarrow B$

$AC^+ = \{ A, C, B \}$
$A^+ = \{ A, C, B \}$
$C^+ = \{ C \}$

$\begin{array}{|l|} \hline B \rightarrow C \\ A \rightarrow C \\ A \rightarrow B \\ \hline \end{array}$

$\begin{array}{|l|} \hline B \rightarrow C \\ A \rightarrow BC \\ \hline \end{array} \rightarrow \text{canonical cover}$
$\text{or}$
$\text{Minimal cover.}$

Gateway classes

## Page 49

# Find the canonical cover/minimal cover (AKTU 2017-18)

**R(X Y Z)**

**F = {**
X $\rightarrow$ YZ
Y $\rightarrow$ Z
X $\rightarrow$ Y
XY $\rightarrow$ Z
**}**

**Decomposition**
1. X $\rightarrow$ YX
2. X $\rightarrow$ Z
3. Y $\rightarrow$ Z
4. X $\rightarrow$ Y
5. XY $\rightarrow$ Z

**Steps/Calculations:**
$X^+ = \{X, Y, Z\}$
ignore eq(1) X $\rightarrow$ Y
$X^+ = \{X\}$
$XY^+ = \{X, Y, Z\}$
ignore X $\rightarrow$ Z
$X^+ = \{X, Y, Z\}$

1. X $\rightarrow$ Z $X^+ = \{X, Z, Y\}$
2. Y $\rightarrow$ Z ignore X $\rightarrow$ Z
3. X $\rightarrow$ Y $X^+ = \{X, Z, Y\}$
4. XY $\rightarrow$ Z

1. Y $\rightarrow$ Z $Y^+ = \{Y, Z\}$
2. X $\rightarrow$ Y ignore Y $\rightarrow$ Z
3. XY $\rightarrow$ Z $Y^+ = \{Y\}$

**Canonical Cover or Minimal Cover:**
$\begin{cases} Y \rightarrow Z \\ X \rightarrow Y \end{cases}$

**Rechecking:**
$X^+ = \{X, Y, Z\}$
$Y^+ = \{Y, Z\}$
$Z^+ = \{Z\}$

## Page 50

# Consider another set of functional dependencies:

$F = \{$
$B \rightarrow A$
$AD \rightarrow BC$
$C \rightarrow ABD$
$\}$

$R(A, B, C, D)$

$A^+ = \{A\}$
$B^+ = \{B, A\}$
$C^+ = \{C, A, B, D\}$
$D^+ = \{D\}$

---

### Decomposition
1. $\checkmark B \rightarrow A$
2. $\times \text{ (crossed out) } AD \rightarrow B$
3. $\checkmark AD \rightarrow C$
4. $\checkmark C \rightarrow A$
5. $\checkmark C \rightarrow B$
6. $\checkmark C \rightarrow D$

$B^+ = \{B, A\}$
$\text{Ignore } B \rightarrow A$
$B^+ = \{B\}$

$AD^+ = \{A, D, B, C\}$
2. $\text{Ignore } AD \rightarrow B$
$AD^+ = \{A, D, C, B\}$

$AD^+ = \{A, D, C, B\}$
$\text{Ignore } AD \rightarrow C$
$AD^+ = \{A, D, B\}$

---

$C^+ = \{C, A, B, D\}$
$\text{Ignore } C \rightarrow A$
$C^+ = \{C, B, D, A\}$

$\checkmark B \rightarrow A$
$\checkmark AD \rightarrow C$
$\checkmark C \rightarrow B$
$\checkmark C \rightarrow D$

$C^+ = \{C, B, D, A\}$
$\text{Ignore } C \rightarrow B$
$C^+ = \{C, D\}$

$C^+ = \{C, B, D, A\}$
$\text{Ignore } C \rightarrow D$
$C^+ = \{C, B, A\}$

---

$B \rightarrow A$
$AD \rightarrow C$
$C \rightarrow B$
$C \rightarrow D$

$AD^+ = \{A, D, C, B\}$
$A^+ = \{A\}$
$D^+ = \{D\}$

$B \rightarrow A$
$AD \rightarrow C$
$C \rightarrow B$
$C \rightarrow D$ {canonical cover}

$A^+ = \{A\}$
$B^+ = \{B, A\}$
$C^+ = \{C, B, D, A\}$
$D^+ = \{D\}$

## Page 51

# AKTU
**B.Tech III-Year** | **5th Semester** | **GW (GATEWAY CLASSES)**

**CS IT & CS Allied**

## DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-6**

---

**Today's Target**
* Normalization
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 52

# Normalization

* Normalization in DBMS is the process of organizing data in a database to reduce redundancy and improve data integrity.
* It involves dividing a database into smaller tables and defining relationships between them to ensure data is stored efficiently and logically.

**Need for normalization:**
Normalization is essential to:
* Reduce Data Redundancy: Avoid storing duplicate data to save space.
* Improve Data Integrity: Maintain consistency across the database by eliminating anomalies.
* Simplify Maintenance: Make updates, deletions, and insertions error-free.

## Page 53

# Employee

| Emp_ID | Emp_Name | Dept_ID | Dept-name | Dept_location |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Alice | D01 | HR | New York |
| 2 | Bob | D01 | HR | New York |
| 3 | Charlie | D03 | IT | San Francisco |

* **Redundancy:** "HR" and "New York" are repeated for every employee in the same department.
* **Update Anomaly:** Updating the location of "HR" requires multiple changes.
* **Insertion Anomaly:** Cannot add new department without at least one employee.
* **Deletion Anomaly:** Deleting all employees in "HR" removes department info.

## Page 54

# Employee Table
| Emp_ID | Demp_Name | Dept_ID (FK) |
| :--- | :--- | :--- |
| 1 | Alice | D01 |
| 2 | Bob | D01 |
| 3 | Charlie | D02 |

# Department Table
| Dept_ID | Dept_name | Dept_location |
| :--- | :--- | :--- |
| D01 | HR | New York |
| D02 | IT | San Francisco |

## Advantages
* **No Redundancy:** Department info stored once.
* **Easy Updates:** Update "HR" location in one place.
* **No Anomalies:** Adding or deleting info is straightforward.

## Normal Forms
* 1NF
* 2NF
* 3NF $\rightarrow$ Numerical
* BCNF
* 4NF
* 5NF $\rightarrow$ Theory

*(Note: Handwritten annotations include "Employee", "Department", "FK", and "Normal form" with "theoretical" and "numerical" notes)*

## Page 55

# 1 NORMAL FORM (1NF)

It states that the **domain of an attribute must include only atomic** (simple, indivisible) **values** and that the value of any attribute in a tuple must be a single value from the domain of that attribute.

### Not in 1NF

| ID | Name | Subjects |
| :--- | :--- | :--- |
| 1 | Alice | {Math, Science} |

---

### 1NF

| ID | Name | Subjects |
| :--- | :--- | :--- |
| 1 | Alice | Math |
| 1 | Alice | Science |

1NF disallows having a **set of values**, a **tuple of values**, or a **combination of both** as an attribute value for a single tuple. In other words, 1NF disallows relations within relations or relations as attribute values within tuples.

## Page 56

# Relation within Relation, Not 1NF):

| ID | Name | Address |
| :--- | :--- | :--- |
| 1 | Alice | Street: "Main St", City: "NYC" |

**1NF**

| iD | Name | Street | City |
| :--- | :--- | :--- | :--- |
| 1 | Alice | Main St | NYC |

**$\text{>}$ 1NF are single atomic (indivisible) values.**

## Page 57

# Text Extraction

**Top Left Section:**
(a)
DEPARTMENT
Dname | Dnumber | Dmgr_ssn | Dlocations

**Bottom Left Section:**
(b)
DEPARTMENT
| Dname | Dnumber | Dmgr_ssn | Dlocations |
| :--- | :--- | :--- | :--- |
| Research | 5 | 333445555 | {Bellaire, Sugarland, Houston} |
| Administration | 4 | 987654321 | {Stafford} |
| Headquarters | 1 | 888665555 | {Houston} |

This violates the 1NF

**Right Section:**
There are three main techniques to achieve first normal form for such a relation:

1. Remove the attribute Dlocations that violates 1NF and place it in a separate relation DEPT_LOCATIONS along with the primary key Dnumber of DEPARTMENT

## Page 58

# Left Panel

**DEPARTMENT**

| Dname | Dnumber | Dmgr_ssn |
| :--- | :--- | :--- |
| Research | 5 | 333445555 |
| Administration | 4 | 987654321 |
| Headquarters | 1 | 888665555 |

**DEPT_LOCATIONS**

| Dnumber | Dlocation |
| :--- | :--- |
| 1 | Houston |
| 4 | Stafford |
| 5 | Bellaire |
| 5 | Sugarland |
| 5 | Houston |

***

# Right Panel

2. Expand the key so that there will be separate tuple in the original DEPARTMENT relation for each location of a DEPARTMENT.

**DEPARTMENT**

| Dname | Dnumber | Dmgr_ssn | Dlocation |
| :--- | :--- | :--- | :--- |
| Research | 5 | 333445555 | Bellaire |
| Research | 5 | 333445555 | Sugarland |
| Research | 5 | 333445555 | Houston |
| Administration | 4 | 987654321 | Stafford |
| Headquarters | 1 | 888665555 | Houston |

This solution has the disadvantage of introducing redundancy in the relation and hence is rarely adopted.

## Page 59

# Text Extraction

**3. If a maximum number of values is known for the attribute—for example, if it is known that at most three locations can exist for a department—replace the Dlocations attribute by three atomic attributes: Dlocation1, Dlocation2, and Dlocation3**

| DNAME | DNUMBER | DMGR_SSN | Dlocation1 | DLOCATIO N2 | Dloac tion3 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Research | 5 | 33344555 | Bellaire | SUGARLAN D | HOUSTON |
| Administration | 4 | 987654321 | STAFFORD | NULL | NULL |
| Headquarter | 1 | 888665555 | HOUSTON | NULL | NULL |

This solution has the **disadvantage of introducing NULL values if most departments have fewer than three locations.**

## Page 60

# NOTE:

* Of the three solutions above, the first is generally considered best because it does not suffer from redundancy and it is completely general.
* It places no maximum limit on the number of values. In fact, if we choose the second solution,
* It will be decomposed further during subsequent normalization steps into the first solution.

First normal form also disallows multivalued attributes that are themselves composite. These are called nested relations because each tuple can have a relation within it.
EMP_PROJ(Ssn, Ename, {PROJS(Pnumber, Hours)})

(a)
EMP_PROJ
| Projs |
| :--- | :--- | :--- | :--- |
| Ssn | Ename | Pnumber | Hours |

## Page 61

**(b)**
**EMP_PROJ**

| Ssn | Ename | Pnumber | Hours |
| :--- | :--- | :--- | :--- |
| 123456789 | Smith, John B. | 1 | 32.5 |
| | | 2 | 7.5 |
| 666884444 | Narayan, Ramesh K. | 3 | 40.0 |
| 453453453 | English, Joyce A. | 1 | 20.0 |
| | | 2 | 20.0 |
| 333445555 | Wong, Franklin T. | 2 | 10.0 |
| | | 3 | 10.0 |
| | | 10 | 10.0 |
| | | 20 | 10.0 |
| | | 30 | 10.0 |
| 999887777 | Zelaya, Alicia J. | 10 | 10.0 |
| 987987987 | Jabbar, Ahmad V. | 10 | 35.0 |
| | | 30 | 5.0 |
| 987654321 | Wallace, Jennifer S. | 30 | 20.0 |
| | | 20 | 15.0 |
| 888665555 | Borg, James E. | 20 | NULL |

---

**EMP_PROJ2**
| Ssn | Pnumber | Hours |
| :--- | :--- | :--- |

**Note:**
* Every relation is in 1NF.
* This is because formal definition of a relation states that value of all the attributes must be atomic.

---

**(c)**
**EMP_PROJ1**
| Ssn | Ename |
| :--- | :--- |

## Page 62

# Question 1: Check whether it is in 1NF

**CANDIDATE (Ssn, Name, {JOB_HIST (Company, Highest_position, {SAL_HIST (Year, Max_sal)}}})**

internal partial keys Company and Year

CANDIDATE (SSN, Name)
CANDIDATE_Jobhist (SSN, Company, Highest_position)
CANDIDATE-Jobhist_Salhist (SSN, Company, Year, Max_sal)

<u>1NF</u>

## Page 63

# 2 NF (2 NORMAL FORM)

A given relation is called in Second Normal Form (2NF) if and only if-

1. Relation already exists in 1NF.
2. No partial dependency exists in the relation.

### Partial Dependency
A partial dependency is a dependency where a portion of the candidate key or incomplete candidate key determines non-prime attribute(s).

---

$A \rightarrow B$ is called a partial dependency if and only if-

* A is a subset of some candidate key
* B is a non-prime attribute.

If any one condition fails, then it will not be a partial dependency.

$R(A\ B\ C\ D)$
$AB \rightarrow D$
$B \rightarrow C$ X

$(AB)^+ = \{A, B, D, C\}$
$\downarrow$
CK

Prime attribute $= \{A, B\}$
Non-prime attribute $= \{C, D\}$

INF
$\downarrow$
$\text{2NFX}$

$R_1(ABD) \quad AB \rightarrow D$
$R_2(BC) \quad B \rightarrow C$

## Page 64

$\alpha \rightarrow \beta$

$(ABC)^+$

$R(ABCDE)$
Prime - $ABC$
Non-prime $DE$

$ABC \rightarrow D \checkmark 2NF \checkmark$
$B \rightarrow E \quad 2NF \times$
$B \rightarrow C \rightarrow 2NF$
$A \rightarrow C \rightarrow 2NF$

Gateway classes

$R_1(ABCD) \quad ABC \rightarrow D$
$\quad \quad \quad \quad \quad \quad B \rightarrow C$
$\quad \quad \quad \quad \quad \quad A \rightarrow C$

$R_2(BE) \quad B \rightarrow E$

## Page 65

# AKTU QUESTIONS

| Question | Year |
| :--- | :--- |
| Define Normal form. Explain 1Nf, 2 NF <br> OR <br> Any numerical to check whether table in 2NF | AKTU 2016-17 <br> AKTU 2017-18 <br> AKTU 2020-21 <br> AKTU 2019-20 |

## Page 66

# AKTU
**B.Tech III-Year** | **5th Semester** | **GW GATEWAY CLASSES**

## CS IT & CS Allied
# DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-7**

---

**Today's Target**
* 2NF NUMERICALS
* 3NF AND BCNF
* AKTU PYQs

---

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 67

# 2NF

**(a)**
**EMP_PROJ**

| Ssn | Pnumber | Hours | Ename | Pname | Plocation |
| :--- | :--- | :--- | :--- | :--- | :--- |

*   **FD1** $\rightarrow$ (points to Hours)
*   **FD2** $\rightarrow$ (points to Ename)
*   **FD3** $\rightarrow$ (points to Pname, Plocation)

**Functional Dependencies:**
1. $\checkmark$ $\{ \text{SSN, Pnumber} \} \rightarrow \text{Hours}$
2. $\times$ $\{ \text{SSN} \} \rightarrow \{ \text{Ename} \}$
3. $\checkmark$ $\{ \text{Pnumber} \} \rightarrow \{ \text{Pname, Plocation} \}$

**Notes:**
*   Non-prime attribute $\{ \text{Hours, Ename, Pname, Plocation} \}$
*   $\text{SSN, Pnumber}$ PK, CK
*   Prime attribute $\rightarrow \text{SSN, Pnumber}$
*   1NF

---

**Decomposition:**

**EP1**
| Ssn | Pnumber | Hours |
| :--- | :--- | :--- |
*   **FD1** $\rightarrow$ (points to Hours)

**EP2**
| Ssn | Ename |
| :--- | :--- |
*   **FD2** $\rightarrow$ (points to Ename)

**EP3**
| Pnumber | Pname | Plocation |
| :--- | :--- | :--- |
*   **FD3** $\rightarrow$ (points to Pname, Plocation)

## Page 68

# Left Panel

**1. R(A B C D E)**

AB $\rightarrow$ C
D $\rightarrow$ E

**CHECK whether it is 2 NF if not convert it into.**

$(ABD)^+ = \{A, B, D, C, E\}$ $\text{C.K}$

$\text{1NF} \checkmark$
$\text{Prime attribute} = \{A, B, D\}$
$\text{2NF}$
$\text{Non-prime attribute} = \{C, E\}$

$AB \rightarrow C$ (partial dependency)
$D \rightarrow E$ (partial dependency)

$\text{2 NF}$
$R_1(ABD)$
$R_2(ABC) \quad AB \rightarrow C$
$R_3(DE) \quad D \rightarrow E$

**NOTE**
$P \rightarrow NP \rightarrow$
$NP \rightarrow NP \rightarrow \text{Not}$
$\text{Only concern}$
$(\text{ch 2 NF})$

---

# Right Panel

**2. R(A B C D E)**

A $\rightarrow$ B
B $\rightarrow$ E
C $\rightarrow$ D

**CHECK whether it is 2 NF if not convert it into**

$(AC)^+ = \{A, B, E, C, D\}$
$\text{CK}$

$\text{Prime attribute} = \{A, C\}$
$\text{Non-prime attribute} = \{B, D, E\}$

$\text{1NF} \checkmark \text{ Every relation is in 1NF}$

$\text{2NF}$
$A \rightarrow B \rightarrow \text{Partial Depency}$ $\times \text{2NF}$
$B \rightarrow E \rightarrow \text{Non-partial dependency}$
$C \rightarrow D \rightarrow \text{Partial Dependecny}$

$\text{2 NF}$
$R_1(AC)$
$R_2(ABE) \quad A \rightarrow B \quad B \rightarrow E$
$R_3(CD) \quad C \rightarrow D$

## Page 69

# 3. R(A B C D E F G H I J)

**Functional Dependencies:**
* AB $\rightarrow$ C
* AD $\rightarrow$ GH
* BD $\rightarrow$ EF
* A $\rightarrow$ I
* H $\rightarrow$ J

**Closure Calculations:**
* $(ABD)^+ = \{A, B, C, D, G, H, E, F, I, J\}$
* $AB \rightarrow C$ (P.D)
* $AD \rightarrow GH$ (P.D)
* $BD \rightarrow EF$ (P.D)
* $A \rightarrow I$ (PD)
* $H \rightarrow J$ (Not Partial Dependency)

**Questions/Tasks:**
* Find out the Key of a relation.
* Check whether it is in 1NF, 2NF. If not, convert it into...

**Analysis:**
* $(ABD)^+ = \text{all attributes}$ $\rightarrow$ Prime attributes: $\{A, B, D\}$
* Non-prime attributes: $\{C, E, F, G, H, I, J\}$
* 1NF $\checkmark$

**Decomposition:**
* $R_1(ABD)$
* $R_2(ABC)$ $\quad AB \rightarrow C$
* $R_3(ADGHJ)$ $\quad AD \rightarrow GH, H \rightarrow J$
* $R_4(BDEF)$ $\quad BD \rightarrow EF$
* $R_5(AI)$ $\quad A \rightarrow I$

## Page 70

# Third Normal

**Form-**

A given relation is called in Third Normal Form (3NF) if and only if-

* Relation already exists in 2NF. $P \rightarrow NPX$ $NP \rightarrow NP$ $P \rightarrow P \checkmark$
* No transitive $NP \rightarrow NPX$ dependency exists for $P \rightarrow P \checkmark$ non-prime attributes.

**NOTE-**
$\text{SupX} \rightarrow \beta$ (non-prime)

---

# Transitive Dependency

$A \rightarrow B$ is called a transitive dependency if and only if-

* A is not a super key.
* B is a non-prime attribute.

If any one condition fails, then it is not a transitive dependency.

$\text{Prove } 3NF \rightarrow 2NF$
$P \rightarrow NPX$ $P \rightarrow NPX$ (PD)
$NO \rightarrow NPX$ $NP \rightarrow NP \checkmark$
$P \rightarrow P$ $P \rightarrow P \checkmark$

* Transitive dependency must not exist for non-prime attributes.
* However, transitive dependency can exist for prime attributes.

## Page 71

# EMP_DEPT
| Ename | Ssn | Bdate | Address | Dnumber | Dname | Dmgr_ssn |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

*(Handwritten annotations: 1NF ✓, 2NF ✓, X3NF)*

---

### ED1
| Ename | Ssn | Bdate | Address | Dnumber |
| :--- | :--- | :--- | :--- | :--- |

### ED2
| Dnumber | Dname | Dmgr_ssn |
| :--- | :--- | :--- |

---

**Definition.** According to Codd's original definition, a relation schema R is in 3NF if it satisfies 2NF and no nonprime attribute of R is transitively dependent on the primary key.

## Page 72

# SUMMARY

| NORMAL FORM | TEST | REMEDY |
| :--- | :--- | :--- |
| **First (1NF)** | Relation should have no multivalued attributes or nested relations | Form new relations for each multivalued attribute or nested relation. |
| **Second (2NF)** | For relations where primary key contains multiple attributes, no non key attribute should be functionally dependent on a part of the primary key | Decompose and set up a new relation for each partial key with its dependent attribute(s).<br><br>Make sure to keep a relation with the original primary key and any attributes that are fully functionally dependent on it |

## Page 73

# SUMMARY

| NORMAL FORM | TEST | REMEDY |
| :--- | :--- | :--- |
| **THIRD (3NF)** | Relation should not have a non key attribute functionally determined by another non-key attribute (or by a set of non-key attributes). That is, there should be no transitive dependency of a non-key attribute on the primary key. | Decompose and set up a relation that includes the non-key attribute(s) that functionally determine(s) other non-key attribute(s)non-key attribute(s) |

## Page 74

# 1. R(A B C)

A -> B
B -> C

CHECK whether it is 3 NF if not convert it into

$A^+ = \{A, B, C\}$ C.K
Prime attribute = $\{A\}$
Non-prime attribute = $\{B, C\}$
$RC_{A,B,C}$

A $\rightarrow$ B (No P.D) $\quad$ 1NF $\checkmark$
B $\rightarrow$ C (No P.D) $\quad$ 2NF $\checkmark$
$\quad \quad \quad \quad \quad \quad$ 3NF

A $\rightarrow$ B (No transitive dependency)
B $\rightarrow$ C (transitive dependency)

$R_1(A B) \quad A \rightarrow B$
$R_2(B C) \quad B \rightarrow C \quad (3NF)$

---

# 2. R(A B C D E)

A -> B
B -> E $\quad (AC)^+ = \{A, B, E, C, D\}$
C -> D $\quad$ C.K

Prime attribute = $\{A, C\}$
Non-prime attribute = $\{B, D, E\}$

Check whether it is 3rd normal form or not if not convert it

A $\rightarrow$ B (Partial Dependency) $\quad$ 1NF $\checkmark$
B $\rightarrow$ E (No P.D) $\quad \quad \quad \quad \quad \quad$ 2NF
C $\rightarrow$ D (No P.D)

$R_1(A C) \quad 3NF$
$R_{21}(A B) \quad A \rightarrow B$
$R_{22}(B E) \quad B \rightarrow E$
$R_3(C D) \quad C \rightarrow D$

$R_1(A C)$
$R_2(A B E) \quad A \rightarrow B, B \rightarrow E$
$R_3(C D) \quad C \rightarrow D$
$\quad \quad \quad \quad \quad 2NF$

## Page 75

# 3. R(A B C D E F G H I J)

**Functional Dependencies:**
* AB $\rightarrow$ C
* A $\rightarrow$ DE
* B $\rightarrow$ F
* F $\rightarrow$ GH
* D $\rightarrow$ IJ

**Candidate Key (C.K.):**
$(AB)^+ = \{A, B, C, D, E, F, G, H, I, J\}$

**Prime attribute** = $\{A, B\}$
**Non-prime attribute** = $\{C, D, E, F, G, H, I, J\}$

**1NF** $\rightarrow$ Every Relation is in 1NF

---

### 2NF
* AB $\rightarrow$ C { No PD }
* A $\rightarrow$ DE { PD }
* B $\rightarrow$ F { PD }
* F $\rightarrow$ GH { No PD }
* D $\rightarrow$ IJ { No PD }

**Decomposition:**
* $R_1(ABC)$ AB $\rightarrow$ C
* $R_2(ADEIJ)$ A $\rightarrow$ DE, D $\rightarrow$ IJ
* $R_3(BFGH)$ B $\rightarrow$ F, F $\rightarrow$ GH

---

### 3NF
* $R_1(ABC)$ AB $\rightarrow$ C
* $R_{21}(ADE)$ A $\rightarrow$ DE
* $R_{22}(DIJ)$ D $\rightarrow$ IJ
* $R_3(BF)$ B $\rightarrow$ F
* $R_{32}(EGH)$ F $\rightarrow$ GH

## Page 76

# 4. R(A B C D E)

**AB $\rightarrow$ C**
**B $\rightarrow$ D**
**D $\rightarrow$ E**

$(AB)^+ = \{A, B, C, D, E\}$
$\text{C.K. P.K}$

**Check whether it is $3^{\text{rd}}$ normal form or not if not convert it**

$\text{Prime attribute} = \{A, B\}$
$\text{Non-prime attribute} = \{C, D, E\}$
$1\text{NF} \rightarrow \text{Every Relation is in 1NF}$

---

$2\text{NF}$

$\text{AB} \rightarrow \text{C } \{\text{No P.D}\}$
$\text{B} \rightarrow \text{D } \{\text{P.D}\}$
$\text{D} \rightarrow \text{E } \{\text{No P.D}\}$

$R_1(\underline{\text{ABC}}) \quad \text{AB} \rightarrow \text{C}$
$R_2(\underline{\text{BDE}}) \quad \text{B} \rightarrow \text{D, D} \rightarrow \text{E}$ $\rightarrow 2\text{NF}$ (transitive dependency)

$R_1(\underline{\text{ABC}}) \quad \text{AB} \rightarrow \text{C} \checkmark$
$R_{21}(\underline{\text{BD}}) \quad \text{B} \rightarrow \text{D} \checkmark$
$R_{22}(\underline{\text{DE}}) \quad \text{D} \rightarrow \text{E} \checkmark$

## Page 77

# Database Normalization Notes

**5. R(A, B, C, D, E, F, G, H, I, J)**

**Functional Dependencies:**
* AB $\rightarrow$ C (PD)
* AD $\rightarrow$ GH (PD)
* BD $\rightarrow$ EF (PD)
* A $\rightarrow$ I (PD)
* H $\rightarrow$ J (No PD)

**Closures & Attributes:**
* $(ABD)^+ = \{A, B, C, D, GH, EF, J, I\}$
* Prime = $\{A, B, D\}$
* Non-prime = $\{C, E, F, G, H, I, J\}$

**Normalization Check:**
* 3NF $\checkmark$
* INF $\checkmark$

**Check whether it is 3rd normal form or not if not convert it**
* $\text{2NF}$

**Decomposition:**
* $R_1(ABD)$
* $R_2(ABC) \quad AB \rightarrow C$
* $R_3(ADGHJ) \quad AD \rightarrow GH, H \rightarrow J$
* $R_4(AI) \quad A \rightarrow I$
* $R_5(BDEF) \quad BD \rightarrow EF$

---
**Right Side Notes:**
* $\times$ No Transitive dependency
* (2NF)
* $R_1(ABD)$
* $R_2(ABC) \quad AB \rightarrow C$
* $R_3(ADGH) \quad AD \rightarrow GH$
* $R_{32}(HJ) \quad H \rightarrow J$
* $R_4(AI) \quad A \rightarrow I$
* $R_5(BDEF) \quad BD \rightarrow EF$

## Page 78

# Boyce-Codd Normal Form-

A given relation is called in BCNF if and only if-

* Relation already exists in 3NF.
* For each non-trivial functional dependency A $\rightarrow$ B, A is a super key of the relation.

---

R( A B C)
AB $\rightarrow$ C
C $\rightarrow$ B

List all prime and non-prime attributes In Relation R(A,B,C,D,E) with FD set F = {AB $\rightarrow$ C, B $\rightarrow$ E, C $\rightarrow$ D}.

## Page 79

| Full Functional Dependency | Partial Functional Dependency |
| :--- | :--- |
| 1. A functional dependency X->Y is a fully functional dependency if Y is functionally dependent on X and Y is not functionally dependent on any proper subset of X. | A functional dependency X->Y is a partial dependency if Y is functionally dependent on X and Y can be determined by any proper subset of X. |
| 2. In full functional dependency, the non-prime attribute is functionally dependent on the candidate key. | In partial functional dependency, the non-prime attribute is functionally dependent on part of a candidate key. |
| 3. In fully functional dependency, if we remove any attribute of X, then the dependency will not exist anymore. | In partial functional dependency, if we remove any attribute of X, then the dependency will still exist. |

## Page 80

| Full Functional Dependency | Partial Functional Dependency |
| :--- | :--- |
| **4.** Full Functional Dependency equates to the normalization standard of Second Normal Form. | Partial Functional Dependency does not equate to the normalization standard of Second Normal Form. Rather, 2NF eliminates the Partial Dependency. |
| **5.** An attribute A is fully functional dependent on another attribute B if it is functionally dependent on that attribute, and not on any part (subset) of it. | An attribute A is partially functional dependent on other attribute B if it is functionally dependent on any part (subset) of that attribute. |

## Page 81

Consider the universal relation R = {A, B, C, D, E, F, G, H, I, J} and the set of functional dependencies F = {{A, B} $\rightarrow$ {C}, {A}$\rightarrow${D, E}, {B}$\rightarrow${F}, {F}$\rightarrow${G, H}, {D}$\rightarrow${I, J} }. What is the key for R?

Decompose R into 2NF and then 3NF relations. (AKTU 2022-23)

## Page 82

# AKTU PYQS

| No. | Question | Year |
| :--- | :--- | :--- |
| 1. | Explain BCNF with example | AKTU 2017-18 |
| 2. | What is second normal form | AKTU 2017-18 |
| 3. | List all prime and non-prime attributes In Relation R(A,B,C,D,E) with FD set F = {AB$\rightarrow$C, B$\rightarrow$E, C$\rightarrow$D}. | AKTU 2023-24 |
| 4. | Consider the universal relation R = {A, B, C, D, E, F, G, H, I, J} and the set of functional dependencies F = {{A, B} $\rightarrow${C}, {A}$\rightarrow${D, E}, {B}$\rightarrow${F}, {F}$\rightarrow${G, H}, {D}$\rightarrow${I, J}}. What is the key for R? Decompose R into 2NF and then 3NF relations. | AKTU 2022-23 |

## Page 83

# AKTU | B.Tech III-Year | 5th Semester | GW (GATEWAY CLASSES)

## CS IT & CS Allied
# DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-8**

**Today's Target**
* Numericals on functional dependency/Normal form
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 84

Based on the image provided, here is the extracted text in markdown format:

***

**Diagram (Concentric Circles):**
* 1NF
* 2NF
* 3NF
* BCNF

**Left Column:**
* 1NF – Multivalued $\times$
* 2NF $\rightarrow$ No partial dependency
* 3NF $\rightarrow$ 2NF + No transitive dependency
* BCNF $\quad$ P/NP $\rightarrow$ P + 3NF + 2NF

**Center-Top:**
* either $\alpha$ is Sk or $\beta$ is prime

**Center-Middle (Functional Dependencies):**
* $P \rightarrow NP \checkmark$
* $NP \rightarrow NP$

**Center-Diagrams:**
* $\alpha \rightarrow \beta$ (Prime)
    * $\alpha$ is Sk $\rightarrow$ 3NF
    * $\beta$ is P
* $P \rightarrow NP \times$
* $NP \rightarrow NP \times$
* $P+NP \rightarrow P \times$
* $\alpha \rightarrow \beta$ (BCNF)
    * $\alpha$ is Sk

**Right Column:**
* $P \rightarrow NP$
* $NP \rightarrow NP$
* 3NF
* 2NF + No trans...

**Watermark:**
* Gateway classes

## Page 85

# Given functional dependency it satisfies which normal form

## 1. R(A B C D E F G H)
*   AB $\rightarrow$ C  $(AB)^+ = \{A, B, C, D, E, F, G, H\}$
*   A $\rightarrow$ DE
*   B $\rightarrow$ F
*   F $\rightarrow$ GH

**Prime attribute:** $\{A, B\}$
**Non-prime:** $\{C, D, E, F, G, H\}$

*   BCNF: $\alpha \rightarrow \beta$ $\times$
*   3NF: $\alpha \rightarrow \beta$ $\checkmark$
*   2NF: $\times$ (P $\rightarrow$ NP)
*   1NF: $\checkmark$

---

## 2. R(A B C D E)
*   CE $\rightarrow$ D  $(CE)^+ = \{C, E, D, B, A\}$
*   D $\rightarrow$ B
*   C $\rightarrow$ A

**Prime attribute:** $\{C, E\}$
**Non-prime:** $\{A, B, D\}$

*   BCNF: $\alpha \rightarrow \beta$ $\times$
*   3NF: $\alpha \rightarrow \beta$ $\times$
*   2NF: $\times$ (No partial dependency, C $\rightarrow$ A $\times$)
*   1NF: $\checkmark$

---

## 3. R(A B C D E F)
*   AB $\rightarrow$ C  $(BD)^+ = \{B, D\}$
*   AC $\rightarrow$ AE
*   E $\rightarrow$ F

$(ABD)^+$
**Prime:** $\{A, B, D\}$
**Non-prime:** $\{C, E, F\}$

$CEBD^+ \{C, E, B, D, F\}$
$CFBD^+ \{F, B, D\}$

*   BCNF: $\alpha \rightarrow \beta$ $\times$
*   3NF: $\alpha \rightarrow \beta$ $\checkmark$
*   2NF $\rightarrow$ 1NF + No partial
*   1NF $\rightarrow$ $\checkmark$

## Page 86

# Given functional dependency it satisfies which normal form

---

### 4. R(A B C D E G H I)
*   AB $\rightarrow$ C
*   BD $\rightarrow$ EF
*   AD $\rightarrow$ GH
*   A $\rightarrow$ I

$(ABD)^+ = \{A, B, C, E, F, D, G, H, I\}$
$Pr_{me} = \{A, B, D\}$
$Non\text{-}pr_{me} = \{C, E, F, G, H, I\}$

$\alpha \rightarrow \beta$ BCNF $\times$
$\downarrow$
3NF $\rightarrow \beta$
$\downarrow$
S.t. $Pr_{nn}$
$\downarrow$
2NF $\rightarrow P \rightarrow NPX$
$\downarrow$
1NF $\checkmark$

---

### 5. R(A B C D E)
*   AB $\rightarrow$ CD
*   D $\rightarrow$ A
*   BC $\rightarrow$ DE

$AB^+ = \{A, B, C, D, E\}$
$CB^+ = \{C, B, D, E, A\}$
$DB^+ = \{D, B, A, C, E\}$
$EB^+ = \{E, B\}$

$Pr_{me} = \{A, B, C\}$
$Nm\text{-}pr_{me} = \{E\}$

$\alpha \rightarrow \beta$ BCNF $\times$
$\downarrow$
3NF $\checkmark$
$\downarrow$
S.t. $Pr_{me}$

---

### 6. R(A B C D E) (3NF)
*   BC $\rightarrow$ ADE
*   D $\rightarrow$ BC

$C^+ = \{C\}$
$A^+ = \{A, C\}$
$BC^+ = \{B, C, A, D, E\}$
$D^+ = \{D, C, B, A, D, E\}$
$E^+ = \{E\}$

$Pr_{me} = \{B, D, C\}$
$Nm\text{-}pr_{me} = \{A, E\}$

$\alpha \rightarrow \beta$ BCNF $\times$
$\downarrow$
3NF $\checkmark$
$\downarrow$
S.t. $\beta$ $Pr_{nn}$

---

### 7. R(V, W X Y Z)
*   X $\rightarrow$ YV
*   Y $\rightarrow$ Z
*   Z $\rightarrow$ Y
*   VW $\rightarrow$ Y

$WX = \{W, X, Y, V, Z\}$
$Pr_{me} = \{W\}$
$Nm\text{-}pr_{me} = \{V, Y, Z\}$

$\alpha \rightarrow \beta$ BCNF $\times$
$\downarrow$
S.t.
$\downarrow$
3NF $\alpha \rightarrow \beta$
$\downarrow$
S.t. $Pr_{nn}$
$\downarrow$
2NF $\checkmark \rightarrow P \rightarrow NP$
$\downarrow$
1NF $\checkmark$

## Page 87

# Given functional dependency it satisfies which normal form

## 8. R(A B C D E F)
*   ABC $\rightarrow$ D
*   ABD $\rightarrow$ E
*   CD $\rightarrow$ F
*   CDF $\rightarrow$ B
*   BF $\rightarrow$ D

**Analysis:**
*   $(BAC)^+ = \{A, B, C, D, E, F\}$
*   $(DAC)^+ = \{A, C, D, F, B, E\}$
*   $(EAC)^+ = \{E, A, C\}$ $\times$
*   $(FAC)^+ = \{F, A, C\}$
*   $(EFAC)^+ = \{E, F, A, C\}$
*   $(BAC, DAC) \rightarrow$ Ck
*   $P_{rme} = \{A, B, C, D\}$
*   $Not = \{P, E, F\}$
*   BCNF $\nrightarrow$ B
*   3NF $\nrightarrow$ B
*   $\text{INFEL}$
*   $\text{INF } P \rightarrow NP \times$

---

## 9. R(A B C)
*   A $\rightarrow$ B
*   B $\rightarrow$ C
*   C $\rightarrow$ A

**Analysis:**
*   $A^+ = \{A, B, C\}$
*   $B^+ = \{B, C, A\}$
*   $C^+ = \{C, A, B\}$
*   $\alpha \rightarrow \beta$
*   Sk.
*   BCNF $\checkmark$

---

## 10. R(A B C D E F)
*   A $\rightarrow$ BCDEF
*   BC $\rightarrow$ ADEF
*   DEF $\rightarrow$ ABC

**Analysis:**
*   A
*   BC Ck.
*   DEF
*   $\alpha \rightarrow \beta$
*   BCNF $\checkmark$

---

## 11. R(A B C)
*   AB $\rightarrow$ C
*   C $\rightarrow$ A

**Analysis:**
*   $AB = \{A, B, C\}$
*   $C B = \{C, B, A\}$
*   $P_{rme} = \{A, B, C\}$
*   $\alpha \rightarrow \beta \times$ BCNF
*   Sk.
*   $\alpha \rightarrow \beta$ 3NF
*   S.k. $P_{rme}$

---

## 12. R(A B C D E)
*   A $\rightarrow$ B
*   BS $\rightarrow$ E
*   DE $\rightarrow$ A

**Analysis:**
*   $(ACD)^+ = \{A, B, C, D, E\}$
*   $(BCD)^+ = \{B, C, D, E, A\}$
*   $ECD = \{E, C, D\}$
*   $(ACD, BCD)$ Ck.
*   $\alpha \rightarrow \beta$ BCNF $\times$
*   Sk.
*   $\alpha \rightarrow \beta$ 3NF $\times$
*   OK $P_{rme}$
*   $P \rightarrow NP$ 2NF $\checkmark$
*   1NF

## Page 88

# Given functional dependency it satisfies which normal form

## 1. R(A B C D E)
AB -> CD
D -> A
BC -> DE

$A B^+ = \{A, B, C, D, E\}$
$C B^+ = \{B, C, D, E, A\}$
$D B^+ = \{D, A, B, C, E\}$
$E B^+ = \{E, B\}$

$\text{Pmi} = \{A, B, C, D\}$ $\text{3NF} \checkmark$
$\text{Nm-pmi} = \{E\}$ $\alpha \rightarrow \beta$
$\text{BCNF} \alpha \rightarrow \beta \times$
$\text{Sk}$
$\text{Y, } X W_1 X \frac{Z}{CK}$
$\text{CK}$

## 2. R(W X Y Z)
Z -> W
Y -> XZ
XW -> Y

$\text{Sk}$
$\alpha \rightarrow \beta \text{ BCNF}$
$\alpha \rightarrow \beta$
$\text{Sk}$
$\text{Pmi 3NF} \checkmark$

$X W^+ = \{X, W, Y, Z\}$
$X Z^+ = \{X, Z, W, Y\}$
$\lambda W Z^+ = \{W, Z\}$

## 3. R(A B C D E)
A -> B
B -> E
C -> D

$(A C)^+ = \{A, B, C, D, E\}$
$\text{Prime}: \{A, C\}$
$\text{Nm-pmi}: \{B, D, E\}$

$\alpha \rightarrow \beta \text{ BCNF } \times$
$\text{Sk}$
$\alpha \rightarrow \beta \text{ 3NF } \times$
$\text{Prime}$
$2\text{NF } P \rightarrow \text{NPX } \text{INF}$

## 4. R(A B C D E F)
AB -> C
DC -> AE
E -> F

## 5. R(V W X Y Z)
Z -> Y
Y -> Z
Y -> YV
VW -> X

## 6. R(A B C D E F)
ABC -> D
ABD -> E
CD -> F
CDF -> B
BF -> D

## Page 89

Given functional dependency it satisfies which normal form

**1. R(A B C D E F)**
C -> F
E -> A
EC -> D
A -> B

**2. R(A B C D E H)**
A -> B
BC -> D
E -> C
D -> A

**3. R(A B C D E P G)**
AB -> CD
DE -> P
C -> E
P -> C
B -> G

**4. R(A B C D E F G H)**
CH -> G
A -> BC
B -> CFH
E -> A
F -> EG

## Page 90

# Given functional dependency it satisfies which normal form

## 5 R(A B C D)
A->B
B->C
C->BD

## 6. R(A B C D E F)
AB->CD
CD->EF
BC->DEF
D->B
CE->F

## Page 91

| Full Functional Dependency | Partial Functional Dependency |
| :--- | :--- |
| 1. A functional dependency X->Y is a fully functional dependency if Y is functionally dependent on X and Y is not functionally dependent on any proper subset of X. | A functional dependency X->Y is a partial dependency if Y is functionally dependent on X and Y can be determined by any proper subset of X. |
| 2. In full functional dependency, the non-prime attribute is functionally dependent on the candidate key. | In partial functional dependency, the non-prime attribute is functionally dependent on part of a candidate key. |
| 3. In fully functional dependency, if we remove any attribute of X, then the dependency will not exist anymore. | In partial functional dependency, if we remove any attribute of X, then the dependency will still exist. |

## Page 92

| Full Functional Dependency | Partial Functional Dependency |
| :--- | :--- |
| **4.** Full Functional Dependency equates to the normalization standard of Second Normal Form. | Partial Functional Dependency does not equate to the normalization standard of Second Normal Form. Rather, 2NF eliminates the Partial Dependency. |
| **5.** An attribute A is fully functional dependent on another attribute B if it is functionally dependent on that attribute, and not on any part (subset) of it. | An attribute A is partially functional dependent on other attribute B if it is functionally dependent on any part (subset) of that attribute. |

## Page 93

# AKTU B.Tech III-Year 5th Semester

**GW GATEWAY CLASSES**

**CS IT & CS Allied**

## DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-9**

**Today's Target**
* $\text{>}$ 4 normal form
* $\text{>}$ Lossless decomposition
* $\text{>}$ AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 94

# Fourth normal form (4NF)

$\text{GW}$ GATEWAY CLASSES

* A relation will be in 4NF if it is in Boyce Codd normal form and has no multi-valued dependency.

**Condition 1:(MULTIVALUED DEPENDENCY)**
For a dependency $\text{A} \rightarrow\rightarrow \text{B}$, if for a single value of $\text{A}$, multiple values of $\text{B}$ exists, then the relation will be a multi-valued dependency.

**Condition 2:**
A table should have at least 3 column(a,b,c) to have multi value dependency.

**Condition 3:**
For a table with column $\text{A} \rightarrow\rightarrow \text{B}$ is a multivalued dependency then b and c should independent of each other.

$\text{GW}$ GATEWAY CLASSES

## Page 95

# Left Panel

**EMP**

| Ename | Pname | Dname |
| :--- | :--- | :--- |
| Smith | X | John |
| Smith | Y | Anna |
| Smith | X | Anna |
| Smith | Y | John |

The EMP relation with two MVDs: Ename $\twoheadrightarrow$ Pname and Ename $\twoheadrightarrow$ Dname.

---

# Right Panel

**EMP_PROJECTS**

| Ename | Pname |
| :--- | :--- |
| Smith | X |
| Smith | Y |

**EMP_DEPENDENTS**

| Ename | Dname |
| :--- | :--- |
| Smith | John |
| Smith | Anna |

Decomposing the EMP relation into two 4NF relations EMP_PROJECTS and EMP_DEPENDENTS

## Page 96

An MVD $X \twoheadrightarrow Y$ in R is called a trivial MVD if (a) Y is a subset of X, or (b) $X \cup Y = R$

$\blacktriangleright$ The relation EMP_PROJECTS has the trivial MVD Ename $\twoheadrightarrow$ Pname and the relation EMP_DEPENDENTS has the trivial MVD Ename $\twoheadrightarrow$ Dname.

$\blacktriangleright$ An MVD that satisfies neither (a) nor (b) is called a nontrivial MVD. A trivial MVD will hold in any relation state r of R; it is called trivial because it does not specify any significant or meaningful constraint on R.

## Page 97

# Lossless decomposition /non-

**additive**

* This property gurantees that the extra or loss tuplern problem does occur afte rdecomposition.
* It is mandatory that this property always hold good.
* If a realtion R is decomposed into realtion r1 and r2 then it is lossless if and only if
    1. $\text{att}(r1) \cup \text{attr}(r2) = \text{attr}(R)$
    2. $\text{att}(r1) \cap \text{attr}(r2) \text{ not equal to } \emptyset$

---

**Handwritten/Diagram Section:**

$\text{att}(r1) \cap \text{attr}(r2) \rightarrow \text{att}(r1)/\text{attr}(r2)$

**R**
| A | B | C | D |
|---|---|---|---|
| 1 | a | p | x |
| 2 | b | q | y |

(Arrows pointing from R to two smaller tables)

**r1**
| A | B |
|---|---|
| 1 | a |
| 2 | b |

**r2**
| C |
|---|
| p |
| q |

$\gamma_1(AB) \cup \gamma_2(C) = R$
$ABC \neq ABCD$

## Page 98

Based on the image provided, here is the extracted text in markdown format:

**Tables:**

**$\gamma_1$**
| A | B |
|---|---|
| 1 | a |
| 2 | b |

**$\gamma_2$**
| C | D |
|---|---|
| p | x |
| q | y |

**$\gamma_1 \times \gamma_2$**
| A | B | C | D |
|---|---|---|---|
| 1 | a | p | x |
| 1 | a | q | y |
| 2 | b | p | x |
| 2 | b | q | y |

*(Note: There are handwritten marks and a note saying "Extra tuple" next to the final table)*

**Equations and Notes:**

$\{AB\} \cap \{C, D\} = \emptyset$

$\text{Gateway Classes}$ (written diagonally)

1. $attr(r_1) \cup attr(r_2) = attr(R)$
   $\{AB\} \cup \{CD\} = R(ABCD)$
   $ABCD = ABCD$

$attr(r_1) \cap attr(r_2) \neq \emptyset$

## Page 99

Based on the image provided, here is the extracted text in markdown format:

# Left Side

**R**
**C.K.** (pointing to column B)

| A | B | C |
|---|---|---|
| 1 | a | p |
| 2 | b | q |
| 3 | a | r |

**r1**
| A | B |
|---|---|
| 1 | a |
| 2 | b |
| 3 | a |

**r2**
| B | C |
|---|---|
| a | p |
| b | q |
| a | r |

$r1 \bowtie r2$

---

# Right Side

| A | B | C |
|---|---|---|
| 1 | a | p |
| 1 | a | r |
| 2 | b | q |
| 3 | a | p |
| 3 | a | r |

$attr(r1) \cap attr(r2) \rightarrow attr(r1), attr(r2)$
$B \rightarrow attr(r1)$

**Watermark:** Gateway Classes

## Page 100

# Gateway Classes

## Table
| A | B | C | D | E |
|---|---|---|---|---|
| a | 12 | 1 | P | W |
| b | 234 | 2 | Q | X |
| C | 568 | 1 | R | Y |
| d | 68 | 3 | S | Z |

---

## Which of the following are lossless decomposition (AKTU 2014-15/2016-17)

1. R1(AB) R2(CD)
2. R1(ABC) R2(DE)
3. R1(ABC) R2(CDE)
4. R1(ABCD) R2(CDE)
5. R1(ABCD) R2(DE)
6. R1(ABC) R2(BCD) R3(DE)

---

## Handwritten Notes/Solutions

**Section 1 (Left/Center):**
* $\text{R} = \text{ABCDE}$
* $\text{R}_1(\text{AB}) \text{ R}_2(\text{CD})$
* $\text{Cmd}^n \text{ attr}(\text{R}_1) \cup \text{attr}(\text{R}_2) = \text{R}$
* $\{\text{A, B}\} \cup \{\text{C, D}\} = \text{ABCD} \neq \text{ABCDE}$
* $\text{ABCD} \neq \text{ABCDE}$
* $\{\text{AB}\} \cap \{\text{CD}\} = \emptyset$
* $\phi$
* $\text{Lossy decomposition}$

**Section 2 (Center):**
* $\text{R}_1(\text{ABC}) \text{ R}_2(\text{CDE})$
* $\text{ABC} \cup \text{CDE} = \text{R}$
* $\{\text{ABCDE}\} = \text{R}$
* $\text{ABC} \cap \text{CDE} \neq \emptyset$
* $\{\text{C}\}$
* $\text{C is not ck as it contain duplicate value Lossy}$

**Section 3 (Right):**
* $\text{R}_1(\text{ABCD}) \text{ R}_2(\text{CDE})$
* ① $\text{ABCD} \cup \text{CDE} = \text{R}$
* $\{\text{ABCDE}\} = \text{R}$
* $\text{True}$
* ② $\text{ABCD} \cap \text{CDE} \neq \emptyset$
* $\text{CD}$
* ③ $\text{C, D is ck}$
* $\text{So it is lossless decomposition}$

**Section 4 (Far Right):**
* $\text{R}_1(\text{ABC}) \text{ R}_2(\text{BCD}) \text{ R}_3(\text{DE})$
* $\text{BC- Com. R}_1, \text{R}_2$
* $\text{R}_1 \text{ combine } \text{R}_3$
* $\text{ABCDU DE}$
* $\text{ABCDE}$
* $\text{ABCD} \cap \text{DE} \neq \emptyset$
* $\text{D} \rightarrow \text{ck}$
* $\text{Lossless decomp.}$

## Page 101

Based on the image provided, here is the extracted text in markdown format:

**Header:**
GW GATEWAY CLASSES
$R(v, w, x, y, z)$

**Left Column:**
$z \rightarrow y$
$y \rightarrow z$
$x \rightarrow yv$
$vw \rightarrow x$

$vw^+$
$xw^+ = \{x, y, w, z\}$
$yw^+$
$zw^+$

$\text{lossy decomposition}$

1. $r1(vwx) \quad r2(xyz)$
   $\{vwx\} \cup \{xyz\} = vwxyz$

2. $r1(vw) \quad r2(yz)$
   $vw \cup yz = vwyz \quad (1 \otimes 2) \times \text{lossy decomposition}$

3. $r1(vwx) \quad r2(yz)$
   $(1) \cup \{vwxyz\} \quad (2) \quad \{vwx\} \cap \{yz\} = \phi$
   $\text{Lossy decomposition}$

4. $r1(vw) \quad r2(wxyz)$
   $r1(vw) \cup r2(wxyz) = vwxyz$
   $r1(vw) \cap r2(wxyz) \neq \phi$
   $w \quad \text{Lossy decomposition}$

**Right Column:**
(2) $\{vwx\} \cap \{yz\} = x \rightarrow x^+ = \{x, y, v, z\}$
$\text{C.k} \times$

$w^+ = \{w\} - \text{C.k.}$

**Watermark:**
Gateway classes

## Page 102

# AKTU PYQS

| Question No. | Question Text | Year |
| :--- | :--- | :--- |
| **Q.1** | What is Functional Dependency? Explain the procedure of calculating the Canonical Cover of a given Functional Dependency Set with suitable example. | AKTU 2020-21 |
| **Q.2** | (i) Consider the relation R(a,b,c,d) with Set F={a$\rightarrow$c,b$\rightarrow$d}. Decompose this relation in 2 NF. (ii) Explain the Loss Less Decomposition with example | AKTU 2020-21 |
| **Q.3** | Explain the multivalued dependency? Explain with suitable example that how functional dependency can be used to show that decompositions are loss-less? | AKTU 2019-20/2018-19 |

## Page 103

# AKTU B.Tech III-Year 5th Semester GW GATEWAY CLASSES

**CS IT & CS Allied**

## DBMS: Database Management System

### UNIT 3
**Database Design and Normalization**
**Lecture-10**

**Today's Target**
* ...Lossless decomposition
* 5NF
* AKTU PYQs

**By PRAGYA RAJVANSHI**
B.Tech, M.Tech( C.S.E.)

## Page 104

# Text Extraction

**Top Left:**
ew GATEWAY CLASSES

**Main Content (Left Side):**
1. $R(v, w, x, y, z)$

$z \rightarrow y$
$y \rightarrow z$
$x \rightarrow yv$
$vw \rightarrow x$

Lossless Decomposition

1. $r1(vwx) \quad r2(xyz)$
2. $r1(vw) \quad r2(yz)$
3. $r1(vwx) \quad r2(yz)$
4. $r1(\underline{vw}) \quad r2(wxyz)$

**Handwritten Notes (Center/Left):**
①
$r_1(VWX) \quad r_2(XYZ)$
$r_1 \cup r_2 = R$
$(VWX) \cup (XYZ) = VWXYZ$
$VWXYZ = VWXYZ$ ①

$\text{att } r_1 \cap \text{att } r_2 \neq \emptyset$
$(VWX) \cap (XYZ) \neq \emptyset$
$X$

$r_1 \rightarrow X \text{ candidate}$
$(VWX) \quad X^+ = \{x, y, v, z\}$
$r_2$
$(XYZ) \quad X^+ = \{x, y, v, z\}$
$r_2 \text{ X is candidate key}$

**Handwritten Notes (Right Side):**
④ $r_1(VW) \quad r_2(WXYZ)$

$\text{att } r_1 \cup \text{att } r_2 = R$
$VWXYZ = VWXYZ$

$\text{att}(r_1) \cap \text{att}(r_2) \neq \emptyset$
$W \rightarrow \text{candidate ?}$

$r_1(VW) \quad W^+ = \{w\}$
$r_2(WXYZ)$
$\}$ lossy decomposition

**Watermark:**
Gateway classes

**Top Right:**
gw GATEWAY CLASSES

## Page 105

# 2. Given the following set of FDs on schema
**R (V,W,X,Y,Z) {Z $\rightarrow$ V, W $\rightarrow$ Y, XY $\rightarrow$ Z, V $\rightarrow$ WX}**

State whether the following decomposition are loss-less-join decompositions or not.
(i) R1=(V,W,X), R2=(V,Y,Z)
(ii) R1=(V,W,X), R2=(X,Y,Z).

---

**Left Column Notes:**
$Z \rightarrow V$
$W \rightarrow Y$
$XY \rightarrow Z$
$V \rightarrow WX$

(i) $R_1(V, W, X), R_2(V, Y, Z)$
1. $att(R_1) \cup att(R_2) = R$
$(V W X) \cup (V Y Z) = V W X Y Z$
$V W X Y Z$
2. $att(R_1) \cap att(R_2) \rightarrow$
$(V W X) \cap (V Y Z) = V$

---

**Right Column Notes:**
$R_1(V, W, X)$
$R_2(V, Y, Z)$
$V = \{V, W, X, Y, Z\}$

**Lossless decomposition**
$\frac{R_1(V W X) \quad R_2(X Y Z)}{R = V W X Y Z}$ (1)

$att(R_1) \cap att(R_2) \neq \phi$
$X$ (2)

$X^+ = \{X\}$
$R_1 = V, W, X$
$R_2 = X, Y, Z$

**lossy decomposition.**

## Page 106

# 3. Consider a relation schema R (A, B, C, D) with the following functional dependencies-

A $\rightarrow$ B
B $\rightarrow$ C
C $\rightarrow$ D
D $\rightarrow$ B

**Determine whether the decomposition of R into $R_1(A, B)$, $R_2(B, C)$ and $R_3(B, D)$ is lossless or lossy.**

---

### Handwritten Notes

**Left Section:**
$R(A, B, C, D)$
$\swarrow \searrow$
$R'(A, B, C) \quad R_3(B, D)$
$\swarrow \searrow$
$R_1(A, B) \quad R_2(B, C)$

**Middle Section:**
$R'(A, B, C)$
$R_1(A, B) \quad R_2(B, C)$

$att(R_1) \cup att(R_2) = R'$
$(A, B) \cup (B, C) = ABC$

$att(R_1) \cap att(R_2) = \{B\}$
$(A, B) \cap (B, C) = B$

$att(R_1 \cap att(R_2)) \rightarrow att(R_1) / att(R_2)$
$R_1(A, B) \quad B^+ = \{B, C, D\}$
$R_2(B, C) \quad R_2 \subset B^+$
Lossless decomposition

**Right Section:**
$R(A, B, C, D)$
$R'(A, B, C) \quad R_3(B, D)$

① $att(R') \cup att(R_3) = R$
$ABC \cup BD = R$
$ABCD$

② $att(R') \cap att(R_3) \neq \emptyset$
$(ABC) \cap (BD) = B$

$att(R' \cap att(R_3)) \rightarrow att(R') / att(R_3)$
$R'(A, B, C) \quad B^+ = \{B, C, D\}$
$R_3(B, D) \quad B, C \subset R_3$

Overall Decomposition is lossless

## Page 107

# Dependency preserving decomposition

**Diagram:**
*   **R** (FD)
    *   $\swarrow$ **R1** (FD1)
    *   $\searrow$ **R2** (FD2)
    *   $\searrow$ **FP** (FP)
    *   $\swarrow$ **FP** (FP)
*   $\text{FD}_1 \cup \text{FD}_2$

---

**Example:**
1. $\text{R(A, B, C)}$
    *   $\text{A} \rightarrow \text{B}$
    *   $\text{B} \rightarrow \text{C}$
    *   $\text{C} \rightarrow \text{A}$

$\text{R1(A, B)}, \text{R2(B, C)} \rightarrow \text{Dependency preserving decomposition}$

**Whether this decomposition is dependency preserving or not**

$\text{R}_1(\text{A, B})$
*   $\text{A}^+ = \{\text{A, B, C}\}$
*   $\text{B}^+ = \{\text{B, C, A}\}$
*   $\text{A} \rightarrow \text{B}$
*   $\text{B} \rightarrow \text{A}$ $\{F_1\}$

$\text{R}_2(\text{B, C})$
*   $\text{B}^+ = \{\text{B, C, A}\}$
*   $\text{C}^+ = \{\text{C, A, B}\}$
*   $\text{B} \rightarrow \text{C}$
*   $\text{C} \rightarrow \text{B}$ $\{F_2\}$

$\text{F}_1 \cup \text{F}_2$
*   $\text{C} \rightarrow \text{B}(\text{F}_2)$
*   $\text{B} \rightarrow \text{A}(\text{F}_1)$
*   $\rightarrow \text{C} \rightarrow \text{A}$

$\text{trivial dependency}$
$\{\text{A} \rightarrow \text{A}$
$\text{B} \rightarrow \text{B}\}$

## Page 108

# R(A B C D)

**AB $\rightarrow$ CD**
**D $\rightarrow$ A**

Whether this decomposition is dependency preserving or not.

$R_1(A, D)$
$R_2(B, C, D)$

$A^+ = \{A\}$
$D^+ = \{D, A\}$
$D \rightarrow A \begin{cases} F_1 \end{cases}$

$B^+ = \{B\}$
$C^+ = \{C\}$
$D^+ = \{D, A\}$
$BC = \{B, C\}$
$BD = \{BD, A\}$
$CD = \{CD, A\}$

$B \rightarrow B \times$
$C \rightarrow C \times$
$D \rightarrow D \times$
$D \rightarrow A \begin{cases} F_2 \end{cases}$
$BC \rightarrow BC \times$
$BD \rightarrow A \times$
$CD \rightarrow A \times$

$F_1 \cup F_2$
$AB \rightarrow CD \text{ (lost)}$

*Handwritten note:*
It is not a Dependency preserving decomposition

## Page 109

# What is transitive dependencies? what are problem arise when transitive dependences present in the database.

A transitive dependency occurs in a database when a non-prime attribute (not part of the candidate key) depends indirectly on a candidate key through another non-prime attribute.

For example, in a relation R(A, B, C)
A -> B
B -> C
(transitive dependency)

$R\{A, B, C\}$
$A^+ = \{A, B, C\}$ Prime = $\{A\}$
$ck = \{A\}$ Non-prime = $\{B, C\}$
$R_1(AB) A \rightarrow B$
$R_2(BC) B \rightarrow C$

---

### Student

| Student_ID | Student_Name | Department_ID | Department_Name |
| :--- | :--- | :--- | :--- |
| 1 | Alice | D01 | Computer science |
| 2 | Bob | D02 | Maths |
| 3 | Charlie | D01 | Computer science |

**Functional dependencies**
Student_ID $\rightarrow$ Department_ID
Department_ID $\rightarrow$ Department_Name
Studentid $\rightarrow$ Student_name

$(Student.id)^+ = \{Departmentid, Studentid, Departmentname, Studentname\}$

## Page 110

# Problems with Transitive Dependency:

**Data Redundancy:** The Department_Name is repeated for every student in the same department.

**Update Anomaly:** If "Computer Science" changes to "CS", all rows for D01 must be updated.

**Insertion Anomaly:** Cannot add a new department without adding a student.

**Deletion Anomaly:** If the last student in a department is deleted, department information is also lost.

---

**R1**
| Studentid | StudentName | Departmid |
| :--- | :--- | :--- |
| 1 | Alice | D01 |
| 2 | Bob | D02 |
| 3 | Charlie | D02 |

Studentid $\rightarrow$ StudentName
Studentid $\rightarrow$ Departmid

**R2**
| Departmid | DepartmatName |
| :--- | :--- |
| D01 | Computision |
| D02 | Math |

Departmentid $\rightarrow$ Departmatname

## Page 111

# Join dependency

* A join dependency is a constraint in a database that specifies how a table can be split into **multiple smaller tables** and then **joined back without any loss of information**.
* A relation has a join dependency if it can be decomposed into two or more sub-relations R1, R2, ..., Rn, such that the natural join of these sub-relations exactly recreates the original relation R.
* A join dependency that is not implied by candidate keys leads to a violation of 5th Normal Form (5NF).

## Page 112

# Table: R1

| Company | Product | Agent |
| :--- | :--- | :--- |
| C1 | TV | Aman |
| C1 | AC | Aman |
| C2 | Refrigerator | Mohan |
| C2 | TV | Mohit |

# Table: R2

| Product | Agent |
| :--- | :--- |
| TV | Aman |
| AC | Aman |
| Refrigerator | Mohan |
| TV | Mohit |

## Page 113

$R_1 \bowtie R_2$

Here, we can see that we got two additional tuples after performing join i.e. (C1, TV, Mohan) & (C2, TV, Aman) these tuples are known as Spurious Tuple, which is not the property of Join Dependency. Therefore, we will create another relation R3 and perform its natural join with (R1 $\bowtie$ R2)

| Company | Product | Agent |
| :--- | :--- | :--- |
| C1 | TV | Aman |
| C1 | TV | Mohan |
| C1 | AC | Aman |
| C2 | Refrigerator | Mohan |
| C2 | TV | Aman |
| C2 | TV | Mohit |

## Page 114

# Table: R3

| Company | Agent |
| :--- | :--- |
| C1 | Aman |
| C2 | Mohan |
| C2 | Mohit |

---

Now on doing natural join of (R1 $\bowtie$ R2) $\bowtie$ R3, we get

| Company | Product | Agent |
| :--- | :--- | :--- |
| C1 | TV | Aman |
| C1 | AC | Aman |
| C2 | Refrigerator | Mohan |
| C2 | TV | Mohit |

---

$R = R_1 \bowtie R_2 \bowtie R_3$

## Page 115

# 5 Normal Form

* Fifth Normal Form (5NF), also known as Projection-Join Normal Form (PJNF), is a level of database normalization aimed at eliminating redundancy and anomalies due to join dependencies.
* A relation is in 5NF if it is in 4NF and every non-trivial join dependency in the relation is a consequence of the candidate keys.
* In simpler terms, 5NF ensures that a table can be decomposed into smaller tables without losing any information and without introducing any redundancy. All decompositions should be lossless and should only occur when the decomposition is based on candidate keys and join dependencies.

## Page 116

# SUPPLY

| Sname | Part_name | Proj_name |
| :--- | :--- | :--- |
| Smith | Bolt | ProjX |
| Smith | Nut | ProjY |
| Adamsky | Bolt | ProjY |
| Walton | Nut | ProjZ |
| Adamsky | Nail | ProjX |
| Adamsky | Bolt | ProjX |
| Smith | Bolt | ProjY |

The relation SUPPLY with no MVDs is in 4NF but not in 5NF if it has the JD(R1, R2, R3)

## Page 117

(d) $R_1$
| Sname | Part_name |
| :--- | :--- |
| Smith | Bolt |
| Smith | Nut |
| Adamsky | Bolt |
| Walton | Nut |
| Adamsky | Nail |

$R_2$
| Sname | Proj_name |
| :--- | :--- |
| Smith | ProjX |
| Smith | ProjY |
| Adamsky | ProjY |
| Walton | ProjZ |
| Adamsky | ProjX |

$R_3$
| Part_name | Proj_name |
| :--- | :--- |
| Bolt | ProjX |
| Nut | ProjY |
| Bolt | ProjY |
| Nut | ProjZ |
| Nail | ProjX |

Decomposing the relation SUPPLY into the 5NF relations R1, R2, R3

## Page 118

# AKTU PYQS

| Question | Description | Year |
| :--- | :--- | :--- |
| **Q.1** | Given the following set of FDs on schema R (V,W,X,Y,Z) {Z$\rightarrow$V, W$\rightarrow$Y, XY$\rightarrow$Z, V$\rightarrow$WX} State whether the following decomposition are loss-less-join decompositions or not. (i) R1=(V,W,X) , R2=(V,Y,Z) (ii) R1=(V,W,X), R2=(X,Y,Z) . | AKTU 2022-23 |
| **Q.2** | What is transitive dependencies? what are problem arise when transitive dependencess present in the database | AKTU 2021-22 |

## Page 119

# AKTU PYQS

**8 Normalisation Advantages**

| Question | Content | Year |
| :--- | :--- | :--- |
| **Q.3** | (i) What is highest normal form of the Relation R(W,X,Y,Z) with the set F= { WY $\rightarrow$ XZ, X $\rightarrow$ Y } <br><br> (ii) Consider a relation R(A,B,C,D,E) with set F= { A$\rightarrow$CD, C$\rightarrow$B,B$\rightarrow$AE} What are the prime attributes of this Relation and Decompose the given relation in 3NF. | AKTU 2020-21 |
| **Q.4** | What is transitive dependencies? what are problem arise when transitive dependences present in the database | AKTU 2021-22 |

## Page 120

# Thank you
