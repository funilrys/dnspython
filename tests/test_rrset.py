# -*- coding: utf-8
# Copyright (C) Dnspython Contributors, see LICENSE for text of ISC license

# Copyright (C) 2003-2007, 2009-2011 Nominum, Inc.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose with or without fee is hereby granted,
# provided that the above copyright notice and this permission notice
# appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND NOMINUM DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL NOMINUM BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import unittest

import dns.name
import dns.rrset

class RRsetTestCase(unittest.TestCase):

    def testEqual1(self):
        r1 = dns.rrset.from_text('foo', 300, 'in', 'a', '10.0.0.1', '10.0.0.2')
        r2 = dns.rrset.from_text('FOO', 300, 'in', 'a', '10.0.0.2', '10.0.0.1')
        self.assertEqual(r1, r2)

    def testEqual2(self):
        r1 = dns.rrset.from_text('foo', 300, 'in', 'a', '10.0.0.1', '10.0.0.2')
        r2 = dns.rrset.from_text('FOO', 600, 'in', 'a', '10.0.0.2', '10.0.0.1')
        self.assertEqual(r1, r2)

    def testNotEqual1(self):
        r1 = dns.rrset.from_text('fooa', 30, 'in', 'a', '10.0.0.1', '10.0.0.2')
        r2 = dns.rrset.from_text('FOO', 30, 'in', 'a', '10.0.0.2', '10.0.0.1')
        self.assertNotEqual(r1, r2)

    def testNotEqual2(self):
        r1 = dns.rrset.from_text('foo', 30, 'in', 'a', '10.0.0.1', '10.0.0.3')
        r2 = dns.rrset.from_text('FOO', 30, 'in', 'a', '10.0.0.2', '10.0.0.1')
        self.assertNotEqual(r1, r2)

    def testNotEqual3(self):
        r1 = dns.rrset.from_text('foo', 30, 'in', 'a', '10.0.0.1', '10.0.0.2',
                                 '10.0.0.3')
        r2 = dns.rrset.from_text('FOO', 30, 'in', 'a', '10.0.0.2', '10.0.0.1')
        self.assertNotEqual(r1, r2)

    def testNotEqual4(self):
        r1 = dns.rrset.from_text('foo', 30, 'in', 'a', '10.0.0.1')
        r2 = dns.rrset.from_text('FOO', 30, 'in', 'a', '10.0.0.2', '10.0.0.1')
        self.assertNotEqual(r1, r2)

    def testCodec2003(self):
        r1 = dns.rrset.from_text_list('Königsgäßchen', 30, 'in', 'ns',
                                      ['Königsgäßchen'])
        r2 = dns.rrset.from_text_list('xn--knigsgsschen-lcb0w', 30, 'in', 'ns',
                                      ['xn--knigsgsschen-lcb0w'])
        self.assertEqual(r1, r2)

    def testCodec2008(self):
        r1 = dns.rrset.from_text_list('Königsgäßchen', 30, 'in', 'ns',
                                      ['Königsgäßchen'],
                                      idna_codec=dns.name.IDNA_2008)
        r2 = dns.rrset.from_text_list('xn--knigsgchen-b4a3dun', 30, 'in', 'ns',
                                      ['xn--knigsgchen-b4a3dun'],
                                      idna_codec=dns.name.IDNA_2008)
        self.assertEqual(r1, r2)

if __name__ == '__main__':
    unittest.main()
