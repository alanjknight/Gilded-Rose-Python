class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality -= 1

    def increment_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def backstage_pass_additional_increment(self,item):
        # if the concert is less than 10 days away increment quality once.  
        # If less than 5 days away increment quality twice.
        if item.sell_in < 10:
            self.increment_quality(item)
        if item.sell_in < 5:
            self.increment_quality(item)

    def update_sold_quality(self, item):
        if item.name == "Aged Brie":
            self.increment_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        elif item.name != "Sulfuras, Hand of Ragnaros":
            self.decrement_quality(item)

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.name not in ["Sulfuras, Hand of Ragnaros", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
                self.decrement_quality(item)
            else:
                if item.quality < 50:
                    self.increment_quality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        self.backstage_pass_additional_increment(item)  
            if item.sell_in < 0:
                self.update_sold_quality(item)
                    