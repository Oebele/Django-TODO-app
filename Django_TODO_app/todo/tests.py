from django.test import TestCase

# Create your tests here.


class MyTests(TestCase):

    async def test_index(self):
        response = await self.async_client.get('')
        self.assertEqual(response.status_code, 200)
