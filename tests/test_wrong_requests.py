import allure
import pytest


@allure.title('Неправильная категория')
@allure.description('Тест попытки получения фактов при неправильной категории')
@allure.tag("ChuckNorris")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Komarov Maksim")
async def test_no_jokes_by_wrong_category(cnapi):
    '''Попытка получения фактов при неправильной категории.
    '''
    r = await cnapi.get_random_joke_by_category('automationQA')
    assert r.status_code == 404


@allure.title('Неправильная категория')
@allure.description('Тест попытки получения фактов при неправильной категории. Намеренная ошибка!')
@allure.tag("ChuckNorris")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Komarov Maksim")
@pytest.mark.xfail
async def test_failed_by_wrong_category(cnapi):
    '''Попытка получения фактов при неправильной категории.
        Намеренная ошибка! Отмечен как xfail.
    '''
    r = await cnapi.get_random_joke_by_category('manualQA')
    assert r.status_code == 200