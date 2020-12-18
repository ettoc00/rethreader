from distutils.core import setup

setup(
<<<<<<< HEAD
    name='rethreader',
    packages=['rethreader'],
    version='1.0.6',
    license='MIT',
    description='Controlled multi-threading',
    author='Ettore Cesari',
    author_email='ettore.cesari@yahoo.it',
    url='https://github.com/ettoc00/rethreader',
    download_url='https://github.com/ettoc00/rethreader/archive/1.0.6.tar.gz',
    keywords=['thread', 'multi', 'processing'],
    install_requires=[],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
=======
  name = 'rethreader',
  packages = ['rethreader'],
  version = '1.0.1',
  license='MIT',
  description = 'Controlled multi-processing',
  author = 'Ettore Cesari',
  author_email = 'ettore.cesari@yahoo.it',
  url = 'https://github.com/ettoc00/rethreader',
  download_url = 'https://github.com/ettoc00/rethreader/archive/1.0.2.tar.gz',
  keywords = ['thread', 'multi', 'processing'],
  install_requires=[
          'threading',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',
>>>>>>> 2b49df7754a6045bbaf561a291e5d1858be63886

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
