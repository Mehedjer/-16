class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

cat1 = Cat("барон", "мальчик", "2")
cat2 = Cat("Сэм", "Мальчик", "2")

print(cat2.gender)