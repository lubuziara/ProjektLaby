import datetime

import self as self
from django.contrib.auth.models import User
from django.test import TestCase
from sklep.models import Zamowienia, Produkt



class ZamowieniaModelTests(TestCase):

    def test_order(self):
        user = User.objects.create_user(username='testuser', password='12345')
        produkt = Produkt.objects.create(name='test', price=12345)
        userid = user
        productid= produkt
        amount = 2
        order = Zamowienia.objects.create(userid=userid, productid=productid, amount=amount)
        self.assertIs(order.userid,userid)

