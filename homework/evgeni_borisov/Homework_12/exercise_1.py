class Flowers:
    def __init__(self, length, price, lifespan, colour, age=1):
        self.length = length
        self.price = price
        self.lifespan = lifespan
        self.colour = colour
        self.age = age

    @property
    def freshness(self):
        return self.lifespan - self.age

    def __repr__(self):
        return type(self).__name__


class Rose(Flowers):
    def __init__(self, length, price, lifespan, colour="blue", age=1):
        super().__init__(length, price, lifespan, colour, age)


class Peony(Flowers):
    pass


class Astra(Flowers):
    pass


blue_rose = Rose(90, 120, 3)
rose = Rose(100, 250, 3, 'red', 2)
peony = Peony(80, 180, 8, 'white', 3)
astra = Astra(50, 60, 5, 'yellow', 1)


# функции для будущей сортировки:
def key_freshness(flower):
    return flower.freshness


def key_colour(flower):
    return flower.colour


def key_length(flower):
    return flower.length


def key_price(flower):
    return flower.price


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add(self, flower):
        self.flowers.append(flower)

    # стоимость букета
    @property
    def bouquet_price(self):
        total_price = 0
        for flower in self.flowers:
            total_price += flower.price
        return total_price

    #  среднее время увядания цветов букете(добавлено округление в меньшую сторону через int)
    @property
    def fading_of_flowers(self):
        count = 0
        for flower in self.flowers:
            count += flower.lifespan
        return int(count / len(self.flowers))

    # метод сортировки
    def bouquet_sorting(self, key):
        self.flowers.sort(key=key)

    def find_by_longer_lifespan(self, count):
        result = []
        for flower in self.flowers:
            if flower.lifespan > count:
                result.append(flower)
        return result


bouquet = Bouquet()
bouquet.add(rose)
bouquet.add(blue_rose)
bouquet.add(peony)
bouquet.add(astra)
print("Цена букета:", bouquet.bouquet_price)
print("Среднее время увядания букета в полных днях:", bouquet.fading_of_flowers)
bouquet.bouquet_sorting(key_freshness)
print("Сортировка по времени жизни цветка:", [f.freshness for f in bouquet.flowers])
bouquet.bouquet_sorting(key_colour)
print("Сортировка по цвету:", [f.colour for f in bouquet.flowers])
bouquet.bouquet_sorting(key_length)
print("Сортировка по длине стебля:", [f.length for f in bouquet.flowers])
bouquet.bouquet_sorting(key_price)
print("Сортировка по цене:", [f.price for f in bouquet.flowers])
print('Цветы в букете :', bouquet.find_by_longer_lifespan(4))
