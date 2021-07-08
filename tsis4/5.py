import re
rn = r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$'
print(str(bool(re.match(rn, input()))))