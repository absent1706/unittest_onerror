from setuptools import setup

"""
1. set "HOME=<current folder>"

2. python setup.py sdist register -r testpypi
   or
   python setup.py sdist register -r pypi
   
3. python setup.py sdist upload -r testpypi
   or
   python setup.py sdist upload -r pypi

see http://peterdowns.com/posts/first-time-with-pypi.html
"""

setup(name='unittest_onerror',
      version='0.1',
      description='Declarative error and failure catching '
                  'for Python unittest module',
      url='https://github.com/absent1706/unittest_onerror',
      author='Alexander Litvinenko',
      author_email='litvinenko1706@gmail.com',
      license='MIT',
      py_modules=[
          'unittest_onerror'
      ],
      install_requires=[
          "mock"
      ],
      keywords=['unittest'],
      platforms='any',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Database',
      ],
  )