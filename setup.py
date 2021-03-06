from setuptools import setup  # Always prefer setuptools over distutils

__author__ = "Romain Thomas"
__credits__ = "Romain Thomas"
__license__ = "GNU GPL v3"
__version__ = "0.4.5"
__maintainer__ = "Romain Thomas"
__email__ = "the.spartan.proj@gmail.com"
__status__ = "Development"
__website__ = "https://astrom-tom.github.io/SPARTAN/build/html/index.html"

setup(
   name = 'spartan',
   version = __version__,
   author = __author__,
   author_email = __email__,
   packages = ['spartan'],
   entry_points = {'gui_scripts': ['spartan = spartan.__main__:main',],},
   url = __website__,
   license = __license__,
   description = 'Python tool for easy data plotting',
   python_requires = '>=3.6',
   install_requires = [
      "PyQt5 >= v5.10.1",
      "npyscreen >= 4.10.5",
      "scipy >= 1.0.1",
      "numpy >=1.14.2",
      "h5py >= 2.8.0",
      "tqdm >= 4.23.4",
      "astropy >= 3.0.2",
      "matplotlib >= 2.2.2",
   ],
   include_package_data=True,
)
