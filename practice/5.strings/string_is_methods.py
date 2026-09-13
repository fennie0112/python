print("1....---isalpha---")
name ="Fennie"
print(name.isalpha())

name2 = "Fennie123"
print(name2.isalpha())
print("_____________________________________________________________")

print("2....---isascii---")
special = "@#$%"
print(special.isascii())

special2 = "é"
print(special2.isascii())
print("_____________________________________________________________")


print("3....---isdecimal---")
num = "123456"
print(num.isdecimal())

num2 = "123.456"
print(num2.isdecimal())
print("_____________________________________________________________")


print("4....---isdigit---")
num3 = "123456"
print(num3.isdigit())
print("_____________________________________________________________")

print("5....---isidentifier---")
#space not allowed
name3 = "Fennie"
print(name3.isidentifier())

name4 = "Fennie 123"
print(name4.isidentifier())
print("_____________________________________________________________")


print("6....---islower---")
name5 = "fennie"
print(name5.islower())

name6 = "Fennie"
print(name6.islower())
print("_____________________________________________________________")


print("7....---isnumeric---")
num4 = "123456" 
print(num4.isnumeric())
print("_____________________________________________________________")

print("8....---isprintable---")
name7 = "Fennie"
print(name7.isprintable())

name8 = "Fennie\n"
print(name8.isprintable())
print("_____________________________________________________________")


print("9....---isspace---")
name9 = "  "
print(name9.isspace())

name10 = "Fennie   "
print(name10.isspace())
print("_____________________________________________________________")

print("10....---istitle---")
name11 = "Hello World"
print(name11.istitle())

name12 = "hello world"
print(name12.istitle())
print("_____________________________________________________________")


print("11....---isupper---")
name13 = "FENNIE"
print(name13.isupper())
name14 = "Fennie"   
print(name14.isupper())
print("_____________________________________________________________")

print("12....---join---")
name15 = "Fennie"
