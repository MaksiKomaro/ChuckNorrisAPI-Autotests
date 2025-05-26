import allure
import pytest


@allure.title('Факты по категориям')
@allure.description('Последовательные тесты получения фактов из 16 категорий')
@allure.tag("ChuckNorris")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Komarov Maksim")
@pytest.mark.parametrize('category',
                            [
                                'animal', 'career', 'celebrity', 'dev',
                                'explicit', 'fashion', 'food', 'history',
                                'money', 'movie', 'music', 'political',
                                'religion', 'science', 'sport', 'travel'
                            ]
                        )
async def test_get_jokes_by_category(cnapi, category):
    '''Получение рандомных шуток по категориям параметризацией.
    '''
    r = await cnapi.get_random_joke_by_category(category)
    assert r.status_code == 200
