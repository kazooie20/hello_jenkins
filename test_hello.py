import pytest
from hello import *

def test_hello():
    results = hello()
    assert results == "Hello!"
    
