# Vertex of a parabola. Write a program that determines the vertex of a parabola
# from the entered values of a,b,c determines and outputs the vertex of the parabola.

# Input data format:
# The input to the program is three integers, each on a separate line.

# Output data format:
# The program outputs the coordinates of the vertex of the parabola.

def parabola_vertex(a, b, c):
    x = -(b / (2*a))
    y = (4*a * c-b**2) / (4*a)
    return x, y

print(parabola_vertex(int(input()), int(input()), int(input())))