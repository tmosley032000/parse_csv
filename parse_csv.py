my_dict = {}

for line in open("test.csv","r"):
     a,b,c,num  = line.split(",")
     num = int(num)
     url = my_dict.get(a)
     if url: 
       if url.has_key(c):
         tx = url.get(c)
         if tx < num:
           my_dict[a][c] = num
       else:
         my_keys = my_dict[a].keys()
         for k in my_keys:
            temp_dict = {c:num}
            my_dict[a] =  dict(my_dict[a].items() + temp_dict.items())
     else:
         my_dict[a] = {c:num}

print my_dict

