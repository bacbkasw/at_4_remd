# -*- coding: utf-8 -*-
import requests
import jxmlease
import testit


"""
Command 4 start: pytest --testit --alluredir allure-results test_searchRegistryItem.py
Command 4 view result: allure serve allure-results
"""
url = "https://remd-dev.rt-eu.ru/port/emdr"


# @testit.externalID('API test searchRegistryItem')
# @testit.displayName('Поиск в реестре SOAP запрсом SearchRegistryItem')
@testit.step('step 1', 'Поиск МСС')
def test_searchRegistry_58type():

    headers = {'content-type': 'application/soap+xml;charset=UTF-8'}

    body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:egis="http://egisz.rosminzdrav.ru" xmlns:oas="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:ser="http://egisz.rosminzdrav.ru/iehr/emdr/service/" xmlns:wsa="http://www.w3.org/2005/08/addressing">
            <soap:Header>
            <egis:transportHeader xmlns="http://egisz.rosminzdrav.ru" xmlns:ns2="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:ns3="http://egisz.rosminzdrav.ru/iehr/emdr/service/">
            <egis:authInfo xmlns:egis="http://egisz.rosminzdrav.ru">
            <egis:clientEntityId>17c74e63-dc38-438d-a27a-a1aa063ee7b8</egis:clientEntityId>
            </egis:authInfo>
            </egis:transportHeader>
            <wsa:MessageID>09fa0dfc-a975-42ce-9739-d8afac7df2d0</wsa:MessageID>
            <wsa:Action>getSignature</wsa:Action>
            </soap:Header><soap:Body>
            <ser:searchRegistryItemRequest>
            <!--Optional:-->
            <ser:organization>1.2.643.5.1.13.13.12.2.1.1</ser:organization>
            <ser:kind>58</ser:kind>
            <ser:registerDateBegin>2021-09-11T00:00:00+03:00</ser:registerDateBegin>
            <ser:registerDateEnd>2021-09-14T00:00:00+03:00</ser:registerDateEnd>
            <!--ser:patientSnils>91426037586</ser:patientSnils-->
            </ser:searchRegistryItemRequest>
            </soap:Body>
            </soap:Envelope>"""
    body = body.encode('utf-8')

    response = requests.post(url, data=body, headers=headers)
    assert response.status_code == 200
    root = jxmlease.parse(response.text)
    # print(type(root))
    status = root["soap:Envelope"]["soap:Body"]["ns3:searchRegistryItemResponse"]["ns3:status"].get_cdata()
    find_result = [root["soap:Envelope"]["soap:Body"]["ns3:searchRegistryItemResponse"]["ns3:matches"]['ns3:item'][
                       "ns3:localUid"].get_cdata(),
                   root["soap:Envelope"]["soap:Body"]["ns3:searchRegistryItemResponse"]["ns3:matches"]["ns3:item"][
                       "ns3:registrationDateTime"].get_cdata()]

    assert status == "success"

    errors = True
    # if find_result[0] == "4a3e9455-22e6-284a-ae64-548188c2c091" and find_result[1] == "2046-09-11+03:00":
    if find_result == ["4a3e9455-22e6-284a-ae64-548188c2c091", '2021-09-13T17:12:09.896+03:00']:
        errors = False
        print(" Найдет ожидаемый документ с LocalID ", find_result[0], "и датой регистрации ", find_result[1])
        # print(root["soap:Envelope"]["soap:Body"]["ns3:searchRegistryItemResponse"]["ns3:matches"]["ns3:item"])
    assert not errors
