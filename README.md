# Programming in Science - Midterm Exam - V2
420-SN1-RE: Programming In Science Winter 2025, Section 2

This template repository is the starter project for the Programming in Science Winter 2025 Midterm Exam V2. Written in Python, and tested with Pytest.

### Question(s)

1. **Write a function `area_of_parallelogram(a,b, \theta)` that calculates the area of a parallelogram given two sides `a`, `b`and angle `\theta` in degrees. [ A(a,b, \theta) = ab sin(\theta) ] .**
   
   - The function should return the area rounded to 2 decimal places.
   - Use the mathematical function `sin` from the `math` module.
   - Note that mathematical function `sin` is used for angles in radians.

 #### Example:
   ```python
   
  area_of_parallelogram(4,5,30)    # Output: 10.00
  area_of_parallelogram(5,5,45)    # Output: 17.68
 
   ```

2.  **Write a function `sum_upto(n)` that returns the sum of positive integers of 1,2,..., n.**

#### Example:
   ```python
  sum_upto(100)    # Output: 5050
  sum_upto(10)    # Output: 55
  ```


3. **Write a function `lower_left_triangle(n)` that returns a string representing a lower left triangle pattern of star-space (`* `) with height `n`.**
   - The height should be at least 3; otherwise, return: `"The triangle height should be at least 3."`


   #### Example (n = 2):
   ```
   The triangle height should be at least 3.
   ```

   #### Example (n = 3):
   ```python
   lower_left_triangle(3)

   # Output:
   
   * 
   * * 
   * * *
   ```

   #### Example (n = 5):
   ```python
   lower_left_triangle(5)

   # Output:
   
   * 
   * * 
   * * * 
   * * * * 
   * * * * *
   ```

4. **Write a function `hollow_right_parallelogram(n)` that returns a string representing a right leaning hollow parallelogram pattern of star-space (`* `) with height `n`.**
   - The rows should be at least 3; otherwise, return: `"The parallelogram rows should be at least 3."`

   #### Example (n = 2):
      ```python
   hollow_right_parallelogram(2)
  
   # Output:       
       The parallelogram rows should be at least 3.

   ```
   
   #### Example (n = 3):
      ```python
   hollow_right_parallelogram(3)

   # Output:
      
        * * * 
       *   * 
      * * *
   ```
   #### Example (n = 4):
      ```python
      
   hollow_right_parallelogram(4)

   # Output:
      
         * * * * 
        *     * 
       *     * 
      * * * *
   ```


### Run Command

```
pytest

