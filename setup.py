from setuptools import setup

setup(name='lasotuvi_django',
      version='0.1.1',
      description='Chương trình an sao tử vi mã nguồn mở',
      url='https://github.com/doanguyen/lasotuvi-django',
      author='doanguyen',
      author_email='dungnv2410@gmail.com',
      license='MIT',
      packages=['lasotuvi_django'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      include_package_data=True,
      zip_safe=False)
