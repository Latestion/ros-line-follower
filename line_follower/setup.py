from setuptools import setup

package_name = 'line_follower'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='udit',
    maintainer_email='you@example.com',
    description='Line follower robot using OpenCV',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'follower = line_follower.follower_node:main'
        ],
    },
)

