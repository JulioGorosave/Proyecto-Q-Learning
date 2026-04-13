# Conecta 4 con Q-Learning

Este proyecto implementa un agente inteligente que aprende a jugar Conecta 4 utilizando el algoritmo de Q-Learning.

## Características
- Interfaz gráfica con Tkinter
- Entrenamiento automático
- Niveles de dificultad
- Persistencia de aprendizaje (Q-table)

---

## Estructura del proyecto

- **main.py** → Contiene la interfaz gráfica del juego y controla la interacción con el usuario.
- **game_logic.py** → Contiene toda la lógica del juego (tablero, movimientos, validaciones y condiciones de victoria).
- **q_learning.py** → Implementa el algoritmo de Q-Learning, el entrenamiento del agente y la toma de decisiones.
- **q_table.pkl** → Archivo donde se almacena el aprendizaje de la IA (se genera automáticamente después del entrenamiento).

---

## ¿Cómo ejecutar el programa?

### 1. Instalar dependencias
Asegúrate de tener instalada la librería necesaria y ejecuta el archivo "main.py":

```bash
pip install numpy
