#!/usr/bin/env python3
"""Valida la estructura sencilla de un documento Markdown de casos de prueba."""

import re
import sys
from pathlib import Path


CASE_HEADING = re.compile(r"^##\s+(TC-\d{3})\s+[—-]\s*(.*)$")
STEP = re.compile(r"^\s*\d+\.\s+\S.*$")
TEMPLATE_MARKERS = re.compile(
    r"\[(?:NOMBRE DE LA FUNCIONALIDAD|TÍTULO DEL CASO|PRECONDICIÓN[^\]]*|"
    r"PASO CONCRETO|RESULTADO OBSERVABLE)\]",
    re.IGNORECASE,
)
FIELDS = ("Precondiciones", "Pasos", "Resultado esperado")


def parse_cases(lines):
    cases = []
    current = None
    invalid_headings = []

    for line in lines:
        heading = CASE_HEADING.match(line)
        if heading:
            current = {
                "id": heading.group(1),
                "title": heading.group(2).strip(),
                "fields": {},
                "content": [line],
            }
            cases.append(current)
            continue

        if re.match(r"^##\s+TC-", line):
            invalid_headings.append(line.strip())
            current = None
            continue

        field_match = re.match(r"^\*\*(.+?)\*\*\s*$", line)
        if current and field_match and field_match.group(1) in FIELDS:
            current["active_field"] = field_match.group(1)
            current["fields"].setdefault(field_match.group(1), [])
            continue

        if current and current.get("active_field"):
            current["fields"][current["active_field"]].append(line)

        if current:
            current["content"].append(line)

    return cases, invalid_headings


def validate(path):
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"[FAIL] No se pudo leer el archivo: {error}")
        print("\nValidación fallida.")
        return 1

    lines = text.splitlines()
    cases, invalid_headings = parse_cases(lines)
    errors = []

    for heading in invalid_headings:
        errors.append(f"Encabezado de caso con formato de ID inválido: {heading}")

    if not cases:
        errors.append("No se detectaron casos de prueba")

    seen_ids = set()
    for case in cases:
        case_id = case["id"]
        if case_id in seen_ids:
            errors.append(f"ID duplicado: {case_id}")
        seen_ids.add(case_id)

        if not case["title"]:
            errors.append(f"{case_id} no contiene título")

        fields = case["fields"]
        for field in FIELDS:
            if field not in fields:
                label = "resultado esperado" if field == "Resultado esperado" else field.lower()
                errors.append(f"{case_id} no contiene {label}")
            elif not "".join(fields[field]).strip():
                label = "resultado esperado" if field == "Resultado esperado" else field.lower()
                errors.append(f"{case_id} no contiene contenido en {label}")

        steps = fields.get("Pasos", [])
        if not any(STEP.match(line) for line in steps):
            errors.append(f"{case_id} no contiene un paso numerado válido")

    for case in cases:
        if TEMPLATE_MARKERS.search("\n".join(case["content"])):
            errors.append(f"{case['id']} contiene marcadores de plantilla sin reemplazar")

    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        print("\nValidación fallida.")
        return 1

    print("[PASS] Casos de prueba detectados")
    print("[PASS] IDs únicos")
    print("[PASS] Campos obligatorios completos")
    print("[PASS] Pasos detectados")
    print("[PASS] Resultados esperados detectados")
    print("\nValidación exitosa.")
    return 0


def main():
    if len(sys.argv) != 2:
        print(
            "Uso: python validate_test_cases.py <archivo.md>",
            file=sys.stderr,
        )
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"[FAIL] El archivo no existe o no es un archivo: {path}")
        print("\nValidación fallida.")
        return 1

    return validate(path)


if __name__ == "__main__":
    raise SystemExit(main())
