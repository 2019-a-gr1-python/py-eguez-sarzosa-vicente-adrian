import scrapy
from scrapy_03.items import ProductoFybeca

class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
    ]

    def parse_page(self, response):

        productos = response.css('div.product-tile-inner')

        for producto in productos:
            existe_producto = producto.css('div.detail')

            if(existe_producto.length > 0):
                titulo = producto.css('a.name::text')
                url = producto.xpath('/div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
                print(titulo.extract_first())
                print(url.extract_first())

        


















"""

url = response.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
contenedor = response.css('div.product-tile-inner')
titulo = contenedor.css('a.name::text')

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    return texto.replace(cadena_a_reemplazar,url)

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(transformar_url_imagen)
    )
    titulo = scrapy.Field()

from scrapy.loader import ItemLoader
il = ItemLoader(item=ProductoFybecaDos())
il.add_value('imagen',url.extract_first())
il.add_value('titulo', titulo.extract_first())
il.load_item()
"""