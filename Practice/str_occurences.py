s = 'obbobobobobobobbbbobbobbjobobbob';
count = 0 ;
for i in range(0, len(s)-2):
    if (s[i:i+3] == 'bob'):
        count += 1
print( str(count))
