def pascal_triangle(n):
    # Handle the edge case where n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate the subsequent rows
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        
        # Calculate the in-between values
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # End each row with a 1
        row.append(1)
        
        # Add the generated row to the triangle
        triangle.append(row)
    
    return triangle

# Testing the function
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    # Test case: n = 5
    print_triangle(pascal_triangle(5))

