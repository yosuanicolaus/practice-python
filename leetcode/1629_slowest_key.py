class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        slowest_time = releaseTimes[0]
        slowest_key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            time = releaseTimes[i] - releaseTimes[i-1]
            if time > slowest_time:
                slowest_time = time
                slowest_key = keysPressed[i]
            elif time == slowest_time:
                slowest_key = max(slowest_key, keysPressed[i])

        return slowest_key


releaseTimes = [12, 23, 36, 46, 62]
keysPressed = "spuda"

s = Solution()
print(s.slowestKey(releaseTimes, keysPressed))
