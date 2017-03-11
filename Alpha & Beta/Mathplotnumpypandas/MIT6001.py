import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('lin')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.clf()
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.clf()
plt.plot(mySamples, myExponential)

plt.figure('lin quad')
plt.clf()
plt.subplot(211)
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, 'b-', label='linear')
plt.legend(loc='upper left')
plt.title('Linear vs. Quadratic')
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic')
plt.legend(loc='upper left')

plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label='cubic')
plt.plot(mySamples, myExponential, 'r--', label='exponential')
plt.legend()
plt.title('Cubic vs. Exponential')

plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label='cubic')
plt.plot(mySamples, myExponential, 'r--', label='exponential')
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')


plt.figure('lin')
plt.title('Linear')
plt.xlabel('sample points')
plt.ylabel('linear function')

plt.figure('quad')
plt.title('Quadratic')
plt.xlabel('sample points')
plt.ylabel('quadratic function')

plt.figure('cube')
plt.title('Cubic')
plt.xlabel('sample points')
plt.ylabel('cubic function')

plt.figure('expo')
plt.title('Exponential')
plt.xlabel('sample points')
plt.ylabel('exponential function')
