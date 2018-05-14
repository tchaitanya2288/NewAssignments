str = input("please enter coma separated words :")

abc = [word for word in str.split(',')]
print(",".join(sorted(list(set(abc)))))
