"""
You are given two s: N and K. Lun the dog is interested in strings that satisfy the following conditions:

The string has exactly N characters, each of which is either 'A' or 'B'.
The string s has exactly K pairs (i, j) (0 <= i < j <= N-1) such that s[i] = 'A' and s[j] = 'B'.
If there exists a string that satisfies the conditions, find and return any such string. Otherwise, return an empty string.

Definition
Class: AB
Method: createString
Parameters: integer, integer
Returns: string
Method signature: def createString(self, N, K):
Limits
Time limit (s): 2.000
Memory limit (MB): 256
Constraints
- N will be between 2 and 50, inclusive.
- K will be between 0 and N(N-1)/2, inclusive.
Examples
0)
3
2
Returns: "ABB"
This string has exactly two pairs (i, j) mentioned in the statement: (0, 1) and (0, 2).
1)
2
0
Returns: "BA"
Please note that there are valid test cases with K = 0.
2)
5
8
Returns: ""
Five characters is too short for this value of K.
3)
10
12
Returns: "BAABBABAAB"
Please note that this is an example of a solution; other valid solutions will also be accepted.
"""
DEBUG = False


class AB:

    @staticmethod
    def createString(N, K):
        checkstr = 'B' * N
        found, outstr = AB.findAB(checkstr, K)
        if found:
            return outstr
        else:
            return ""


    @staticmethod
    def findAB(s, K):
        n = len(s)

        nAB = AB.countAB(s)

        if nAB == K:
            return True, s

        if s.find('B') < 0:
            return False, ""

        # Start spanning from right to left
        for i in range(n):
            if s[n - i - 1] == 'B':
                s = AB.strReplaceAt(s, n - i - 1, 'A')
                nAB = AB.countAB(s)

                if nAB == K:
                    # Found! Return output
                    return True, s

                elif nAB > K:
                    # No more to be found!
                    return False, ""

                else:
                    # Recurse further with changed string
                    found, outstr = AB.findAB(s, K)
                    if not found:
                        # Flip back and keep searching
                        s = AB.strReplaceAt(s, n - i - 1, 'B')
                    else:
                        return found, outstr

        return False, ""


    @staticmethod
    def strReplaceAt(s, i, t):
        if i < 0 or i >= len(s):
            return s
        return s[:i] + t + s[i + 1:]

    @staticmethod
    def countAB(in_str):
        n = len(in_str)
        n_a_b = n_b = 0

        for i in range(n):
            if in_str[n - i - 1] == 'A':
                n_a_b += n_b
            elif in_str[n - i - 1] == 'B':
                n_b += 1
            else:
                raise ValueError('String has to be composed of either A or B')

        return n_a_b


M = AB()

s = 'ABB'
print(s, len(s), M.countAB(s))
o = M.createString(len(s), M.countAB(s))
print("Result = {}\n".format(o))

s = 'BA'
print(s, len(s), M.countAB(s))
o = M.createString(len(s), M.countAB(s))
print("Result = {}\n".format(o))

s = 'BBABBAB'
print(s, len(s), M.countAB(s))
o = M.createString(len(s), M.countAB(s))
print("Result = {}\n".format(o))

s = 'BAABBABAAB'
print(s, len(s), M.countAB(s))
o = M.createString(len(s), M.countAB(s))
print("Result = {}\n".format(o))