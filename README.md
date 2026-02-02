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
│   ├── menu_gestion_puertos.py
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
- **Validaciones**: Control estricto de capacidad máxima de contenedores para evitar sobrecarga.

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

El sistema utiliza **JSON** para guardar el estado completo entre ejecuciones. Dado que JSON no soporta objetos complejos (instancias de clases) nativamente, se implementó una estrategia de serialización manual:

### Estrategia de Serialización (`to_dict`)
Cada clase del sistema (`Puerto`, `Contenedor`, `Producto`) cuenta con un método `to_dict()` que convierte sus atributos en un diccionario estándar de Python.
- **Recursividad**: La conversión es recursiva. Al guardar un puerto, este invoca `to_dict()` en sus contenedores, y cada contenedor invoca `to_dict()` en sus productos.
- **Carga de Datos**: El proceso inverso ocurre al iniciar el programa. El repositorio lee el JSON y reconstruye los objetos instanciando las clases con los datos del diccionario.

### Clase `RepositorioPuertos` (`src/repositorios/repositorios_puerto.py`)
Esta clase maneja toda la lógica de entrada/salida:
1.  **Guardado (`guardar`)**: Se ejecuta al cerrar una sesión o realizar cambios importantes, transformando la lista de objetos `Puerto` actual a JSON.
2.  **Carga (`cargar`)**: Se ejecuta al iniciar el programa para restaurar el estado anterior.
3.  **Seguridad (`security_check`)**:
    - Si el archivo JSON no existe (primera ejecución) o está corrupto, se activa `security_check()`.
    - Esta función **crea automáticamente un puerto por defecto** ("Puerto de San Antonio") con un contenedor y productos de muestra.
    - Esto asegura que el programa **nunca falle al iniciar**, garantizando continuidad y permitiendo al usuario empezar a trabajar de inmediato sin configuraciones manuales previas.
- **Compatibilidad**: Maneja la conversión automática entre el sistema de objetos y el formato de archivo.

---

## ✨ Funcionalidades Implementadas

1.  **Gestión de Puertos**:
    - Ver lista de puertos con formato de tabla.
    - **Agregar Puerto**:
        - Validación de país costero.
        - **Explicación UI**: Instrucciones claras sobre los requisitos de ubicación.
        - Definición de límite máximo de contenedores.
    - **Eliminar Puerto**:
        - Filtro de búsqueda por ubicación.
        - UI mejorada para evitar errores.

2.  **Gestión de Contenedores**:
    - Ver contenedores de un puerto (ID, Tipo, Peso Max, **Peso Actual**).
    - **Agregar Contenedor**: 
        - Generación automática o manual.
        - Validación de capacidad del puerto (impide agregar si está lleno).
    - **Modificar Contenedor**:
        - Acceder a un contenedor específico.
        - **Carga Masiva Inteligente**: Agregar X productos aleatorios.
        - **Eliminación Aleatoria**: Funcionalidad para eliminar productos al azar del contenedor.
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
