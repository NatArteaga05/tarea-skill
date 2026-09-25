---
name: acceptance-to-test-cases
description: Convierte un requisito o una funcionalidad descrita en lenguaje natural en casos de prueba manuales, estructurados y verificables para este proyecto. Úsala cuando se pidan casos o escenarios de prueba a partir de un requisito. No la uses para implementar o corregir código, diagnosticar fallos ni ejecutar pruebas.
---

# Generar casos de prueba desde requisitos

Convierte el requisito proporcionado por el usuario en uno o más casos de prueba manuales. Genera un documento Markdown y no modifiques el código de la aplicación.

## Cuándo usar esta skill

Úsala cuando el usuario proporcione un requisito o una funcionalidad en lenguaje natural y pida casos o escenarios para comprobarla.

No la uses para implementar o corregir la funcionalidad, diagnosticar un fallo, ejecutar pruebas, crear reportes de errores o documentar una funcionalidad sin casos de prueba.

## Procedimiento

1. Toma como entrada el requisito o la funcionalidad que proporcione el usuario. Si no proporciona ninguno, pídeselo.
2. Analiza únicamente los archivos del repositorio que sean pertinentes para entender el contexto del requisito. No inspecciones áreas no relacionadas.
3. Usa el código solo como contexto para identificar componentes y términos relevantes. El código no es fuente para inventar requisitos ni reglas de negocio.
4. Lee `references/test-case-guidelines.md` antes de decidir los escenarios y redactar los casos.
5. Si el requisito es ambiguo o no es verificable y la ambigüedad afecta al resultado esperado, pide aclaración antes de generar los casos afectados. No supongas el comportamiento.
6. Usa `assets/test-case-template.md` como estructura del documento generado. Completa y repite el bloque de caso de la plantilla cuando haya varios casos; no agregues campos.
7. Asigna IDs consecutivos desde `TC-001` (`TC-002`, `TC-003`, etc.).
8. Cuando esté disponible `scripts/validate_test_cases.py`, ejecuta el validador sobre el documento final. Si informa errores, corrígelos y vuelve a validarlo antes de entregar.
9. Entrega la ruta del documento y un resumen breve. No afirmes que los casos fueron ejecutados: esta skill los diseña, no los ejecuta.

## Formato obligatorio

Cada caso contiene exactamente estos cinco campos:

- ID
- Título
- Precondiciones
- Pasos
- Resultado esperado

No agregues campos como prioridad, estado o tipo de prueba.
