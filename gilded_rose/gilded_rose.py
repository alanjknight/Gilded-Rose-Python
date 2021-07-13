class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality -= 1

    def increment_quality(self, item):
        if item.quality < 50:
            item.quality += 1

#    items_increment_in_quality["Backstage passes to a TAFKAL80ETC concert",
#                                "Sulfuras, Hand of Ragnaros",
#                                ]
    

    def update_quality(self):
        for item in self.items:
            if item.name not in ["Sulfuras, Hand of Ragnaros", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
                self.decrement_quality(item)
            else:
                if item.quality < 50:
                    self.increment_quality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            self.increment_quality(item)
                        if item.sell_in < 6:
                            self.increment_quality(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            self.decrement_quality(item)
                    else:
                        item.quality = 0
                else:
                    self.increment_quality(item)
