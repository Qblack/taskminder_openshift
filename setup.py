from setuptools import setup

import os

# Put here required packages or
# Uncomment one or more lines below in the install_requires section
# for the specific client drivers/modules your application needs.
packages = ['Django<=1.6',
            'static3',  # If you want serve the static files in the same server
            # 'mysql-connector-python',
            # 'pymongo',
            # 'psycopg2',
           ]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='taskminder', version='1.0',
      description='OpenShift Python-3.3 / Django-1.6 Community Cartridge based application',
      author='Quinton Black', author_email='admin@example.org',
      url='http://taskminder-qblack.rhcloud.com',
      install_requires=packages,
     )
