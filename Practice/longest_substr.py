
#
#find out longest substring in alphabetical order from given string
#
s = 'azcbobobegghakl'  #input string
max = 0
cnt = 0
i_index = 0
for i in range(0, len(s)):
    cnt = 0
    for j in range(i, len(s)-1):
        if(ord(s[j]) <= ord(s[j+1])):
            cnt += 1
        else:
            break

    if cnt > max:
        i_index = i
        max = cnt

print("Longest substring in alphabetical order is: " + s[i_index:i_index+max+1])
