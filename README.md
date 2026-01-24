# 🚢 Sistema de Gestión Portuaria (Python)

Bienvenido al **Sistema de Gestión Portuaria**, una aplicación de consola robusta diseñada en Python utilizando **Programación Orientada a Objetos (POO)**. Este sistema permite administrar puertos, contenedores y cargas de manera eficiente, con persistencia de datos y una interfaz de usuario amigable.

## 📂 Estructura del Proyecto

El proyecto está organizado modularmente para facilitar la escalabilidad y el mantenimiento:

```
src/
├── clases/          # Definición de modelos de datos (POO)
│   ├── contenedor.py
│   ├── puertos.py
│   ├── productos.py
│   └── ...
├── data/            # Almacenamiento de datos persistentes
│   └── puertos.json
├── modulos/         # Lógica de menús y flujos de usuario
│   ├── menu.py
│   ├── menu_puertos.py
│   ├── menu_contenedor.py
│   └── config.py
├── repositorios/    # Capa de acceso a datos (Persistencia)
│   └── repositorios_puerto.py
├── utils/           # Herramientas transversales
│   ├── decoradores.py
│   ├── generadores.py
│   └── validadores.py
└── main.py          # Punto de entrada de la aplicación
```

---

## 🏗 Arquitectura y POO

El sistema se basa en clases que representan las entidades del negocio:

### 1. `Puerto` (`src/clases/puertos.py`)
- Representa un puerto marítimo.
- **Atributos**: Nombre, Ubicación (validada contra lista de países costeros), Capacidad Máxima y Lista de Contenedores.
- **Métodos**: `agregar_contenedor()`, `to_dict()`.

### 2. `Contenedor` (`src/clases/contenedor.py`)
- Representa un contenedor de carga.
- **Tipos soportados**: Refrigerado, Seco, OpenTop.
- **Optimización de Carga**: 
  - La carga se gestiona internamente como un **diccionario** para agrupar productos repetidos (ej. `200x Manzana`), lo que optimiza la memoria y la visualización.
  - Calcula automáticamente el peso actual.
- **Validaciones**:
  - Verifica **Tipos de Producto** (ej. Alimentos que requieren frío solo van en Refrigerado).
  - Verifica **Peso Máximo** (100,000 kg).

### 3. `Producto` y Subclases (`src/clases/productos.py`)
- **Herencia**:
  - `Producto` (Clase Padre): Nombre, Peso, Precio.
  - `Alimento`: Agrega `requiere_frio`.
  - `Tecnologia`: Agrega `marca`.
  - `Vehiculo`: Agrega `marca` y `año`.

---

## 🛠 Utilidades y Herramientas

### ✅ Validadores (`src/utils/validadores.py`)
- `verificar_input_entero()`: Asegura que el usuario ingrese números válidos dentro de un rango.
- `verificar_pais_costeros()`: Valida si una ubicación corresponde a un país costero permitido.

### 🎨 Decoradores (`src/utils/decoradores.py`)
Mejoran la experiencia de usuario (UX):
- `titulo_menu(texto)`: Estandariza los encabezados de todos los menús.
- `cambio_de_pagina()`: Simula limpieza de pantalla y transiciones suaves.
- `despedida_programa()`: Mensaje de cierre amigable.

### 🎲 Generadores (`src/utils/generadores.py`)
- `generar_producto_general()`: Crea productos aleatorios (Alimento, Tecnología o Vehículo) con datos realistas.
- `generar_contenedor_random()`: Crea contenedores con IDs y tipos aleatorios para pruebas rápidas.

---

## 💾 Persistencia de Datos

El sistema utiliza **JSON** para guardar el estado completo entre ejecuciones:

- **Repositorio** (`src/repositorios/repositorios_puerto.py`):
    - Se encarga de **Cargar** datos desde `data/puertos.json`.
    - Transforma los diccionarios JSON nuevamente en objetos Python (`Puerto`, `Contenedor`, `Producto`).
    - Se encarga de **Guardar** los objetos actuales en el archivo JSON.
- **Compatibilidad**: Maneja la conversión automática entre el sistema de objetos y el formato de archivo.

---

## ✨ Funcionalidades Implementadas

1.  **Gestión de Puertos**:
    - Ver lista de puertos con formato de tabla.
    - Agregar nuevos puertos (con validación de país).
    - Eliminar puertos (con filtro de búsqueda por ubicación).

2.  **Gestión de Contenedores**:
    - Ver contenedores de un puerto (ID, Tipo, Peso Max, **Peso Actual**).
    - **Agregar Contenedor**: Generación automática o manual.
    - **Modificar Contenedor**:
        - Acceder a un contenedor específico.
        - **Carga Masiva Inteligente**: Agregar X productos aleatorios.
        - El sistema intenta llenar el contenedor hasta que se llene o ocurra un error de validación, sin detenerse por un solo fallo.
    - Eliminar Contenedor.

3.  **Interfaz de Usuario (UI) Premium**:
    - Diseño consistente en toda la aplicación.
    - Tablas alineadas.
    - Mensajes de error y éxito claros (con emojis ⚠, ✅, ❌).
    - Tiempos de espera (`sleep`) para mejorar la legibilidad.

---

## 🚀 Cómo Ejecutar

Requiere **Python 3**.

1. Abre la terminal en la carpeta raíz.
2. Ejecuta:
   ```bash
   python src/main.py
   ```
