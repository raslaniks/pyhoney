import pytest
import os
def test_compile_hello_world():
        
        ret_code = os.system("HOME_PATH/main.py -o tests/test1.elf tests/test1.hny")
        assert ret_code == 0
def test_compile_multiboot():
        ret_code = os.system("HOME_PATH/main.py -o tests/test1.elf tests/test2.hny")
        assert ret_code == 0
# def test_multiboot():
#         os.system("HOME_PATH/main.py -o tests/test1.elf tests/test1.hny")
# def test_hello_world():
#         os.system("HOME_PATH/main.py -o tests/test1.elf tests/test2.hny")


    
