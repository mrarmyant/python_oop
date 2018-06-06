class MathDojo:
    def __init__(self):
        self.result=0
    def add(self,*num):
        for val in num:
            self.result+=val
        return self
    def subtract(self,*num):
        for val in num:
            self.result-=val
        return self

md=MathDojo()
print(md.add(2).add(2,5,1).subtract(3,2).result)
