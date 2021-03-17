# -- coding: utf-8 --
import os
import shutil

import pytest

pytest.main(['-s', '-v', '-rerun=3', '--alluredir=./report/allure'])
os.system(r'allure generate ./report/allure -o ./report/html --clean')
shutil.make_archive('aaa', 'zip', root_dir=r'./report/html')
