#!/usr/bin/python
"""
	pycall
	~~~~~~

	A flexible python library for creating and using Asterisk call files.

	:author:	Randall Degges
	:email:		rdegges@gmail.com
	:license:	BSD, see LICENSE for more information.

	This file is used to test pycall, and ensure all functionality works as
	expected.
"""

import unittest

from pycall import CallFile
from pycall import NoActionDefinedError
from pycall import NoChannelDefinedError


class CallFileCreationTestCase(unittest.TestCase):
	"""
	Test to make sure that `CallFile`s are created properly. When not created
	properly, we test that the appropriate exceptions are raised.
	"""

	def setUp(self):
		"""
		Prepare for the tests by setting some standard variables to use for the
		tests.
		"""
		self.trunk_type = 'SIP'
		self.trunk_type_local = 'Local'
		self.trunk_name = 'flowroute'
		self.trunk_name_local = 'outbound'
		self.number = '18002223333'
		self.channel = self.trunk_type+'/'+self.trunk_name+'/'+self.trunk_name
		self.channel_local = self.trunk_type_local+'/'+self.number+'@'+ \
			self.trunk_name_local

		self.context = 'test'
		self.extension = 's'
		self.priority = '1'

		self.application = 'Playback'
		self.data = 'hello-world'

	def test_no_channel_and_no_trunk(self):
		self.assertRaises(NoChannelDefinedError, CallFile().run())

	def test_no_channel(self):
		self.assertTrue(CallFile(
			trunk_type = self.trunk_type,
			trunk_name = self.trunk_name,
			number = self.number
		).run())

	def test_no_trunk(self):
		self.assertTrue(CallFile(channel=self.channel).run())

	def test_no_action(self):
		cf = CallFile(channel=self.channel)
		self.assertRaises(NoActionDefinedError, cf.run())

	def test_no_application(self):
		self.assertTrue(CallFile(
			channel = self.channel,
			context = self.context,
			extension = self.extension,
			priority = self.priority
		).run())

	def test_no_context_extension_priority(self):
		self.assertTrue(CallFile(
			channel = self.channel,
			application = self.application,
			data = self.data
		).run())


def suite():

	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(CallFileCreationTestCase))
	return suite


if __name__ == '__main__':
	unittest.main(defaultTest='suite')
