#Calculate the frequency of each word in a given string
#Input : AI is amazing AI is powerful
#output :
# {
#     "AI":2,
#     "is":2,
#     "amazing":1,
#     "powerful":1
# }
inputStr = "AI is amazing AI is powerful powerful"
word_list = inputStr.split()
word_freq = {}
for word in word_list:
   if word in word_freq:
      word_freq[word] += 1
   else :
      word_freq[word]=1
sorted_word = dict(sorted(word_freq.items(),key = lambda x:x[1],reverse=True))
print(sorted_word)