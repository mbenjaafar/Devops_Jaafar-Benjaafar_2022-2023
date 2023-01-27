import unittest
import flask_app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.flaskApp = flask_app.flaskApp.test_client()

    def test_loginpagina(self):
        index = self.flaskApp.get('/index')
        loginpage = self.flaskApp.get('/loginSQL')
        ntpserver = self.flaskApp.get('/ntpserver')
        self.assertEqual(loginpage.status, '200 OK')
        self.assertEqual(index.status, '200 OK')
        self.assertEqual(ntpserver.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
