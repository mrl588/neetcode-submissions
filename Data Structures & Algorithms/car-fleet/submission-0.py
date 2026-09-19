class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), reverse = True)
        fleet = 1
        prevtime = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            cur = cars[i]
            curtime = (target-cur[0])/cur[1]
            if curtime > prevtime:
                fleet += 1
                prevtime = curtime
        return fleet
        