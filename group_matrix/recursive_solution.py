class Matrix:
    def search(self, row, col, matrix):
        if ( row < 0 or col < 0 or row > len(matrix) - 1 or col > len (matrix[0]) - 1 or matrix[row][col] == 0):
            return
        matrix[row][col] = 0
        self.search(row + 1, col, matrix)
        self.search(row - 1, col, matrix)
        self.search(row, col + 1, matrix)
        self.search(row, col - 1, matrix)

    def find(self, matrix):
        if not matrix:
            return 0
        nr_gr = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1:
                    nr_gr += 1
                    self.search(row, col, matrix)
        return nr_gr

    def iterative_sol(self, matrix):
        if not matrix:
            return 0
        nr_gr = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row < 0 or col < 0 or row > len(matrix) - 1 or col > len(matrix[0]) - 1 or matrix[row][col] == 0):
                    nr_gr += 0
                elif (row + 1 < 0 or col < 0 or row + 1 > len(matrix) - 1 or col > len(matrix[0]) - 1 or matrix[row + 1][col] == 0):
                    nr_gr += 0
                elif (row - 1 < 0 or col < 0 or row - 1 > len(matrix) - 1 or col > len(matrix[0]) - 1 or matrix[row - 1][col] == 0):
                    nr_gr += 0
                elif (row < 0 or col + 1 < 0 or row > len(matrix) - 1 or col + 1 > len(matrix[0]) - 1 or matrix[row][col + 1] == 0):
                    nr_gr += 0
                elif (row < 0 or col - 1 < 0 or row > len(matrix) - 1 or col - 1 > len(matrix[0]) - 1 or matrix[row][col - 1] == 0):
                    nr_gr += 0
                #elif matrix[row][col] == 1:
                #    nr_gr += 1
                else:
                    nr_gr += 1
        return nr_gr


ob = Matrix()

matrix = [
   [1, 0, 1, 0, 0],
   [0, 0, 1, 0, 0],
   [0, 1, 1, 0, 0],
   [0, 0, 0, 0, 0],
   [1, 1, 0, 1, 1],
   [1, 1, 1, 0, 1]
]

print(ob.find(matrix))


matrix = [
   [1, 1, 0, 0, 0],
   [0, 1, 0, 0, 1],
   [1, 0, 0, 1, 1],
   [1, 0, 0, 0, 0],
   [1, 0, 1, 0, 1]
]

print(ob.find(matrix))



matrix = [
   [1, 1, 0, 0, 0],
   [0, 1, 0, 0, 1],
   [1, 0, 0, 1, 1],
   [1, 0, 0, 0, 0],
   [1, 0, 1, 0, 1]
]

print(ob.iterative_sol(matrix))