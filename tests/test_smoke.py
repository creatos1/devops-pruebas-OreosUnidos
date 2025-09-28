# tests/test_smoke.py
def test_imports():
    """Smoke test: asegurar que los módulos principales se pueden importar sin errores."""
    import src.main  # o desde donde esté tu app

    assert src.main.app is not None
