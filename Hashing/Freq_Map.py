n = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
Freq_Map = dict()
# for i in range(0,len(n)):
#     if n[i] in Freq_Map:
#         Freq_Map[n[i]]+=1
#     else:
#         Freq_Map[n[i]]=1
# print(Freq_Map)

for i in range(0,len(n)):
    Freq_Map[n[i]] = Freq_Map.get(n[i],0)+1
    #.get returns 0 if the value is not present in dictionary 
    #if the value exists it will return the value of that key 
    #+1 will basically increment the value of that key by 1
print(Freq_Map)