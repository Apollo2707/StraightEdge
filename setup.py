
from setuptools import setup

setup(name='StraightEdge',
      version='0.1',
      description='Webscrapper',
      long_description='Personal Built WebScrapper',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3. :: Only,
        'Topic :: Internet :: WWW/HTTP',
      ],
      keywords='webscrapper web scrapper text',
      url='https://github.com/Apollo2707/StraightEdge',
      author='Andrew Neumann',
      author_email='neumann6994@gmail.com',
      license='MIT',
      packages=['StraightEdge'],
      install_requires=[
          'markdown',
      ],
      include_package_data=True,
      zip_safe=False)
