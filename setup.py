try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from pip.req import parse_requirements
import uuid

install_reqs = parse_requirements("requirements.txt", session=uuid.uuid1())

reqs = [str(ir.req) for ir in install_reqs]

setup(
  name = 'pandocfilter-pygments',
  scripts = ['pandocfilter-pygments'],
  version = '0.0.1',
  description = 'Quick-and-dirty pandoc filter to pass all code blocks through pygments highlighter.',
  author = 'Piotr Gaczkowski',
  author_email = 'doomhammerng@gmail.com',
  url = 'https://github.com/doomhammer/pandocfilter-pygments',
  keywords = ['pandoc', 'pygments'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Text Processing :: Filters'
  ],
  install_requires=reqs,
)
