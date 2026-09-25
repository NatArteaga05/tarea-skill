# Casos de prueba: Agregar productos al carrito

## TC-001 — Agregar un producto al carrito

**Precondiciones**
- Hay al menos un producto disponible.
- El carrito está vacío.

**Pasos**
1. En una tarjeta de producto, seleccionar «Agregar».
2. Abrir el carrito.

**Resultado esperado**
El producto seleccionado aparece en el carrito y el contador del carrito aumenta en uno.

## TC-002 — Agregar nuevamente el mismo producto

**Precondiciones**
- Hay al menos un producto disponible.
- El carrito está vacío.

**Pasos**
1. En una tarjeta de producto, seleccionar «Agregar».
2. Seleccionar «Agregar» nuevamente en la tarjeta del mismo producto.
3. Abrir el carrito.

**Resultado esperado**
El producto aparece en el carrito con cantidad 2 y el contador del carrito refleja dos productos.
