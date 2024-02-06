"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    
    def getTotalImportance(self, emps : dict, id : int)->int:
        
        imp = emps[id].importance            
        for s in emps[id].subordinates:
            imp += self.getTotalImportance(emps,s)
        
        return imp
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emps = {emp.id:emp for emp in employees}
        
        return self.getTotalImportance(emps,id)
        
        
        


        
        