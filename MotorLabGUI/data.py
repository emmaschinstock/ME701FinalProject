#dummy data file for execution of a lab

f = open('data1.txt')
data = f.readlines()
dtime1,din1,dout1=[],[],[]

for i in range(len(data)):
    time,into,out = data[i].split()
    dtime1.append(time)
    din1.append(into)
    dout1.append(out)
    
dtime1 = map(float, dtime1)
din1 = map(float, din1)
dout1 = map(float, dout1)

for i in range(len(din1)):
       din1[i] = din1[i]/10000
       dout1[i] = dout1[i]/10000

f.close()

f = open('data2.txt')
data = f.readlines()
dtime2,din2,dout2=[],[],[]

for i in range(len(data)):
    time,into,out = data[i].split()
    dtime2.append(time)
    din2.append(into)
    dout2.append(out)
    
dtime2 = map(float, dtime2)
din2 = map(float, din2)
dout2= map(float, dout2)

for i in range(len(din2)):
       din2[i] = din2[i]/1000
       dout2[i] = dout2[i]/1000

f.close()

f = open('data3.txt')
data = f.readlines()
dtime3,din3,dout3=[],[],[]

for i in range(len(data)):
    time,into,out = data[i].split()
    dtime3.append(time)
    din3.append(into)
    dout3.append(out)
    
dtime3 = map(float, dtime3)
din3 = map(float, din3)
dout3 = map(float, dout3)

for i in range(len(din3)):
       din3[i] = din3[i]/200
       dout3[i] = dout3[i]/200
       
f.close()

