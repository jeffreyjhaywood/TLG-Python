#!/usr/bin/env python3
import shutil
import os
import pytest

def move_my_file():
    os.chdir('/home/student/TLG-Python/')
    shutil.move('raynor.obj', 'ceph_storage/')
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
    
def test_move_myFile():
    assert exists('/home/student/ceph_storage/kerrigan.obj') == True
