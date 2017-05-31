from collections import defaultdict

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sec_oop = defaultdict(int)
        gue_oop = defaultdict(int)
        bulls = cows = 0
        for i, s in enumerate(secret):
            if s == guess[i]:
                bulls += 1
            else:
                sec_oop[s] += 1
                gue_oop[guess[i]] += 1
        for x, cnt in sec_oop.iteritems():
            cows += min(cnt, gue_oop[x])
        return "{}A{}B".format(bulls, cows)
