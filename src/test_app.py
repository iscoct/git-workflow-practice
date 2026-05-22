def test_health():
    assert health() == {"status": "ok"}

def test_version():
    result = version()
    assert result["version"] == "1.0.0"
    assert result["api"] == "v1"
