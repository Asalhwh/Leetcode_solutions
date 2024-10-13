class Solution(object):
    def romanToInt(self, s):
     rdict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
     number=0
     for i in range(len(s)):
        #check if the index i is less than i+1 or not
        if i<len(s)-1 and rdict[s[i]]<rdict[s[i+1]]:
            #substract the first one from the second
            number=number-rdict[s[i]]
        else:
            number=number+rdict[s[i]]
     return number

        
        