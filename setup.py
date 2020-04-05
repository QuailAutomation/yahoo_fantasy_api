from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='yahoo_fantasy_api',
      version='1.7.0',
      description='Python bindings to access the Yahoo! Fantasy APIs',
      long_description=readme(),
      url='http://github.com/QuailAutomation/yahoo_`fantasy_api',
      author='Craig',
      author_email='craigh@quailholdings.com',
      license='MIT',
      packages=['yahoo_fantasy_api'],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
      ],
      install_requires=['objectpath', 'pytz'],
      python_requires='>=3',
      zip_safe=False)
