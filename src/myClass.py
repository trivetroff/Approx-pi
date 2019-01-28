from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import math



class Data:
    def __init__(self, data, label=None):
        self.data = data
        self.label = label

class View:
    def __init__(self):
        self.dataList=[]

    def addData(self, data):
        self.dataList.append(data)
        return self

    @abstractmethod
    def view(self):
        pass


class Graph(View, ABC):
    def __init__(self):
        super(Graph, self).__init__()
        self.legend = False

    def showLegend(self):
        #enable display for the legend
        self.legend = True
        return self

    def view(self):
        #display the Graph
        for data in self.dataList:
            plt.plot(data.data, label='{}'.format(data.label))
        if self.legend:
            plt.legend()
        plt.show()


class PiMethodes:
    def __init__(self):
        self.value = 0

    def SerieInvCarres(self, n):
        if (n<0):
            raise ValueError('N should be positive')
        result = 0
        for k in range(1, n+1):
            result += 1/math.pow(k, 2)
        return result

    def MethodeSerieInvCarres(self, n):
        return math.sqrt(6 * self.SerieInvCarres(n))

    def SerieInvCarresImparis(self, n):
        if (n < 0):
            raise ValueError('N should be positie')
        result = 0
        for k in range(0, n+1):
            result += 1 / math.pow((2 * k) + 1, 2)
        return result

    def MethodeSerieInvCarresImparis(self,n):
        return math.sqrt(8 * self.SerieInvCarresImparis(n))

    def SerieRamanujan(self,n):
        result = 0
        for k in range(0, n + 1):
            result += ((math.factorial(4 * k)) / (math.pow(math.factorial(k), 4))) * (
                        (1103 + 26390 * k) / math.pow((4 * 99), (4 * k)))
        return result

    def MethodeSerieRamanujan(self,n):
        return 1 / (((2 * math.sqrt(2)) / 9801) * self.SerieRamanujan(n))

    def realPi(self):
        return math.pi
