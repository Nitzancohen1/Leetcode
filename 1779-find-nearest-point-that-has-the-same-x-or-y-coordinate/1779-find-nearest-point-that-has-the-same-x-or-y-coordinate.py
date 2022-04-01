class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        list1 = []
        for point in points:
            if point[0] == x or point[1] == y:
                list1.append(point)
        smallest_Manhattan_distance = 2**30
        index1 = None 
        for i in range(len(list1)):
            if smallest_Manhattan_distance > abs(x - list1[i][0]) + abs(y - list1[i][1]):
                smallest_Manhattan_distance = abs(x - list1[i][0]) + abs(y - list1[i][1])
                index1 = i
        if len(list1) == 0:
            return -1
        return points.index(list1[index1])