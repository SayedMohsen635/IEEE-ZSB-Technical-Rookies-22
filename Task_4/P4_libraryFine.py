# Method to calculate the libraryFine
def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0                                    # Not Late
    if(d2 < d1 and m2 == m1 and y2 == y1):      # First Case
        fine = (d1 - d2) * 15
    elif(m2 < m1 and y2 == y1):                 # Second Case 
        fine = (m1 - m2) * 500
    elif(y2 < y1):                              # Third Case
        fine = 10000
    return fine

# Program Test
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()
    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])
    
    print(libraryFine(d1, m1, y1, d2, m2, y2))