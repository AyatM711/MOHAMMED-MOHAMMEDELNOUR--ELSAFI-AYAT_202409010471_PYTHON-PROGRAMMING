-----------------------------------------------------------------------------------
**Identify the components**



1-Identify the inputs?
-------------------------------------------------------------------------------------
**Answer**
age , adult company,valid tickets 


--------------------------------------------------------------------------------
2-what is the process
--------------------------------------------------------------------------------
**Answer**
the system check if the user is 13 years old or older,chech if the user is accomanied by an adult ,checki if the user have a valid ticket 


--------------------------------------------------------------------------
Design the Algorithm 
---------------------------------------------------------------------------
**Answer**




Design the algorithim using draw.io/canva
-------------------------------------------------------------------------
complete the truth table 
-----------------------------------------------------------------------------


Let :
* **A** = Age $\ge$ 13
* **B** = Accompanied by adult
* **C** = Has valid ticket




| A| B  | C | A OR B | (A OR B) AND C  |
| :---: | :---: | :---: | :---: | :---: |
| False | False | False | False | **False** |
| False | False | True  | False | **False** |
| False | True  | False | True  | **False** |
| False | True  | True  | True  | **True** |
| True  | False | False | True  | **False** |
| True  | False | True  | True  | **True** |
| True  | True  | False | True  | **False** |
| True  | True  | True  | True  | **True** |


-------------------------------------------------------------
design an algorithim 
------------------------------------------------------------

1. **START**
2. Read the user's input for `age`.
3. Read the user's input for `is_accompanied` (true/false).
4. Read the user's input for `has_ticket` (true/false).
5. **IF** (`age` $\ge$ 13 OR `is_accompanied` == true) **AND** (`has_ticket` == true) **THEN**:
      * Display "Allowed to enter"
6. **ELSE**:
      * Display "Not allowed to enter"
7. **END**

-----------------------------------------------------------
create Pseudcode
-----------------------------------------------------------


```text
BEGIN
    DISPLAY "Enter your age please :"
    INPUT age
    DISPLAY "Are you accompanied by an adult? (true/false):"
    INPUT is_accompanied
    DISPLAY "Do you have a valid ticket? (true/false):"
    INPUT has_ticket

    IF (age >= 13 OR is_accompanied == true) AND (has_ticket == true) THEN
        DISPLAY "Allowed to enter"
    ELSE
        DISPLAY "Not allowed to enter"
    ENDIF
END






--------------------------------------------------------------------------------
3-what is the output 
--------------------------------------------------------------------------------
**Answer**
a messeage shoes if the user is allowed to enter or the user is not allowed 

