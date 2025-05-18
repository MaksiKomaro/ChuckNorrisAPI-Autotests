import asyncio
import pytest


@pytest.mark.asyncio
async def test_get_joke_text(cnapi):
    '''Получение текста рандомной шутки.
    '''
    r = await cnapi.get_random_joke_text()
    assert isinstance(r, str)


@pytest.mark.asyncio    
async def test_get_categories(cnapi):
    '''Получение и обновление списка категорий.
    '''
    r = await cnapi.get_categories_list()
    assert isinstance(r, list)


@pytest.mark.asyncio
async def test_async_get_jokes_status_code(cnapi):
    '''Асинхронное получение рандомных шуток по категориям.
    '''
    tasks = []
    for category in cnapi.categories:
        params = {'category':category}
        tasks.append(cnapi.get(cnapi.RANDOM_PATH, params=params))
        
    results = await asyncio.gather(*tasks)
    
    for result in results:
        assert result.status_code == 200


@pytest.mark.asyncio
@pytest.mark.parametrize('category',
                            [
                                'animal', 'career',
                                'celebrity', 'dev',
                                'explicit', 'fashion', 
                                'food', 'history',
                                'money', 'movie',
                                'music', 'political',
                                'religion', 'science',
                                'sport', 'travel'
                            ]
                        )
async def test_get_jokes_status_code(cnapi, category):
    '''Получение рандомных шуток по категориям параметризацией.
    '''
    params = {'category':category}
    r = await cnapi.get(cnapi.RANDOM_PATH, params=params)
    assert r.status_code == 200
