msg="we learn python"
print(msg.capitalize())#Strings are immutable
name="raina lopes"
print(name.title())
print(msg.upper())
print(msg.lower())

print(msg.find("learn"))#3
print(msg.find("afternoon"))#-1
msg1="   HELLO WORLD   "
print(msg1.rstrip())
print(msg1.lstrip())
print(len(msg))

#part of a string
print(name[6:12])#lopes
print(msg[3:9])
print(msg.replace("learn","study"))
tokens=name.split(" ")
print(tokens[0])
print(tokens[1])

