# Zadanie 11

from math import sin, cos, tan

a, b, c, d, e = 0, 30, 45, 60, 90

tab1 = [a, b, c, d, e]
tab2 = [sin(a), sin(b), sin(c), sin(d), sin(e)]
tab3 = [cos(a), cos(b), cos(c), cos(d), cos(e)]
tab4 = [tan(a), tan(b), tan(c), tan(d), tan(e)]


print("Sinus 30 wynosi =", tab2[0], "Sinus 45 wynosi =", tab2[1], "Sinus 45 wynosi =",
      tab2[2], "Sinus 60 wynosi =", tab2[3], "Sinus 90 wynosi =", tab2[4])
print("Cosinus 30 wynosi =", tab3[0], "Cosinus 45 wynosi =", tab3[1], "Cosinus 45 wynosi =",
      tab2[2], "Cosinus 60 wynosi =", tab3[3], "Cosinus 90 wynosi =", tab3[4])
print("Tangens 30 wynosi =", tab4[0], "Tangens 45 wynosi =", tab4[1], "Tangens 45 wynosi =",
      tab4[2], "Tangens 60 wynosi =", tab4[3], "Tangens 90 wynosi =", tab4[4])
