# DO NOT CHANGE THIS FILE, OR ZERO MARK WILL BE ASSIGNED.
from Midterm import area_of_parallelogram, sum_upto, lower_left_triangle, hollow_right_parallelogram

# Test Q1: area_of_parallelogram
def test_area_of_parallelogram():
    assert area_of_parallelogram(5,6,30) == 15.00
    assert area_of_parallelogram(10,10, 60) == 86.60
    assert area_of_parallelogram(0,10, 45) == 0.0
    assert area_of_parallelogram(4,5, 90) == 20.00

# Test Q2: sum_of_numbers
def test_sum_upto():
    assert sum_upto(100)== 5050
    assert sum_upto(10) == 55
    assert sum_upto(0) == 0
    
# Test Q3: lower left triangle
def test_lower_left_triangle():
    assert lower_left_triangle(2) == "The triangle height should be at least 3."
    assert lower_left_triangle(4) == "* \n* * \n* * * \n* * * *"
    assert lower_left_triangle(5) == "* \n* * \n* * * \n* * * * \n* * * * *"

# Test Q4: hollow_left_parallelogram
def test_hollow_left_parallelogram():
    assert hollow_right_parallelogram(2) == "The rows should be at least 3."
    assert hollow_right_parallelogram(3) == "  * * * \n *   * \n* * *"
    assert hollow_right_parallelogram(4) == "   * * * * \n  *     * \n *     * \n* * * *"
    assert hollow_right_parallelogram(5) == "    * * * * * \n   *       * \n  *       * \n *       * \n* * * * *"


# Run tests
if __name__ == "__main__":
   test_area_of_parallelogram()
   test_sum_upto()
   test_lower_left_triangle()
   test_hollow_right_parallelogram() 
   print("All tests passed!")
