count = 0

def fun():
    global count
    count = count + 1
    print("Function called")

fun()
fun()
fun()


print("Count =", count)