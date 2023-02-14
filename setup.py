from setuptools import setup

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jun',
    maintainer_email='mswkdh3790@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mp = my_package.mpub:main', # 명령어 mp는 my_package폴더 안의 mpub코드를 하고 사요할 함수(main) 입력
            'ms = my_package.msub:main',
            'mt = my_package.mtim:main'
        ],
    },
)
