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
print(Freq_Map)