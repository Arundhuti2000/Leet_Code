class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        light=0
        heavy=n-1
        boat=0
        while light<=heavy:
            if people[light]+people[heavy]<=limit:
                boat+=1
                light+=1
                heavy-=1
            else:
                boat+=1
                heavy-=1
        return boat


  
