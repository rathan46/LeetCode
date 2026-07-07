from collections import Counter, defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        wl=len(words[0])
        wc=len(words)
        target=Counter(words)
        ans=[]
        for offset in range(wl):
            left=offset
            curr=defaultdict(int)
            count=0
            for right in range(offset,len(s)-wl+1,wl):
                word=s[right:right+wl]
                if word in target:
                    curr[word]+=1
                    count+=1
                    while curr[word]>target[word]:
                        leftWord=s[left:left + wl]
                        curr[leftWord]-=1
                        left+=wl
                        count-=1
                    if count==wc:
                        ans.append(left)
                        leftWord=s[left:left+wl]
                        curr[leftWord]-=1
                        left+=wl
                        count-=1
                else:
                    curr.clear()
                    count=0
                    left=right+wl
        return ans