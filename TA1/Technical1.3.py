'''A program that will display the following given output. (for a. use nested for statement and for b. use nested while statement)

a.            1

             12

           123

         1234

       12345

b.     1

        333

        55555

        666666

        7777777'''
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

num = 1
count = 1
while num <= 7:
    if num % 2 != 0 or num == 6:
        spaces = (7 - count) // 2
        while spaces > 0:
            print (" ", end ="")
            spaces -= 1
        i = 0
        while i < count:
            print (num, end="")
            i += 1
        print()
        count += 2 if num != 6 else 1
    num += 1