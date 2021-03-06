import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from pyas2lib import as2, exceptions


class Pyas2TestCase(unittest.TestCase):
    TEST_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'fixtures')

    @classmethod
    def setUpClass(cls):
        with open(os.path.join(cls.TEST_DIR, 'payload.txt'), 'rb') as t_file:
            cls.test_data = t_file.read()

        with open(os.path.join(
                cls.TEST_DIR, 'cert_test.p12'), 'rb') as fp:
            cls.private_key = fp.read()

        with open(os.path.join(
                cls.TEST_DIR, 'cert_test_public.pem'), 'rb') as fp:
            cls.public_key = fp.read()

        with open(os.path.join(
                cls.TEST_DIR, 'cert_mecas2_public.pem'), 'rb') as fp:
            cls.mecas2_public_key = fp.read()

        with open(os.path.join(
                cls.TEST_DIR, 'cert_oldpyas2_public.pem'), 'rb') as fp:
            cls.oldpyas2_public_key = fp.read()

        with open(os.path.join(
                cls.TEST_DIR, 'cert_oldpyas2_public.pem'), 'rb') as fp:
            cls.oldpyas2_public_key = fp.read()

        with open(os.path.join(
                cls.TEST_DIR, 'cert_oldpyas2_private.pem'), 'rb') as fp:
            cls.oldpyas2_private_key = fp.read()

        with open(os.path.join(
                cls.TEST_DIR, 'cert_sb2bi_public.pem'), 'rb') as fp:
            cls.sb2bi_public_key = fp.read()

        with open(os.path.join(
                cls.TEST_DIR, 'cert_sb2bi_public.ca'), 'rb') as fp:
            cls.sb2bi_public_ca = fp.read()
