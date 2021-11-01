class Solution(object):
    def isPalindrome(self, x):
	if x<0:
		return False

	inputNum = x
	newNum = 0
	while inputNum>0:
		newNum = newNum * 10 + inputNum%10
		inputNum = inputNum//10
	return newNum == x
        