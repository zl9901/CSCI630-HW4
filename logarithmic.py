import csv
from math import  *
is2018 = False
class linear():

    def __init__(self):
        self.gradient=[0,0,0,0]
        self.w=[1,1,1,1]
        self.iterations=10000
        self.learningRate=0.0001
        self.x=[]
        self.y=[]

    def load_csv(self,filename):
        with open(filename, "r") as f:
            read = csv.reader(f)
            all_row = []
            for row in read:
                all_row.append(row)
        return all_row

    def processFile(self,data):
        global is2018
        data = data[1:]
        for i in range(len(data)):
            if is2018:
                self.x.append(float(data[i][0]))
                self.y.append(float(data[i][5]))
            else:
                self.x.append(float(data[i][0]))
                self.y.append(float(data[i][3]))

    def derivative(self,xi, yi):
        self.gradient[0]= -2*(yi-(self.w[0]+self.w[1]*xi+self.w[2]*log(xi+self.w[3])))
        self.gradient[1]= -2*(yi-(self.w[0]+self.w[1]*xi+self.w[2]*log(xi+self.w[3])))*xi
        self.gradient[2] = -2 * (yi - (self.w[0] + self.w[1] * xi + self.w[2] * log(xi + self.w[3])))*log(xi+self.w[3])
        self.gradient[0] = -2 * (yi - (self.w[0] + self.w[1] * xi + self.w[2] * log(xi + self.w[3])))*self.w[2]/(xi+self.w[3])


    def gradient_descent(self):
        # error = 1
        for item in range(self.iterations):
            for i in range(len(self.y)):
                self.derivative(self.x[i], self.y[i])
                # error = (self.y[i]-(self.w[1]*self.x[i]+self.w[0]+self.w[2]*log(self.x[i] + self.w[3]))) ** 2
                # error=(self.y[i]-(self.w[1]*self.x[i]+self.w[0]))**2
                for j in range(len(self.w)):
                    self.w[j] -= self.learningRate*self.gradient[j]
        return self.w

    def calculateError(self):
        error = 0
        for i in range(len(self.x)):
            error += (self.y[i] - (self.w[0]+self.w[1]*self.x[i]+self.w[2] * log(self.x[i]+self.w[3]))) ** 2
        return error
        # for i in range(len(self.x)):
        #     error+=(self.y[i]-(-0.046*self.x[i]+23.25))**2
        # return error



    def calculateValue(self):
        xy = 0
        for i in range(0, len(self.x)):
            xy += self.x[i] * self.y[i]
        print(xy)
        xx = 0
        for j in range(0, len(self.x)):
            xx += self.x[j] * self.x[j]
        print(xx)
        x=0
        y=0
        for k in range(0,len(self.x)):
            x+=self.x[k]
            y+=self.y[k]
        print(x)
        print(y)
        print(len(self.x))
        print(len(self.y))


def main():
    global is2018
    g = linear()
    data = g.load_csv('2017.csv')
    g.processFile(data)
    result = g.gradient_descent()
    print("w0: " + str(result[0]))
    print("w1: " + str(result[1]))
    print("w2: " + str(result[2]))
    print("w3: " + str(result[3]))
    print("2017 error for 2017 logarithmic model: " + str(g.calculateError()))

    is2018 = True
    f = linear()
    data = f.load_csv('2018.csv')
    f.processFile(data)
    error = 0
    for i in range(len(f.x)):
        error += (f.y[i] - (result[0]+result[1]*f.x[i]+result[2] * log(f.x[i] + result[3]))) ** 2
    print("2018 error for 2017 logarithmic model: " + str(error))

    # g.calculateValue()







if __name__ == "__main__": main()
