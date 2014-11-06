import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

requires = [
    'pyramid',
    ]

setup(name='iampharaoh',
      version='0.0.1',
      description='A Pyramid Scaffold to Pony users (django) by Mario Idival',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Mario Idival',
      author_email='marioidival@gmail.com',
      url="https://github.com/marioidival/iampharaoh",
      keywords='pyramid scaffold',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [pyramid.scaffold]
      pharaohproject = iampharaoh:ProjectTemplate
      pharaohapps = iampharaoh:AppsTemplate
      """,
      )
