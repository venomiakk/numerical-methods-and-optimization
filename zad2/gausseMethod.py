import showSteps

class matrix():
    def zad2(self):
        self.condition = 0
        self.readMatrix()
    def readMatrix(self):
        file = open("matrix.txt", "r")
        lines = file.readlines()
        self.matrix = []
        for line in lines:
            pom1 = line.rsplit(" ")
            for i in range(len(pom1)):
                pom1[i] = float(pom1[i].strip("\n"))
            self.matrix.append(pom1)
        self.veriables = [0]*len(self.matrix)
        for i in range(0, len(self.matrix)):
            self.veriables[i]=i
        self.numRow = int(len(self.matrix))


    def partlyChosenMainElement(self, index, matrix):
        max = index

        # Szukanie najwiekszej wartosci co do modulu w kolumnie
        for j in range(index, self.numRow):
            if abs(matrix[max][index]) < abs(matrix[j][index]):
                max = j

        # Jezeli najwieksza wartosc co do modulu jest rowna 0, przeszukujemy wiersze
        if matrix[max][index] == 0:
            max = index
            for i in range(index, self.numRow):
                if abs(matrix[index][i]) > abs(matrix[index][max]):
                    max = i

            # Zamiana kolumn miejscami
            for i in range(0, self.numRow):
                pom = matrix[i][max]
                matrix[i][max] = matrix[i][index]
                matrix[i][index] = pom

            # Zamiana zmiennych
            pom = self.veriables[index]
            self.veriables[index] = self.veriables[max]
            self.veriables[max] = pom

        # Zamiana wierszami
        else:
            pom = matrix[max]
            matrix[max] = matrix[index]
            matrix[index] = pom

        # showSteps.printMatrix(matrix)
        return matrix

    def fullyChosenMainElement(self, index, matrix):
        max = [index, index]

        # Szukanie najwiekszej wartosci co do modulu wsrod elementow macierzy
        for i in range(index, self.numRow):
            for j in range(index, self.numRow):
                if abs(matrix[max[0]][max[1]]) < abs(matrix[i][j]):
                    max=[i,j]

        # Zamiana wierszy
        pom = matrix[index]
        matrix[index] = matrix[max[0]]
        matrix[max[0]] = pom

        # Zamiana kolumn
        for i in range(0, self.numRow):
            pom = matrix[i][max[1]]
            matrix[i][max[1]] = matrix[i][index]
            matrix[i][index] = pom

        # Zamiana zmiennych
        pom = self.veriables[index]
        self.veriables[index] = self.veriables[max[1]]
        self.veriables[max[1]] = pom

        showSteps.printMatrix(matrix)
        return matrix

    def gausse(self, type):

        numRow = int(len(self.matrix))
        numColl = int(len(self.matrix[0]))
        pom1 = self.matrix

        # Ustawianie najwiekszego wspolczynnika na przekatnej
        for i in range(0, numRow):
            if type == 1:
                pom1 = self.partlyChosenMainElement(i, pom1)
            else:
                pom1 = self.fullyChosenMainElement(i, pom1)
            if self.condition == 0:

                # Przeksztalcenia elementarne
                showSteps.printMatrix(pom1)
                # pom1 - macierz trojkatna
                for j in range(i+1, numRow):
                    pom2 = pom1[j][i] / pom1[i][i]
                    for k in range(0, numColl):
                        pom1[j][k]-=pom1[i][k]*pom2
            results = []

        # Szukamy rozwiazania ukladu rownan
        for i in range(numRow-1, -1, -1):
            for j in range(numRow, numRow-1, -1):
                pom3 = 0
                for r in range(0, len(results)):
                    pom3+=results[r]*pom1[i][numColl-r-2]
                if (pom1[i][numColl-1]-pom3) != 0 and pom1[i][i] == 0:
                    self.condition = 1
                    # break
                elif (pom1[i][numColl-1]-pom3) == 0 and pom1[i][i] == 0:
                    self.condition = 2
                    # break
                else:
                    results.append((pom1[i][numColl-1]-pom3)/(pom1[i][i]))

        if self.condition == 0:
            for i in range(0, len(results)):
                print("x",self.veriables[len(self.veriables)-i-1]+1," = ",results[i])
        elif self.condition == 1:
            print("sprzecznosc")
        else:
            print("uklad nieoznaczony")





