-----------------------------------------------------------------------------------
**Identify the components**



1-Identify the inputs?
-------------------------------------------------------------------------------------
**Answer**
age , adult accompany,valid tickets 


--------------------------------------------------------------------------------
2-what is the process
--------------------------------------------------------------------------------
**Answer**
the system check if the person is 13 years old or older,chech if the user is accomanied by an adult ,checki if the user have a valid ticket 

---------------------------------------------------------------------------
3-what is the output 
--------------------------------------------------------------------------

**Answer**
a messeage shoes if the person is allowed to enter or  not allowed 




---------------------------------------------------------------------------
Design the Algorithm 
Design the algorithim using draw.io/canva
-------------------------------------------------------------------------
**Answer**


                      [Start] -> [Input: age, accompanied, ticket] -> [Is ticket valid?]
                                                         |
                                               +---------+---------+
                                               | Yes               | No
                                               v                   v
                                 [age >= 13 OR accompanied?]  [Denied Entry]
                                               |                   |
                                     +---------+---------+         |
                                     | Yes               | No      |
                                     v                   v         v
                              [Allowed Entry]        [Denied Entry] 
                                     |                   |
                                     +---------+---------+
                                               |
                                               v
                                            [End]




----------------------------------------------------------------------------
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
     BEGIN
         DISPLAY "Enter customer age: "
         INPUT age
         DISPLAY "Is customer accompanied by an adult? (true/false): "
         INPUT is_accompanied
         DISPLAY "Does customer have a valid ticket? (true/false): "
         INPUT has_ticket

     
         IF (age >= 13 OR is_accompanied == true) AND has_ticket == true THEN
             DISPLAY "OUTPUT: Access Granted. Allowed to enter."
         ELSE
             DISPLAY "OUTPUT: Access Denied. Not allowed to enter."
         ENDIF
     END





---------------------------------------------------------------------------
Evaluate the expression:
---------------------------------------------------------------------------
test with some input sample
**Answer**


Sample Case 1
If the Child alone is alone but with a ticket:
Inputs: age = 9,    is_accompanied = false,     has_ticket = true
evaluation : (9>= 13 OR false) AND true $\rightarrow$ (false OR false) AND true $\rightarrow$ false AND true $\rightarrow$ 



Output: "Not allowed to enter"









