#!/bin/env python3

from unittest.mock import Mock
from unittest import TestCase
from leopard import Report

class test_report(TestCase):
    def setUp(self):
        self.report = Report(title=Mock(),intro=Mock(),conclusion=Mock(),outname='mockname')
        self.kwargs = {
            'figures': (('fig1',Mock()),('fig2',Mock())),
            'tables': (('tab1',Mock()),('tab2',Mock()))
            }

    def tearDown(self):
        del self.report, self.kwargs

    def test_append(self):
        self.report.append(Mock(),Mock(),**self.kwargs)
        self.assertEqual(len(self.report.sections),1)
        # Test appending as subsection
        self.report.append(Mock(),Mock(),toSection=0,**self.kwargs)
        # Check that subsection was not added as section
        self.assertEqual(len(self.report.sections),1)
        # Check that it was indeed added as subsection to section 0
        self.assertEqual(len(self.report.sections[0].subs),1)
        
    def test_list(self):
        self.report.sections += [Mock(),Mock(),Mock()]
        self.report.list()
        self.report.sections[-1].list.assert_called_with(walkTrace=(2,))
