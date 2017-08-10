from sys import intern
n1="raina"
n2="ra"+"ina"
print(n1 is n2)#true
n1="raina lopes"
n2="raina"+" lopes"
print(n1==n2)#true
print(n1 is n2)#false
n1="raina lopes"
n2="raina lopes"
print(n1 is n2)#true because of compiler level
#rearranging of the code n1==n2="raina lopes"
a=4+5
b=8+1
print(a is b)#true
c=255+2
d=256+1
print(c is d)#false
print(c==d)#true
e=258
d=258
print(e is d)

#bypass python string caching rules
n1=intern("raina lopes")
n2=intern("raina"+" lopes")
print(n1 is n2)
