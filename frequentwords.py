def patterncount(Text, Pattern):
    count=0
    c= len(Text)-len(Pattern)+1
    for i in range(c):
        if Text[i:i+len(Pattern)]==Pattern:
            count = count+1
    return(count)        

def FrequentWords(Text, K):
    frequentword = []
    count = []
    for i in range(len(Text) - K):
        pattern = Text[i:i+K]
        count.append(patterncount(Text, pattern):
    maxcount=max(count)
    for i in range(len(Text) - K):
        if count[i] == maxcount:
            frequentword.apppend(Text[i:i+K])
    frw = set(frequentword)
    return frw
        
Text = str(input())
K = int(input())
print(FrequentWords(Text,K))

        
