class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = [] 
        for i in range(len(operations)):
            if ((operations[i] != 'C') and (operations[i] != 'D') and (operations[i] != '+')): 
                score.append(int(operations[i]))
            elif operations[i] == 'C' and score != []:
                score.pop()
            elif operations[i] == 'D' and score != []: 
                score.append(2* score[-1]) 
            elif operations[i] == '+' and len(score)>= 2:
                score.append(int(score[-1])+ int(score[-2]))
            print(score)
        return sum(score)