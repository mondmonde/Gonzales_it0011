A = {'a', 'g', 'd', 'f', 'j', 'i', 'c', 'b'}
B = {'l', 'm', 'o', 'b', 'c', 'h'}
C = {'h', 'i', 'j', 'k', 'c'}

print("Elements in A:", len(A))  
print("Elements in B:", len(B)) 

b_not_ac = B - (A | C)
print("Elements in B not in A or C:", b_not_ac) 

print("i:", list(C))  

print("ii:", list(A & (A - C))) 

print("iii:", list(B & (A | C)))  

print("iv:", list(A - (B | C))) 

print("v:", list(A & B & C))

print("vi:", list(B - (A | C))) 