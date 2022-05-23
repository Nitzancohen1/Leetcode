class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        waiting_time = []
        current_time = 1
        for customer in customers:
            if current_time < customer[0]:
                current_time = customer[0]
            waiting_time.append(max(current_time,customer[0]) + customer[1] - customer[0])
            current_time += customer[1]
        return (float(sum(waiting_time))/float(len(waiting_time)))