#!/usr/bin/env python3

from unittest.mock import Mock,MagicMock,patch,call
from unittest import TestCase
from leopard import Report,Section
from os.path import expanduser as eu

class test_report(TestCase):
    def setUp(self):
        with patch('time.strftime', return_value='2017_01_01'):
            self.report = Report(title=MagicMock(),intro=Mock(),conclusion=MagicMock(),outname='mockname')
        self.report.sections += [MagicMock(),MagicMock(),MagicMock()] #Mock sections
        self.kwargs = { #Mock arguments for making a section
            'figures': (('fig1',Mock()),('fig2',Mock())),
            'tables': (('tab1',Mock()),('tab2',Mock()))
            }

    def tearDown(self):
        del self.report, self.kwargs

    def test_append(self):
        self.report.append(MagicMock(),MagicMock(),**self.kwargs)
        self.assertEqual(len(self.report.sections),4) #4 because already 3 mock sections
        # Test appending as subsection
        self.report.append(MagicMock(),MagicMock(),toSection=-1,**self.kwargs)
        # Check that subsection was not added as section
        self.assertEqual(len(self.report.sections),4)
        # Check that it was indeed added as subsection to section 0
        self.assertEqual(len(self.report.sections[-1].subs),1)
        
    def test_list(self):
        self.report.list()
        self.report.sections[-1].list.assert_called_with(walkTrace=(3,))

    def test_outputZip(self):
        with patch('zipfile.ZipFile',MagicMock()) as m:
            self.report.outfile = 'testzipfilename'
            self.report.outputZip()
            m.assert_called_once_with('testzipfilename.zip', 'w')
            for s in self.report.sections:
                s.sectionOutZip.assert_called_once()

    def test_outputPDF(self):
        with patch('pylatex.Document',MagicMock()) as m1,\
             patch('pylatex.utils.NoEscape',MagicMock()) as m2,\
             patch('re.compile',MagicMock()) as m3:
            self.report.outputPDF()
            m1().generate_pdf.assert_called_once_with(eu('~/Reports/mockname/2017_01_01_mockname'))
            m2.assert_any_call('\\maketitle')

class test_section(TestCase):
    def setUp(self):
        self.kwargs = { #Mock arguments for making a section
            'figures': (('fig1title',Mock()),('fig2title',Mock())),
            'tables': (('tab1title',Mock()),('tab2title',Mock()))
            }
        self.section = Section(title=MagicMock(),text=Mock(),**self.kwargs)

    def tearDown(self):
        del self.section, self.kwargs

    def test_sectionOutZip(self):
        zipcontainer = MagicMock()
        self.section.sectionOutZip(zipcontainer=zipcontainer,zipdir='mockdir/',figtype='mockfig')
        #zipcontainer.writestr.assert_any_call('mockdir/section.txt',...) # not checking as expects inconsistent mock str
        zipcontainer.writestr.assert_any_call('mockdir/fig1_fig1title.mockfig', b'')
        zipcontainer.writestr.assert_any_call('mockdir/table1_tab1title.csv', b'')
        
