# -*- coding: utf-8 -*-
from odoo import fields
from odoo.tests.common import TransactionCase


class BookCase(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(BookCase, self).setUp()

        self.book_01_test = self.env['library.book'].create(
            {
                'name': 'book one',
                'isbn': '12345214',
                'active': True,
                'used_type': 'new',
                'state': 'draft',
                'date_published': fields.date.today(),
            }
        )

    def test_01_book_values(self):
        book_id = self.book_01_test
        self.assertRecordValues(book_id, [{
            'name': 'book one',
            'isbn': '12345214',
            'active': True,
            'used_type': 'new',
            'state': 'draft',
            'date_published': fields.date.today(),
        }])
