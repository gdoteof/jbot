from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='jbot',
      version=version,
      description="All the code Jeremey builds during the Foundations of DL course.  A Neural Net / Deep Learning / Pytorch toolkit",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jeremy Howard',
      author_email='',
      url='fast.ai',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
