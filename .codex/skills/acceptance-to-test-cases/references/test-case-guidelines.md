# Guía breve para escribir casos de prueba

- Cada caso debe comprobar un escenario concreto y describir un resultado que se pueda observar.
- **Precondiciones:** indica qué debe cumplirse antes de empezar. Si no hace falta ninguna, escribe `Ninguna`.
- **Pasos:** enumera en orden acciones concretas que otra persona pueda seguir.
- **Resultado esperado:** describe qué debería observarse después de los pasos; evita opiniones o expresiones vagas.
- El resultado esperado no debe limitarse a reformular el requisito o la acción realizada. Debe indicar una consecuencia observable que permita determinar si el caso pasó o falló. Si el requisito no proporciona esa evidencia y definirla exigiría asumir comportamiento no especificado, solicita una aclaración.
- No inventes reglas de negocio ni completes detalles ausentes del requisito. Esto incluye, por ejemplo, reglas de coincidencia, filtros, ordenamiento, validaciones, límites, mensajes, estados, cantidades, permisos y comportamientos de error; estos ejemplos no implican que siempre haya que preguntar por ellos.
- Pregunta únicamente cuando un dato ausente sea necesario para determinar el resultado esperado verificable del caso. Si no es necesario, no preguntes ni lo supongas: omite los casos que dependan de ese dato y redacta los casos independientes que sí sean verificables.
- El código del proyecto aporta contexto para localizar la funcionalidad, pero no demuestra cuál debería ser el comportamiento requerido ni completa reglas ausentes.
- Si una funcionalidad solicitada no se encuentra en el código actual, no asumas que existe ni que se trata de una funcionalidad futura. Informa al usuario y confirma si desea continuar diseñando los casos a partir de un requisito futuro antes de redactarlos.
- Si solo parte de una funcionalidad tiene evidencia, distingue las partes encontradas de las no encontradas; no generes casos para las partes sin evidencia hasta confirmar que son futuras y no bloquees los casos independientes verificables.
- Los casos existentes no deben sobrescribirse ni modificarse sin confirmación explícita del usuario.
