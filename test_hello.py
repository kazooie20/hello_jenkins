import pytest
from hello import *

#This is a test hello jenkins!

def test_hello():
    results = hello()
    assert results == "Hello!"
    
