from setuptools import setup

setup(name='lasotuvi_django',
      version='0.1.3',
      description='Chương trình an sao tử vi mã nguồn mở sử dụng django',
      long_description="Chương trình an sao tử vi mã nguồn mở sử dụng django",
      long_description_content_type="text/markdown",
      url='https://github.com/doanguyen/lasotuvi-django',
      author='doanguyen',
      author_email='dungnv2410@gmail.com',
      license='MIT',
      packages=['lasotuvi_django'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      include_package_data=True,
      install_requires=[
          "Django <= 2.1",
          "lasotuvi >= 0.1.2",
          "pytz==2018.5",
          "six==1.11.0",
          "typed-ast==1.1.0",
      ],
      zip_safe=False)
