from src.injector import inject
from src.analyzer import analyze

def test_injection():
    res = inject("test")
    assert "INJECTED" in res
