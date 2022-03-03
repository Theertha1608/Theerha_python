
test_str = "Leaning python is fun"
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
# printing result 
print ("Leaning python is fun :\n "
                                        +  str(all_freq))
