# 🔐 Política de seguridad

Este repositorio es material educativo, pero tiene dos superficies reales de
riesgo y ambas se vigilan de forma automática.

## 🎯 Alcance

| Superficie | Qué puede fallar | Qué lo vigila |
|---|---|---|
| **Herramientas y simulador** (`tools/`, `apps/`) | Código Python que alguien ejecuta tras clonar | `bandit`, `pytest`, compilación en 3 sistemas |
| **Dependencias** (`requirements*.txt`) | Una versión con vulnerabilidad conocida llega a quien clona | `pip-audit`, semanalmente y en cada cambio |
| **Historial de git** | Un secreto o dato personal versionado por error | `gitleaks` sobre el historial completo |
| **Árbol actual** | Credenciales o PII en clases, plantillas o datos | `tools/detect_secrets.py`, `tools/detect_pii.py` |
| **Workflows** (`.github/workflows/`) | Inyección de expresiones, permisos excesivos, acciones sin pinear | `actionlint`, `zizmor` |

El portal publicado en GitHub Pages es **estático**: no tiene backend, no recoge
datos, no usa cookies ni analítica, y no envía nada a terceros salvo la carga de
la librería de diagramas desde su CDN.

## 📬 Cómo reportar una vulnerabilidad

**No abras un issue público.** Usa
[GitHub Security Advisories](https://github.com/vladimiracunadev-create/executive-leadership-founder-program/security/advisories/new),
que es un canal privado entre quien reporta y quien mantiene.

Incluye, en la medida de lo posible:

- qué componente afecta y en qué versión;
- cómo reproducirlo, paso a paso;
- qué impacto tiene y sobre quién;
- si ya existe una corrección propuesta.

**Compromiso de respuesta:** acuse en 72 horas, diagnóstico en 7 días naturales y
corrección publicada según severidad. Se dará crédito a quien reporte, salvo que
prefiera lo contrario.

## 🚫 Fuera de alcance

- Que una norma citada esté desactualizada. Eso es un **error de contenido**:
  abre un issue público con la fuente oficial vigente y su fecha.
- Que un consejo de gestión no funcione en tu contexto. Eso es una discusión
  pedagógica, y también va en un issue público.
- Vulnerabilidades de GitHub Pages, GitHub Actions o del CDN de diagramas:
  repórtalas a su proveedor.

## 📋 Qué no debes publicar aquí

Ni en issues, ni en pull requests, ni en el portafolio:

- secretos, tokens, credenciales o claves de cualquier tipo;
- datos personales reales —propios o de terceros—, incluidos RUT, correos
  personales, direcciones o números de tarjeta;
- información confidencial de empleadores, clientes, alumnos o proveedores;
- contratos, informes o cifras reales de una empresa sin autorización expresa.

Los ejercicios del programa piden documentos ejecutivos reales. **Anonimízalos
antes de compartirlos.** El detector de datos personales bloquea el cambio si
encuentra un identificador que valida su dígito verificador, pero no puede
proteger de un dato que parece genérico y no lo es: esa parte es tuya.
