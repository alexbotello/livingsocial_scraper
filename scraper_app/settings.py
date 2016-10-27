BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = {
    'scraper_app.pipelines.LivingSocialPipeline': 100}

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': "Jeconais1",
    'database': 'scrape'
}
