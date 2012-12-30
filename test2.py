import sh
#print(sh.fab("-H 1PI09IS020@119.82.126.182 host_type"));
#pr=sh.fab("-H","1PI09IS020@119.82.126.182","host_type");
pr=sh.ls("/")
print (pr)
pr=sh.fab("hello")
print (pr)

print(len(pr))