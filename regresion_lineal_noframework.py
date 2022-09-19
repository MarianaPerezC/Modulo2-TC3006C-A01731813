import math
date=[1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965]
gdp=[243.16,265.74,275.03,280.83,336,359.82,387.98,385.35,413.07,439.75,469.78,467.54,510.33,542.65,545.02,594.01,621.67,669.82,717.79]
promedio_date=sum(date)/len(date)
promedio_gdp=sum(gdp)/len(gdp)
x=[]
y=[]
for i in range(len(date)):
    x.append(date[i]-promedio_date)
for i in range(len(gdp)):
    y.append(gdp[i]-promedio_gdp)
xy=[]
for i in range(len(x)):
    xy.append(x[i]*y[i])
x2=[]
for i in range(len(x)):
    x2.append(x[i]*x[i])
y2=[]
for i in range(len(y)):
    y2.append(y[i]*y[i])
b1=sum(xy)/sum(x2)
b0=promedio_gdp-(promedio_date*b1)
print('Inserte el año para el que desea predecir el GDP')
year=int(input())
y_pred=(year*b1)+b0
print("El valor predicho para el año "+str(year)+" es "+ str(round(y_pred,2)))
