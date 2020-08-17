import time

i=0
initial =time.time()
while(i<=10):
    print(i)
    time.sleep(2)     # delay for 2 sec
    i+=1
    exe=time.time()   # return the no of tics

print(f"Execution time is {abs(initial-exe)} seconds")
