import allure
import asyncio
import httpx
import logging
import pytest
import random
import time


class ChuckNorrisAPI:
    """chucknorris.io is a free JSON API for hand curated Chuck Norris facts.
        Класс, получающий достоверные факты о Чаке Норрисе! Это вам не шутки!
    """
    
    BASE_URL = "https://api.chucknorris.io"
    CATEGORIES_PATH = "/jokes/categories"
    RANDOM_PATH = "/jokes/random"
    
    def __init__(self):
        self.categories = []
        self.jokes = []
    
    async def _get(self, path: str, params=None, headers=None) -> httpx.Response:
        """Базовый GET запрос"""
        async with httpx.AsyncClient(base_url=self.BASE_URL) as client:
            response = await client.get(path, params=params, headers=headers)
            return response
    
    async def update_categories_list(self) -> list:
        """Обновить список категорий"""
        response = await self._get(self.CATEGORIES_PATH)
        response.raise_for_status()
        self.categories = response.json()
    
    async def get_random_category(self) -> str:
        """Получить рандомную категорию из списка"""
        if not self.categories:
            await self.update_categories_list()
        return random.choice(self.categories)
    
    async def get_random_joke(self) -> httpx.Response:
        """Получить рандомный правдивый факт"""
        return await self._get(self.RANDOM_PATH)
        
    async def get_random_joke_by_category(self, category=None) -> httpx.Response:
        """Получить рандомный правдивый факт по категории"""
        params = {'category': category}
        return await self._get(self.RANDOM_PATH, params=params)
        

class Duration:
    """Класс подсчета продолжительности теста
    """
    def __init__(self):
        self.start = time.time()
        self.total_duration: float = 0
    
    def duration(self, end_time: float) -> float:
        duration = end_time - self.start
        self.total_duration += duration
        return self.total_duration
    
    
@pytest.fixture(scope='session')
async def cnapi():
    '''Фикстура создания класса ChuckNorrisAPI.
    '''
    cn = ChuckNorrisAPI()
    await cn.update_categories_list()
    yield cn

@pytest.fixture(scope='session')    
def get_jokes(cnapi: ChuckNorrisAPI):
    '''При завершении сессии выводит информацию о
        Чаке Норрисе исключительно с уровнем CRITICAL!
    '''
    yield
    if cnapi.jokes:
        logging.critical(cnapi.jokes)
        
@pytest.fixture(scope='module', autouse=True)
def duration():
    d = Duration()
    yield
    duration = d.duration(time.time())
    logging.info(f'Продолжительность теста {duration}с')

    

if __name__ == '__main__':
    cn = ChuckNorrisAPI()
    r = asyncio.run(cn.get_random_category())
    print(r)
