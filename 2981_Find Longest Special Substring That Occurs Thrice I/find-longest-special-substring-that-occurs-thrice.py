class Solution:
    def maximumLength(self, s: str) -> int:
        if len(s) < 3:
            return -1
        elif len(set(list(s))) == len(s):
            return -1
        else:
            alph_list = list(set(list(s)))
            if len(alph_list) == 1:
                return len(s) - 2
            else:
                temp_len = -1
                for i in range(1,len(s)-2):
                    temp_alph_list = alph_list
                    if len(temp_alph_list) == 0:
                        return temp_len
                    else:
                        alph_list = []
                        for alph in temp_alph_list:
                            temp_count = 0
                            print(temp_alph_list)
                            idx = 0
                            print(alph*i)
                            while s.find(alph*i, idx) != -1:
                                idx = s.find(alph*i, idx)+1
                                temp_count += 1
                            if temp_count >= 3:
                                temp_len = i
                                alph_list.append(alph)
            return temp_len