import allure
import asyncio
import httpx
import logging
import os
import pytest
import random
import time
from prometheus_client import CollectorRegistry, Gauge, Summary, push_to_gateway


class ChuckNorrisAPI:
    """chucknorris.io is a free JSON API for hand curated Chuck Norris facts.
        Класс, описывающий реальные факты о Чаке Норрисе!
    """
    
    BASE_URL = "https://api.chucknorris.io"
    CATEGORIES_PATH = "/jokes/categories"
    RANDOM_PATH = "/jokes/random"
    
    def __init__(self):
        self.categories = []
    
    async def get(self, path: str, params=None, headers=None) -> httpx.Response:
        """Базовый GET запрос"""
        async with httpx.AsyncClient(base_url=self.BASE_URL) as client:
            response = await client.get(path, params=params, headers=headers)
            return response
    
    async def get_categories_list(self) -> list:
        """Получить список категорий"""
        response = await self.get(self.CATEGORIES_PATH)
        self.categories = response.json()
        return self.categories
    
    async def get_random_joke_text(self, ) -> str:
        """Получить рандомную шутку"""
        response = await self.get(self.RANDOM_PATH)
        joke_text = response.json()['value']
        logging.info(joke_text)
        return joke_text


@pytest.fixture(scope='session')
def cnapi():
    '''Фикстура создания класса ChuckNorrisAPI.
    '''
    yield ChuckNorrisAPI()
    
@pytest.fixture(autouse=True)
def func_duration():
    '''Фикстура подсчета времени выполнения теста.
    '''
    start_time = time.time()
    yield
    duration = time.time() - start_time
    logging.info(f'Продолжительность тестируемой функции {duration}')
    

if __name__ == '__main__':
    cn = ChuckNorrisAPI()
    r = asyncio.run(cn.get_random_joke_text())
    print(r)
