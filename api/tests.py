from rest_framework.test import APITestCase, APIRequestFactory

from .views import ActorViewSet

class TestActor(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ActorViewSet.as_view({'get': 'list',
                                          'post': 'create'})
        self.url = '/actor/'

    def test_list(self):
        req = self.factory.get(self.url)
        res = self.view(req)
        self.assertEqual(res.status_code, 200,
                         'expected http code 200'
                         .format(res.status_code)
                         )

    def test_create(self):
        data = {'m_title': 'type', 'name': 'TCY', 'awards': 5}
        req = self.factory.post(self.url, data, format='json')
        res = self.view(req)
        self.assertEqual(res.status_code, 201,
                         'exepted created 201'
                         .format(res.status_code)
                         )