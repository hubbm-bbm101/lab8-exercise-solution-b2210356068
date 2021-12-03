import sys
with open(sys.argv[1],encoding = "utf-8") as f:
    list=[]
    list2=[] #list for studentinfo
    dict={}
    a=0
    for line in f:
        list.append(line.split(":"))
    for element in list:
        while a<len(list):
         list2=list[a][1].split(",")
         dict.update({list[a][0]:list2})
         a+=1  
   
    for name in sys.argv[2].split(","):
        try:
            university=dict[name][0]
            department=dict[name][1]
            print(f"Name:{name}\nUniversity:{university}\nDepartment:{department}\n")
        except KeyError:
            print(f"\nNo record of ‘{name}’ was found!\n")
