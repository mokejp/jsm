import os
from setuptools import setup, find_packages
import codecs
VERSION = "0.16"

README = os.path.join(os.path.dirname(__file__),'PKG-INFO')
long_description = codecs.open(README, "r", encoding="utf-8").read() + "\n"

setup(name='jsm',
      version=VERSION,
      description="Get the japanese stock market data",
      long_description=long_description,
      install_requires=[
        'beautifulsoup4',
        'html5lib',
        "requests",
        "six"
      ],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='japanese stock market data investment',
      author='utahta',
      author_email='labs.ninxit@gmail.com',
      url='https://github.com/utahta/jsm',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
