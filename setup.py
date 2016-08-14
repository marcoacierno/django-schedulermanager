import pypandoc

from setuptools import setup, find_packages


VERSION = '1.0'

setup(
    name='django_schedulermanager',
    version=VERSION,
    description='A package that allows you to schedule and unschedule jobs',
    long_description=pypandoc.convert('README.md', 'rst'),
    author='Marco Acierno',
    author_email='marcoaciernoemail@gmail.com',
    packages=find_packages(),
    install_requires=['django-rq', 'rq-scheduler'],
    url='https://github.com/marcoacierno/django-schedulermanager/',
    license='MIT',
    keywords=['django_schedulermanager', ],
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Topic :: Software Development :: Libraries :: Python Modules',

        'Operating System :: OS Independent',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',

        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.8',
        'Framework :: Django',
    ],
)
