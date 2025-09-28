# tests/test_smoke.py
def test_import_main():
    """Verifica que la aplicación principal se pueda importar sin errores."""
    from src.main import app

    assert app is not None
