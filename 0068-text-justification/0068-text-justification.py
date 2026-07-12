class Solution:
    def fullJustify(self, words, maxWidth):
        res=[]
        i=0
        n=len(words)
        while i<n:
            line_len=len(words[i])
            j=i+1
            while j<n and line_len+1+len(words[j])<=maxWidth:
                line_len+=1+len(words[j])
                j+=1
            num_words=j-i
            total_letters=sum(len(word) for word in words[i:j])
            if j==n or num_words==1:
                line=" ".join(words[i:j])
                line+=" " * (maxWidth-len(line))
            else:
                total_spaces=maxWidth-total_letters
                gaps=num_words-1
                even=total_spaces//gaps
                extra=total_spaces%gaps
                line=""
                for k in range(gaps):
                    line+=words[i+k]
                    line+=" "*even
                    if extra>0:
                        line+=" "
                        extra-=1
                line+=words[j-1]
            res.append(line)
            i=j
        return res