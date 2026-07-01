----------------------------------------------------------
### 1. Answer below questions
-----------------------------------------------------------

### 1.1. Define the problem statement
The café currently calculates customer bills manually, which is inefficient,and time-consuming,our Aim is to built an  automated Python command-line application that takes a customer's name and ordered item quantities as inputs, computes the total balance using fixed menu prices, and outputs a neatly structured receipt.

### 1.2. What are the Inputs?
* **Customer name:** `string` 
* **Coffee quantity:** `integer`
* **Tea quantity:** `integer` 
* **Sandwich quantity:** `integer`

### 1.3. What are the Outputs?
* A formatted text receipt printed to the console displaying:
  * Header and divider lines
  * Customer's name
  * Ordered quantities for Coffee, Tea, and Sandwich
  * The calculated grand total formatted with the currency code and two decimal places (`Total = RM XX.XX`)

### 1.4. What would be the typical process flow?
1. **Initialization:** Start the application execution loop.
2. **Data Acquisition (Input):** Prompt the user to enter the customer's name followed sequentially by the quantity for each item.
3. **Business Logic Processing (Computation):** Pass the raw quantities into a logic function where they are multiplied by their respective fixed unit costs and summed together:
   $$\text{Total} = (\text{Coffee} \times 8.50) + (\text{Tea} \times 6.00) + (\text{Sandwich} \times 12.00)$$
4. **Presentation Output (Rendering):** Pass the processed total along with the user details to a formatting function to display the receipt structure cleanly on screen.

### 1.5. What are the constraints?
* **Fixed Pricing Schema:** Unit prices cannot fluctuate within the application (`Coffee = RM 8.50`, `Tea = RM 6.00`, `Sandwich = RM 12.00`).
* **Data Validation Limits:** Inputs for item counts must be non-negative integers ($\ge 0$).
* **String Layout Formatting:** Total output must string-format values to display exactly two fractional decimal points.

---
-----------------------------------------------------------------------------------
## 2. Problem Decomposition
----------------------------------------------------------------------------------
we can  broken down the problem  into four distinct structural parts:
* **Input Collection Subsystem:** Handles console reading operations and converts user text streams safely into numeric integer variables.
* **Pricing/Calculation Engine:** computation routine isolated from user interactions that strictly executes the pricing mathematical formulas.
* **Formatting/Receipt Output Layout:** A display processor responsible for building strings, applying templates, and aligning margins for the printable output grid.
* **Runtime Controller:** The root main entry gate that maps outputs from the input steps straight into the business math processor, then bridges those outcomes into the printer pipeline.

---

## 3. Program Pseudocode

```text
START
    // Define constant menu pricing metrics
    CONSTANT PRICE_COFFEE = 8.50
    CONSTANT PRICE_TEA = 6.00
    CONSTANT PRICE_SANDWICH = 12.00

    // Capture user transaction details
    PRINT "Customer name: "
    READ customer_name
    
    PRINT "Coffee quantity: "
    READ coffee_qty
    
    PRINT "Tea quantity: "
    READ tea_qty
    
    PRINT "Sandwich quantity: "
    READ sandwich_qty

    // Compute final transaction balance
    SET total_bill = (coffee_qty * PRICE_COFFEE) + (tea_qty * PRICE_TEA) + (sandwich_qty * PRICE_SANDWICH)

    // Render receipt template format out to system console
    PRINT "===== RECEIPT ====="
    PRINT "Customer : " + customer_name
    PRINT "Coffee   : " + coffee_qty
    PRINT "Tea      : " + tea_qty
    PRINT "Sandwich : " + sandwich_qty
    PRINT "-------------------"
    PRINT "Total = RM " + FORMAT_TO_TWO_DECIMAL_PLACES(total_bill)
END
