

import unittest
from cpuinfo import cpuinfo


class DataSource(object):
	bits = '64bit'
	cpu_count = 1
	is_windows = False
	raw_arch_string = 'x86_64'

	@staticmethod
	def has_proc_cpuinfo():
		return False

	@staticmethod
	def has_dmesg():
		return False

	@staticmethod
	def cat_proc_cpuinfo():
		return 1, None

	@staticmethod
	def cpufreq_info():
		return 1, None

	@staticmethod
	def sestatus_allow_execheap():
		return False

	@staticmethod
	def sestatus_allow_execmem():
		return False

	@staticmethod
	def dmesg_a_grep_cpu():
		return 1, None

	@staticmethod
	def dmesg_a_grep_origin():
		return 1, None

	@staticmethod
	def dmesg_a_grep_features():
		return 1, None

	@staticmethod
	def sysctl_machdep_cpu_hw_cpufrequency():
		return 1, None

	@staticmethod
	def isainfo_vb():
		return 1, None

	@staticmethod
	def kstat_m_cpu_info():
		return 1, None




class TestExample(unittest.TestCase):
	def test_all(self):
		cpuinfo.DataSource = DataSource

		self.assertEqual(None, cpuinfo.get_cpu_info_from_registry())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_proc_cpuinfo())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_sysctl())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_kstat())

		self.assertEqual(None, cpuinfo.get_cpu_info_from_dmesg())

		#self.assertEqual(None, cpuinfo.get_cpu_info_from_cpuid())

		#self.assertEqual(None, cpuinfo.get_cpu_info())



