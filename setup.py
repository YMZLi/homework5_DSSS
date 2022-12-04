#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup
#or
#from distutils.core import setup
setup(
    name="snowflake",
    version="1.0",
    author="DSSS_Yumingzhu LI",
    author_email="ymz.li@fau.de",
    url="https://github.com/YMZLi/homework5_DSSS.git",
    packages=find_packages(),
    install_requires=["numpy","turtle","random"]
)

