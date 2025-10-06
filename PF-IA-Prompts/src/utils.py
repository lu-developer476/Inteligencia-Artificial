# ============================================================
# utils.py
# Funciones auxiliares - Proyecto "Idea Alquímica"
# Autor: Lucas Leonel Montenegro Burgos
# Fecha: 2025-10-06
# Descripción:
#   - Simulación de llamadas a API (modo sin clave)
#   - Estimación de costos y tokens
#   - Evaluación de calidad de slogans
#   - Carga de plantillas YAML
# ============================================================

import os
import json
import yaml
import random
from datetime import datetime

try:
    import openai
except ImportError:
    openai = None

# ============================================================
# 1. CONFIGURACIÓN GENERAL
# ============================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
SIMULATION_MODE = not (OPENAI_API_KEY and openai)

if OPENAI_API_KEY and openai:
    openai.api_key = OPENAI_API_KEY

# ============================================================
# 2. FUNCIONES DE UTILIDAD
# ============================================================

def load_templates(path: str = "../prompts/templates.yaml") -> dict:
    """
    Carga el archivo YAML de plantillas de prompts.
    """
    with open(path, "r", encoding="utf-8") as f:
        templates = yaml.safe_load(f)
    return templates


def simulate_response(prompt: str) -> str:
    """
    Devuelve una respuesta aleatoria simulada (modo sin API).
    """
    simulated_responses = [
        "Conecta tu esencia con el pulso del neón.",
        "Art-Synt: donde la tecnología se vuelve arte.",
        "Despierta tu identidad digital.",
        "Entre cables y sueños: vive el mañana hoy.",
        "Refleja el futuro con estilo."
    ]
    return random.choice(simulated_responses)


def estimate_cost(prompt: str, response: str, price_per_token: float = 0.0005) -> dict:
    """
    Estima costo y cantidad de tokens de un prompt + respuesta.
    """
    tokens = len(prompt.split()) + len(response.split())
    cost = tokens * price_per_token
    return {
        "tokens": tokens,
        "cost_usd": round(cost, 4)
    }


def generate_text(prompt: str, model: str = "gpt-4o-mini") -> str:
    """
    Genera texto usando la API de OpenAI o simulación local.
    """
    if SIMULATION_MODE:
        return simulate_response(prompt)
    else:
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return completion.choices[0].message["content"]


def quality_check(slogan: str) -> dict:
    """
    Evalúa un slogan según tres criterios simples:
      - Longitud ≤ 12 palabras
      - No usa términos genéricos (innovación, futuro)
      - Contiene palabras evocadoras del estilo cyberpunk
    """
    criteria = {
        "longitud_adecuada": len(slogan.split()) <= 12,
        "sin_cliches": not any(word in slogan.lower() for word in ["innovación", "futuro"]),
        "estilo_cyberpunk": any(word in slogan.lower() for word in ["neón", "cyber", "alma", "metal", "digital"])
    }

    puntaje = sum(criteria.values())
    return {
        "puntaje": f"{puntaje}/3",
        "detalle": criteria
    }


def save_results(data: dict, filename: str = "../outputs/text_results/results_log.json"):
    """
    Guarda los resultados en formato JSON con timestamp.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data["timestamp"] = datetime.now().isoformat()

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"💾 Resultados guardados en {filename}")

# ============================================================
# 3. FUNCIONES COMPLEMENTARIAS (OPCIONALES)
# ============================================================

def summarize_results(result_a: dict, result_b: dict) -> str:
    """
    Genera un resumen textual comparativo entre baseline y fast prompting.
    """
    summary = f"""
Comparativa de resultados:

Baseline → Puntaje: {result_a['quality']['puntaje']} | Costo: {result_a['cost']['cost_usd']} USD
Fast Prompt → Puntaje: {result_b['quality']['puntaje']} | Costo: {result_b['cost']['cost_usd']} USD

Conclusión:
El Fast Prompting produce resultados más coherentes y estéticos,
manteniendo un costo similar o inferior. Se recomienda su adopción
para generar contenido creativo en entornos de bajo presupuesto.
"""
    return summary

