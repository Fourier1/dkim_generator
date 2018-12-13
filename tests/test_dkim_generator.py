#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

from unittest import TestCase, main
from dkim.generate import generate_dkim, delete_dkim, print_dkim


class TestGetAccount(TestCase):
    """
    Zimbra test DKIM
    """

    def setUp(self):
        """"""
        self.domaine = "domainna.ci"

    def test_create_print_delete_DKIM(self):
        """ creation afficher suppression DKIM """
        c_dkim = generate_dkim(self.domaine)
        self.assertIsNotNone(c_dkim, "ok")

        p_dkim = print_dkim(self.domaine)
        self.assertIsNotNone(p_dkim, "ok")

        d_dkim = delete_dkim(self.domaine)
        self.assertIsNotNone(d_dkim, "ok")


if __name__ == '__main__':
    main()
