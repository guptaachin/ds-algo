class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i_ch = -1
        for i in range(len(word)):
            if word[i] == ch:
                i_ch = i
                break
        word_ = [w for w in word]
        if i_ch in [-1,0]:
            return word
        l = 0
        r = i_ch
        while l<r:
            word_[l], word_[r] = word_[r], word_[l]
            l += 1
            r -= 1
        return "".join(word_)

        
