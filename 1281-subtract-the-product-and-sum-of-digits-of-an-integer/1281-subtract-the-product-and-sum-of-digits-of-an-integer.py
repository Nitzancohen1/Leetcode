class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product_digits = 1
        sum_digits = 0
        for digit in str(n):
            product_digits *= int(digit)
            sum_digits += int(digit)
        return product_digits-sum_digits