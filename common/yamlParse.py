# -- coding: utf-8 --
import yaml

yaml.warnings({'YAMLLoadWarning':False})
with open('testcases1.yaml', encoding='utf-8') as f:
    x = yaml.load(f)
    print(x)
