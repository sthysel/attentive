# -*- encoding: utf-8 -*-
import io
from glob import glob

from os.path import basename, dirname, join, splitext
from setuptools import find_packages, setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='attentive',
    license='GPLv2',
    version='0.1.4',
    description='Stoppable thread with common stop signalling',
    long_description=read('README.rst'),
    install_requires=[],
    author='sthysel',
    author_email='sthysel@gmail.com',
    url='https://github.com/sthysel/attentive',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[],
    extras_require={},
    setup_requires=[],
)
