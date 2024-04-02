import math


class matrix():

    def zad2(self):
        self.readMatrix()
        self.checkConvergence()
    def readMatrix(self):
        file = open("matrix.txt", "r")
        lines = file.readlines()
        self.matrix = []
        for line in lines:
            pom1 = line.rsplit(" ")
            for i in range(len(pom1)):
                pom1[i] = float(pom1[i].strip("\n"))
            self.matrix.append(pom1)

    def checkConvergence(self):
        if self.rowNorm() or self.collNorm() or self.matrixNorm() or self.diagonalDomination():
            return True
        else:
            return False
    def rowNorm(self):
        numRow= len(self.matrix)
        pom1 = [0]*numRow
        for i in range(numRow):
            for j in range(numRow):
                pom1[i]+=abs(float(self.matrix[i][j]))
            if i == 0:
                maximum = pom1[i]
            else:
                if maximum<pom1[i]:
                    maximum = pom1[i]
        if maximum < 1:
            return True
        else:
            return False


    #TODO dodac wykrywanie 0 i sprawdzanie wtedy max dla kolumny

    def partlyChosenMainElement(self, index, matrix):
        print("przed")
        self.printMatrix(matrix)
        numRow = int(len(matrix))
        for i in range(index, numRow):
            max = i
            for j in range(index, numRow):
                if matrix[max][index] < matrix[j][index]:
                    max = j
                pom = matrix[max]
                matrix[max] = matrix[i]
                matrix[i] = pom
        print("po")
        self.printMatrix(matrix)
        return matrix

    def gausseWithpcme(self):
        numRow = int(len(self.matrix))
        numColl = int(len(self.matrix[0]))
        pom1 = self.matrix
        for i in range(0, numRow):
            pom1 = self.partlyChosenMainElement(i, pom1)
            for j in range(i+1, numRow):
                pom2 = pom1[j][i] / pom1[i][i]
                for k in range(0, numColl):
                    pom1[j][k]-=pom1[i][k]*pom2
        results = []
        for i in range(numRow-1, -1, -1):
            for j in range(numRow, numRow-1, -1):
                pom3 = 0
                for r in range(0, len(results)):
                    pom3+=results[r]*pom1[i][numColl-r-2]
                if (pom1[i][numColl-1]-pom3) != 0 and pom1[i][i] == 0:
                    print("sprzecznosc")
                    break
                elif (pom1[i][numColl-1]-pom3) == 0 and pom1[i][i] == 0:
                    print("uklad nieoznaczony")
                    break
                else:
                    results.append((pom1[i][numColl-1]-pom3)/(pom1[i][i]))
        print(results)


    def printMatrix(self, matrix):
        numRows = len(matrix)
        for i in range(numRows):
            print(matrix[i])
        print("\n")

