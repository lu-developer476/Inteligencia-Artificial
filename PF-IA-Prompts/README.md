# Idea Alquímica: Tejiendo el Futuro con Prompt Engineering

1. Descripción breve

Este proyecto explora cómo aplicar técnicas de Fast Prompting para generar textos e imágenes de calidad utilizando IA, reduciendo costos y mejorando consistencia. Se implementa en Jupyter Notebook con un caso de uso concreto: la tienda virtual Art-Synt.

2. Estructura

notebooks/: Notebook con pruebas baseline vs fast prompting.

prompts/: Plantillas de prompts YAML.

src/: Código auxiliar (simulación + cálculo de costos).

outputs/: Resultados de ejecución (texto + imágenes).

3. Instalación
git clone https://github.com/tuusuario/PF-IA-Prompts.git
cd PF-IA-Prompts
pip install -r requirements.txt

4. Ejecución
jupyter notebook notebooks/fast_prompting_poc.ipynb

(Funciona en modo simulación sin claves API. Se puede usar OpenAI API real, configurando el OPENAI_API_KEY)

5. Resultados

5 prompts de texto → slogans cyberpunk

5 prompts de imagen → afiches estilo Art-Synt

Comparativa baseline vs fast prompting (mejor calidad + menor costo)

6. Tecnologías

Python 3.10+

Jupyter Notebook

OpenAI API (texto)

Stable Diffusion / Leonardo.AI / NightCafe (imágenes)

7. Licencia

(Opcional, MIT recomendado)
