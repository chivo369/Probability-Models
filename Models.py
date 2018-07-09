import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

# Binomial Distribution
n,p =10,0.3
k=np.arange(0,21)
bino=stats.binom.pmf(k,n,p)
plt.figure(1)
plt.subplot(221)
plt.plot(k,bino,'o-')
plt.title('Binomial Distribution')


# Poisson Distribution

rate=2
poi=stats.poisson.pmf(k,rate)
plt.subplot(222)
plt.plot(k,poi,'o-')
plt.title('Poison Distribution')


# normal distribution

mu,sigma=0,1
k=np.arange(-10,10,0.1)
nor=stats.norm.pdf(k,mu,sigma)
plt.subplot(223)
plt.plot(k,nor)
plt.title('Normal Distribution')


# Exponential Distribution

l=0.5
k=np.arange(0,15,0.1)
y=l*np.exp(-l*k)
plt.subplot(224)
plt.plot(k,y)
plt.title('Exponential Distribution')

# Beta Distribution

a=0.5
b=0.5
k=np.arange(0.01,1,0.01)
bet=stats.beta.pdf(k,a,b)
plt.figure(2)
plt.subplot(221)
plt.plot(k,bet)
plt.title('Beta Distribution')



# Erlang Distribution

a=0.5
k=np.arange(0.01,1,0.01)
bet=stats.gamma.pdf(k,a)
plt.figure(2)
plt.subplot(222)
plt.plot(k,bet)
plt.title('Erlang Distribution')
plt.show()


