# ch03/03_11.py
class Car:
    def __init__(self, model, year): # 생성자
       self.model = model
       self.year = year

sonata = Car("SONATA", 2017)
g80 = Car("G80", 2018)

print(sonata.model, sonata.year)
print(g80.model, g80.year)