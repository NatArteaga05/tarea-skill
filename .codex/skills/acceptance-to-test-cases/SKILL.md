---
name: acceptance-to-test-cases
description: Convierte un requisito o una funcionalidad descrita en lenguaje natural en casos de prueba manuales, estructurados y verificables para este proyecto. Úsala cuando se pidan casos o escenarios de prueba a partir de un requisito. No la uses para implementar o corregir código, diagnosticar fallos ni ejecutar pruebas.
---

# Generar casos de prueba desde requisitos

Convierte el requisito proporcionado por el usuario en uno o más casos de prueba manuales. Guarda el documento Markdown dentro de `test-cases/` en la raíz del proyecto y no modifiques el código de la aplicación.

## Cuándo usar esta skill

Úsala cuando el usuario proporcione un requisito o una funcionalidad en lenguaje natural y pida casos o escenarios para comprobarla.

No la uses para implementar o corregir la funcionalidad, diagnosticar un fallo, ejecutar pruebas, crear reportes de errores o documentar una funcionalidad sin casos de prueba.

## Procedimiento

1. Toma como entrada el requisito o la funcionalidad que proporcione el usuario. Si no proporciona ninguno, pídeselo.
2. Analiza únicamente los archivos del repositorio que sean pertinentes para entender el contexto del requisito. No inspecciones áreas no relacionadas.
3. Usa el código solo como contexto para identificar componentes, campos, rutas y términos relevantes, y para determinar si la funcionalidad solicitada existe actualmente en el proyecto. El código no es fuente para completar requisitos ni inferir reglas de negocio ausentes.
4. Lee `references/test-case-guidelines.md` antes de decidir los escenarios y redactar los casos.
5. Antes de redactar, distingue qué comportamientos están explícitos en el requisito y qué información faltante es necesaria para establecer un resultado esperado verificable:
   - Usa la información explícita y no vuelvas a preguntarla. Interpreta el alcance expresado de forma completa; por ejemplo, «por nombre y descripción» especifica ambos campos de búsqueda.
   - Si falta información necesaria para el resultado esperado de un caso, pide únicamente la aclaración necesaria antes de generar ese caso. No bloquees los casos independientes que sí puedan redactarse sin esa información.
   - Si el detalle ausente no es necesario para los casos que pueden generarse, no preguntes por él, no lo asumas y evita los casos que dependan de ese detalle.
   - No infieras comportamientos ausentes sobre coincidencias, filtros, ordenamiento, validaciones, límites, mensajes, estados, cantidades, permisos, reglas de negocio ni errores. Esta lista orienta qué no asumir; no exige preguntar por cada elemento.
   - No uses como resultado esperado una simple reformulación del requisito o de la acción ejecutada. El resultado debe contener una consecuencia observable que permita determinar si el caso pasó o falló; si esa consecuencia no está definida y no puede establecerse sin inventar comportamiento, pide una aclaración.
6. Si el análisis pertinente no encuentra evidencia de la funcionalidad solicitada en el código actual del proyecto, informa al usuario que no se encontró información o implementación relacionada y detente antes de generar los casos. Pregunta si se trata de una funcionalidad futura que aún no está implementada y si desea continuar con la creación de los casos de prueba a partir del requisito proporcionado.
   - Si el requisito incluye varios comportamientos y solo algunos tienen evidencia, informa cuáles encontraste y cuáles no. No trates toda la funcionalidad como inexistente ni asumas que la parte sin evidencia funciona; pregunta si desea incluir esa parte como funcionalidad futura y no generes casos para ella hasta recibir confirmación. Genera los casos independientes de la parte existente si son verificables, sin bloquearlos innecesariamente.
   - No asumas por tu cuenta que se trata de una funcionalidad futura.
   - No generes los casos hasta que el usuario confirme que desea continuar.
   - Si el usuario confirma que es una funcionalidad futura, utiliza el requisito proporcionado como fuente del comportamiento esperado, sin inventar detalles a partir del código.
   - Si después de la confirmación todavía falta información necesaria para obtener resultados esperados verificables, solicita únicamente las aclaraciones necesarias antes de generar los casos.
   - Si el usuario no desea continuar, no generes ningún caso.
7. Determina el nombre de archivo correspondiente a la funcionalidad y comprueba si ya existe en `test-cases/` antes de escribir o modificar cualquier archivo. Si no existe, continúa con el flujo normal. Si existe, no lo sobrescribas ni modifiques todavía: informa al usuario y pregunta qué desea hacer: reemplazar los casos, actualizar los casos existentes o conservarlos sin cambios.
   - **Reemplazar:** vuelve a generar el documento utilizando el requisito actual y sustituye el archivo existente solo después de la confirmación explícita del usuario.
   - **Actualizar:** revisa los casos existentes, conserva los que sigan siendo válidos y modifica o agrega únicamente lo necesario según el nuevo requisito, sin inventar comportamientos no especificados.
   - **Conservar:** no realices ningún cambio en el archivo ni vuelvas a validarlo.
8. Usa `assets/test-case-template.md` como estructura del documento generado. Completa y repite el bloque de caso de la plantilla cuando haya varios casos; no agregues campos.
9. Asigna IDs consecutivos desde `TC-001` (`TC-002`, `TC-003`, etc.). Al actualizar, conserva los IDs de los casos existentes que mantengas y asigna IDs consecutivos nuevos a los casos agregados, sin duplicarlos.
10. Crea la carpeta `test-cases/` en la raíz del proyecto si no existe.
11. Guarda o actualiza el documento en `test-cases/<nombre-funcionalidad>.md`. El nombre debe describir brevemente la funcionalidad, usando solo minúsculas y guiones para separar palabras; por ejemplo, `test-cases/busqueda-productos.md`.
12. Ejecuta `.codex/skills/acceptance-to-test-cases/scripts/validate_test_cases.py` sobre el archivo creado, reemplazado o actualizado. Si informa errores, corrige el documento y vuelve a validarlo antes de entregarlo.
13. Informa la ruta del archivo y el resultado de la validación. No afirmes que los casos fueron ejecutados ni que la funcionalidad pasó o falló: esta skill diseña y valida la estructura de los casos, no los ejecuta contra la aplicación.

## Formato obligatorio

Cada caso contiene exactamente estos cinco campos:

- ID
- Título
- Precondiciones
- Pasos
- Resultado esperado

No agregues campos como prioridad, estado o tipo de prueba.
