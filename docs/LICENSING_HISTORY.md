# Historial de licenciamiento

Este documento separa el estado **histórico** de la política **actual**. No
reescribe concesiones anteriores.

## 13 de agosto de 2026: publicación inicial bajo MIT

El repositorio se publicó en el commit
[`cb6efeb`](https://github.com/vladimiracunadev-create/executive-leadership-founder-program/commit/cb6efeb99b57071238385b161fb1af56f0fc132c)
con un único archivo `LICENSE` MIT que abarcaba el software y la documentación
entonces presentes.

## 19 de agosto de 2026: último estado previo a la separación

El commit
[`ddb68fa`](https://github.com/vladimiracunadev-create/executive-leadership-founder-program/commit/ddb68faa22d37493add41d78b2767997fe35ad8a)
es el último estado publicado antes de adoptar la separación entre software y
contenido. Quien obtuvo una copia de ese estado o de uno anterior conserva los
derechos que recibió bajo MIT. Esta política no intenta revocar ni reducir esas
concesiones.

## 22 de septiembre de 2026: separación prospectiva

Desde esta fecha:

- el software auxiliar continúa bajo [MIT](../LICENSE);
- las nuevas contribuciones originales al contenido educativo se reciben bajo
  [CC BY-NC-SA 4.0](../LICENSE-CONTENT.md);
- marcas e identidad quedan fuera de ambas licencias; y
- los materiales de terceros conservan sus propios derechos.

En consecuencia, una parte del contenido existente puede estar disponible
simultáneamente bajo la concesión MIT histórica y la política CC actual. Las
revisiones originales creadas después del punto de corte no quedan cubiertas
por la licencia MIT histórica salvo que su titular lo indique expresamente.

## Autoría y contribuciones

El historial hasta el punto de corte registra a un único autor:
**Vladimir Acuña** (`vladimir.acuna.dev@gmail.com`). Las contribuciones futuras
se atribuyen a sus autores mediante el historial de Git y se aceptan bajo la
licencia correspondiente a su naturaleza, según
[CONTRIBUTING.md](../CONTRIBUTING.md).

## Cómo verificar

```bash
git log --follow -- LICENSE
git shortlog -sne --all
git show ddb68faa22d37493add41d78b2767997fe35ad8a:LICENSE
```

Este historial documenta la política del proyecto; no sustituye asesoría legal.
