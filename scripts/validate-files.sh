#!/bin/bash
set -e

required_files=("README.md" "LICENSE" "CONTRIBUTING.md")

for file in "${required_files[@]}"; do
  if [ ! -f "$file" ]; then
    echo "❌ Falta el archivo obligatorio: $file"
    exit 1
  fi
done

# Validación básica del README: que no esté vacío y tenga al menos un título
if [ ! -s "README.md" ]; then
  echo "❌ README.md está vacío"
  exit 1
fi

if ! grep -q "^#" README.md; then
  echo "❌ README.md no tiene encabezados (formato básico inválido)"
  exit 1
fi

echo "✅ Todos los archivos obligatorios están presentes y válidos."