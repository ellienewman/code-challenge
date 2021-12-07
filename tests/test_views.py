import pytest
from django.urls import reverse
import ast


def test_api_parse_succeeds(client):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    addr = '123 main st chicago il'
    url = reverse('address-parse')
    response = client.get(url, {'request': addr})
    content = ast.literal_eval(response.content.decode('utf-8'))
    assert response.status_code == 200
    assert content['address_components']['PlaceName'] == 'chicago'


def test_api_parse_raises_error(client):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    addr = '123 main st chicago il 123 main st'
    url = reverse('address-parse')
    response = client.get(url, {'request': addr})
    assert response.status_code == 400
