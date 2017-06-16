
count = 0
def inner():
    count += 1
    print(count)

start = inner()
start()
start()