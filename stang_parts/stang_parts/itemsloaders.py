from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader


class StangPartsLoader(ItemLoader):

    default_output_processor = TakeFirst()
    availability_in = MapCompose(lambda x: ''.join(list(x)).strip())
