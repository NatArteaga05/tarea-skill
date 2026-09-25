# Casos de prueba: Búsqueda de productos

## TC-001 — Mostrar únicamente productos coincidentes

**Precondiciones**
- Hay productos disponibles, incluidos productos que coinciden y productos que no coinciden con el término de búsqueda.

**Pasos**
1. Escribir en el campo «Buscar...» un término que coincida con uno o más productos.

**Resultado esperado**
Se muestran únicamente los productos que coinciden con el término de búsqueda; no se muestran los productos que no coinciden.

## TC-002 — No mostrar productos cuando no hay coincidencias

**Precondiciones**
- Hay productos disponibles.

**Pasos**
1. Escribir en el campo «Buscar...» un término que no coincida con ningún producto.

**Resultado esperado**
No se muestra ningún producto.

## TC-003 — Actualizar resultados mientras se escribe

**Precondiciones**
- Hay productos disponibles con nombres que coinciden con distintos prefijos del término que se va a escribir.

**Pasos**
1. Escribir el término de búsqueda carácter por carácter en el campo «Buscar...», sin enviar un formulario ni confirmar la búsqueda.
2. Observar los productos mostrados después de cada carácter.

**Resultado esperado**
Los productos mostrados se actualizan mientras se escribe y, en cada actualización, solo se muestran productos que coinciden con el texto ingresado hasta ese momento.
