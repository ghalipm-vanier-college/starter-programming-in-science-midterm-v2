# Programming in Science - Midterm Exam - V2
420-SN1-RE: Programming In Science Winter 2025, Section 2

This template repository is the starter project for the Programming in Science Winter 2025 Midterm Exam V1. Written in Python, and tested with Pytest.

### Question(s)

1. **Write a function `area_of_ellipse(a,b)` that calculates the area of an ellipse. [ A(a,b) = πab ] .**
   - The function should return the area rounded to 2 decimal places.
   - Use the mathematical constant `π` from the `math` module.

 #### Example:
   ```python
   
  area_of_ellipse(4,5)    # Output: 62.83
  area_of_ellipse(5,5)    # Output: 78.54
 
   ```

2.  **Write a function `sum_of_numbers(numbers)` that returns the sum of `numbers`.**

#### Example:
   ```python
  sum_of_numbers([5,10,2,8])    # Output: 25
  sum_of_numbers([-7,9,10,8])    # Output: 20
  ```


3. **Write a function `upper_left_triangle(n)` that returns a string representing a upper left triangle pattern of star-space (`* `) with height `n`.**
   - The height should be at least 3; otherwise, return: `"The triangle height should be at least 3."`


   #### Example (n = 2):
   ```
   The triangle height should be at least 3.
   ```

   #### Example (n = 3):
   ```python
   upper_left_triangle(3)

   # Output:
   
    * * * 
    * * 
    *
   ```

   #### Example (n = 5):
   ```python
   upper_left_triangle(5)

   # Output:
   
    * * * * * 
    * * * * 
    * * * 
    * * 
    *
   ```

4. **Write a function `hollow_left_parallelogram(n)` that returns a string representing a left leaning hollow parallelogram pattern of star-space (`* `) with height `n`.**
   - The rows should be at least 3; otherwise, return: `"The parallelogram rows should be at least 3."`
   
   #### Example (n = 3):
      ```python
   hollow_left_parallelogram(3)

   # Output:
      
       * * * 
        *   * 
         * * *
   ```
   #### Example (n = 4):
      ```python
      
   hollow_left_parallelogram(4)

   # Output:
      
       * * * * 
        *     * 
         *     * 
          * * * *
   ```


### Run Command

```
pytest

