from setuptools import setup

setup(name = 'leopard',
      version = '0.1.1',
      description = 'Fast lab reporting python package',
      url = 'https://github.com/beukueb/leopard',
      author = 'Christophe Van Neste',
      author_email = 'christophe.vanneste@ugent.be',
      license = 'MIT',
      packages = ['leopard'],
      install_requires = [
          'pylatex',
          'matplotlib',
          'pandas',
      ],
      zip_safe = False,
      test_suite = 'nose.collector',
      tests_require = ['nose']
)

#To install with symlink, so that changes are immediately available:
#pip install -e . 
