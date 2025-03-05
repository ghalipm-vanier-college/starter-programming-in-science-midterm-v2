from Midterm import area_of_ellipse, sum_of_numbers, upper_left_triangle, hollow_left_parallelogram

# Test Q1: area_of_ellipse
def test_area_of_ellipse():
    assert area_of_ellipse(5,6) == 94.25
    assert area_of_ellipse(10,10) == 314.16
    assert area_of_ellipse(0,10) == 0.0
    assert area_of_ellipse(2,5) == 31.42

# Test Q2: sum_of_numbers
def test_sum_of_numbers():
    assert sum_of_numbers([2,8,10,5])== 25
    assert sum_of_numbers([2,-7,10,8,9]) == 22
    assert sum_of_numbers([-9,4,5]) == 0.0
    assert sum_of_numbers([-2,-5, -7, -6]) == -20
    
# Test Q3: upper_left_triangle
def test_upper_left_triangle():
    assert upper_left_triangle(2) == "The triangle height should be at least 3."
    assert upper_left_triangle(4) == "* * * * \n* * * \n* * \n*"
    assert upper_left_triangle(5) == "* * * * * \n* * * * \n* * * \n* * \n*"

# Test Q4: hollow_left_parallelogram
def test_hollow_left_parallelogram():
    assert hollow_left_parallelogram(2) == "The rows should be at least 3."
    assert hollow_left_parallelogram(3) == "* * * \n *   * \n  * * *"
    assert hollow_left_parallelogram(5) == "* * * * * \n *       * \n  *       * \n   *       * \n    * * * * *"


# Run tests
if __name__ == "__main__":
   test_area_of_ellipse()
   test_sum_of_numbers()
   test_upper_left_triangle()
   test_hollow_left_parallelogram() 
   print("All tests passed!")
