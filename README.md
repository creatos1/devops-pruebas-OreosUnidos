# Stock Market API

API simple para obtener precios de acciones.

## Endpoints

- `GET /stock/{symbol}` → devuelve precio de una acción

## Ejemplo

```bash
curl http://localhost:8000/stock/AAPL

> Solo necesitas que **no esté vacío** y tenga al menos una línea que empiece con `#`.

✅ Con esto, el job de validación pasará.

---

## 📁 Archivos que debes crear/actualizar en tu repositorio

| Archivo | Contenido mínimo |
|--------|------------------|
| `.flake8` | ```ini\n[flake8]\nmax-line-length = 88\nignore = E402\nexclude = .git,__pycache__,venv,.venv,.github\n``` |
| `README.md` | Cualquier texto con un `# Título` (ver ejemplo arriba) |
| (opcional) `CONTRIBUTING.md` | Puede estar vacío o con "Próximamente" |
| (opcional) `LICENSE` | Puedes usar una [MIT License](https://choosealicense.com/licenses/mit/) |

> Asegúrate de que `LICENSE` y `CONTRIBUTING.md` existan (aunque estén vacíos), porque el script los requiere.

---

## ✅ Workflow actualizado (solo cambios clave)

Tu `ci.yml` ya está bien, pero **añade `PYTHONPATH` en `smoke-test`**:

```yaml
smoke-test:
  runs-on: ubuntu-latest
  env:
    PYTHONPATH: ${{ github.workspace }}/src  # <-- IMPORTANTE
  steps:
    - uses: actions/checkout@v4
    - name: Configurar Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.9'
    - name: Instalar dependencias
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest
    - name: Ejecutar smoke tests
      run: pytest tests/test_smoke.py -v