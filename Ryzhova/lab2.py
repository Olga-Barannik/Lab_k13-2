print("First part")
print(" ")
a = 2*4%7
print("2*4%7 = " + str(a))
print("Type of result:")
print(type(a))
print(" ")
b = 2*(4%7)
print("2*(4%7) = " + str(b))
print("Type of result:")
print(type(b))
print(" ")
c = 51//6%7
print("51//6%7 = " + str(c))
print("Type of result:")
print(type(c))
print(" ")
e = (-3+5)*(2%7//3+4*2)
print("(-3+5)*(2%7//3+4*2) = " + str(e))
print("Type of result:")
print(type(e))
print(" ")
f = (3//5.0)*20+32.0
print("(3//5.0)*20+32.0 = " + str(f))
print("Type of result:")
print(type(f))
print(" ")
g = float(int(1.56))
print("float(int(1.56)) = " + str(g))
print("Type of result:")
print(type(g))
print(" ")
d = bool(-0.0)
print("bool(-0.0) = " + str(d))
print("Type of result:")
print(type(d))
print(" ")
j = float('inf')
print("float('inf') = " + str(j))
print("Type of result:")
print(type(j))
print(" ")
k = int(bool(13.56))
print("int(bool(13.56)) = " + str(k))
print("Type of result:")
print(type(k))
print(" ")
print("Second part")
print(" ")
print("Write number_ ")
v = int(input())
if v>=0:
    print("Least significant decimal digit = " + str(int((v%100-v%10)/10)))
    print("Least significant binary digit = " + str(v%10))
print(" ")
print("Third part")
print(" ")
l = 10.001**345 *13.001**249 / (9.001**355 * 11.001**269)
print("10.001^345 *13.001^249 / (9.001^355 * 11.001^269) = " + str(l))
print(" ")
print("Fourth part")
print(" ")
r = """Виконавець: Рижова
            Олександра
            Юріївна
     Група: К-13(2)"""
print(r)
