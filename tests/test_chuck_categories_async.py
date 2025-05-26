import asyncio
import allure
import pytest
    

@allure.title('Факты по категориям')
@allure.description('Асинхронные тесты получения фактов из 16 категорий')
@allure.tag("ChuckNorris")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Komarov Maksim")
async def test_async_get_jokes_by_category(cnapi):
    '''Асинхронное получение рандомных шуток по категориям.
    '''    
    tasks = []
    
    for category in cnapi.categories:
        tasks.append(cnapi.get_random_joke_by_category(category))
        
    results = await asyncio.gather(*tasks)
    
    for result in results:
        assert result.status_code == 200
