from distutils.core import setup

setup(
    name='rethreader',
    packages=['rethreader'],
    version='1.1.3',
    license='MIT',
    description='Controlled multi-threading',
    author='Ettore Cesari',
    author_email='ettore.cesari@yahoo.it',
    url='https://github.com/ettoc00/rethreader',
    download_url='https://github.com/ettoc00/rethreader/archive/1.1.3.tar.gz',
    keywords=['thread', 'multi', 'processing'],
    install_requires=[],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
    ],
)
