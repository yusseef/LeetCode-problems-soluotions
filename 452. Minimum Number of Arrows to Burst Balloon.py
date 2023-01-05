def findMinArrowShots(points):
        points.sort(key = lambda x: x[1])
        count = 0
        end = float("-inf")
        for a, b in points:
	        if end < a:
		        count += 1
		        end = b
        return count