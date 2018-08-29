
#function definition
def hist(str):
  h = dict()

  for c in str:
    if c in h:
      h[c] += 1
    else:
      h[c] = 1

  return h

#function calling
h = hist('welcome')

#formatted printing
key_list = list(h.keys())
key_list.sort()
for k in key_list:
    print(str(k)+" = "+str(h[k]))
