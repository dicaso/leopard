from setuptools import setup, find_packages

setup(name = 'leopard',
      version = '0.2.3',
      description = 'Fast lab reporting python package',
      url = 'https://github.com/beukueb/leopard',
      author = 'Christophe Van Neste',
      author_email = 'christophe.vanneste@ugent.be',
      license = 'MIT',
      packages=find_packages(),
      install_requires = [
          'pylatex',
          'python-docx',
          'matplotlib',
          'pandas',
      ],
      extras_require = {
          'documentation': ['Sphinx']
      },
      zip_safe = False,
      test_suite = 'nose.collector',
      tests_require = ['nose']
)

#To install with symlink, so that changes are immediately available:
#pip install -e . 
