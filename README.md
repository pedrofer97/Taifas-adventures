# 🐱 Taifa's Adventures: Mercado Medieval

¡Bienvenido a **Taifa's Adventures**! Un emocionante juego de arcade desarrollado en Python donde encarnas a Taifa, una gata muy audaz que debe recolectar tesoros en un bullicioso mercado medieval mientras esquiva a una banda de ratones ladrones.

## 📜 Historia del Juego
En el corazón del reino, el mercado de las Taifas es famoso por sus objetos valiosos. Taifa tiene la misión de recolectar aceitunas, espárragos, lentejas y otros tesoros para llenar su cesta. Pero cuidado: los ratones del mercado no descansan y tratarán de robarle todo lo que consiga. ¡Si recolectas 10 tesoros, Taifa desbloqueará sus poderes de **Hechicera**!

## 🎮 Características Principales
- **Mecánica de Recolección:** Encuentra los objetos que aparecen aleatoriamente y llévalos a la cesta para puntuar.
- **Sistema de Energía:** Taifa se cansa al moverse. Si su energía llega a cero, ¡se quedará dormida (Zzz...) y tendrás que esperar a que descanse!
- **Power-ups:** Busca las pociones mágicas para recuperar tu energía al instante.
- **Evolución de Personaje:** Al llegar a los 10 puntos, Taifa se transforma en Hechicera, cambiando su aspecto y enfrentándose al temible **Ratón Jefe**.
- **Dificultad Dinámica:** Los ratones aparecen progresivamente para complicar tu misión.

## ⌨️ Controles
| Acción | Tecla |
| :--- | :--- |
| **Movimiento** | `W`, `A`, `S`, `D` |
| **Navegar Menús** | `Espacio` |
| **Cerrar Juego** | `Esc` o cerrar ventana |

## 🛠️ Conceptos de Programación Aplicados (POO)
Este proyecto ha sido desarrollado aplicando principios avanzados de **Programación Orientada a Objetos**:
- **Encapsulamiento:** Uso de atributos privados (ej. `__energia`, `__velocidad`) y decoradores `@property` (Getters y Setters) para proteger la lógica del personaje.
- **Herencia y Polimorfismo:** Los enemigos comparten una base, pero el `RatonJefe` utiliza un método de movimiento inteligente diferente al de los ratones comunes.
- **Gestión de Estados:** Implementación de un ciclo de juego con estados diferenciados (MENU, REGLAS, JUEGO, RESULTADOS).

## 🚀 Requisitos e Instalación
Para jugar a Taifa's Adventures, necesitas tener instalado **Python** y la librería **Pygame**.

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/pedrofer97/Taifas-adventures.git](https://github.com/pedrofer97/Taifas-adventures.git)

  
2. **Instala las dependencias:**
   ```bash
   pip install pygame

3. **Ejecuta el juego:**
   ```bash
   python main.py

4. **📂 Estructura de Archivos
  main.py: Lógica principal y bucle del juego.
  jugador.py: Clase PersonajeTaifa con lógica de movimiento y energía.
  enemigo.py: Lógica de los ratones y el Jefe.
  assets/: Carpeta con todos los recursos visuales, sonidos y fuentes.

Desarrollado con ❤️ por pedrofer97
