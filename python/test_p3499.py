from math import inf


class Solution:
    def maxActiveSectionsAfterTrade1(self, s: str) -> int:
        n = len(s)
        zeroes = list()
        i = 0
        answer = 0

        while i < n:
            if s[i] == '1':
                answer += 1
                i += 1
            elif s[i] == '0':
                conti = 0
                while i + conti < n and s[i + conti] == '0':
                    conti += 1
                zeroes.append(conti)
                i += conti

        sum_max = 0
        for i in range(len(zeroes) - 1):
            local_sum = zeroes[i] + zeroes[i + 1]
            sum_max = max(local_sum, sum_max)

        return answer + sum_max

    def maxActiveSectionsAfterTrade2(self, s: str) -> int:
        n = len(s)
        zeroes = list()
        i = 0
        answer = s.count('1')

        while i < n:
            if s[i] == '0':
                conti = 0
                while i + conti < n and s[i + conti] == '0':
                    conti += 1
                zeroes.append(conti)
                i += conti
            i += 1

        local_sum = 0
        sum_max = 0
        for i in range(len(zeroes) - 1):
            local_sum = zeroes[i] + zeroes[i + 1]
            sum_max = max(local_sum, sum_max)

        return answer + sum_max

    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        i = 0
        answer = s.count('1')
        pre_conti = int(-inf)
        sum_max = 0

        while i < n:
            if s[i] == '0':
                conti = 0
                while i + conti < n and s[i + conti] == '0':
                    conti += 1
                sum_max = max(pre_conti + conti, sum_max)
                pre_conti = conti
                i += conti
            i += 1

        return answer + sum_max