from setuptools import setup, find_packages

setup(name='contentRecurrent',
      version='0.1',
      description='For detect content recurrent on videos',
      url='https://github.com/epaolillo/pi-content-recurrent-video',
      author='Ezequiel Paolillo',
      author_email='paolilloe@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data = True,
      install_requires=[
          'Pillow==6.*',
          'ffmpeg_python==0.*',
          'matplotlib==3.*',
          'opencv_python==4.*',
          'pandas==0.*',
          'scipy==1.*',
          'tqdm==4.*',
          'natsort==6.*',
          'numpy==1.*',
          'pytest==6.*'
      ],
      zip_safe=False)