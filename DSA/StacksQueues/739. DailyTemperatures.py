class Solution(object):
    def dailyTemperatures(temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for curr_day, curr_temperature in enumerate(temperatures):
            while stack and curr_temperature > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return answer
    
    def dailyTemperaturesBrute(temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if not temperatures:
            return []
        
        count = 0
        output = [0] * len(temperatures)

        for i in range(0, len(temperatures)):
            count = 1
            for j in range(i + 1, len(temperatures)):
                if (temperatures[i] > temperatures[j]):
                    count += 1
                else:
                    output[i] = count
                    break
                    
                        

        return output
            

temperatures = [73,74,75,71,69,72,76,73]
# [1,1,4,2,1,1,0,0]

print(Solution.dailyTemperatures(temperatures))


temperatures = [30,40,50,60]
# [1,1,1,0]

temperatures = [30,60,90]
print(Solution.dailyTemperaturesBrute(temperatures))

# [1,1,0]
