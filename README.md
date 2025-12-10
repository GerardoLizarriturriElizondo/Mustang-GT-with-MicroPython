# Carrito con ESP32, Puente H L298N y MicroPython

## Integrantes del equipo

- **Gerardo Lizarriturri Elizondo - 2530517**
- **Nahum Azael Hernández Peña - 2530227**
- **Jorge González Cárdenas - 2530260**
- **Isaac Torres Díaz - 2530277**
- **Julián Carmona Báez - 2530059**
- **Esteban Trejo Rodríguez - 2530344**


Proyecto de primer cuatrimestre donde se controla un carrito usando una placa **ESP32**, un puente H **L298N** y dos motores DC de **6 V**:

- Un motor para la **tracción** (avanzar y retroceder).
- Un motor para la **dirección** (giro de las llantas).

El programa está escrito en **MicroPython**, se flashea el firmware con **esptool** y se suben los archivos al ESP32 con **ampy**.




Este proyecto consiste en la construcción de un carrito a escala controlado por una **ESP32** y un puente H **L298N**, que maneja dos motores DC de **6 V**: uno para la **tracción** avanzar y retroceder y otro para la **dirección** giro de las llantas. El control de los motores se realiza mediante salidas digitales y señales PWM.

El código está desarrollado en **MicroPython**, flasheando primero el firmware con **esptool** y cargando los programas al ESP32 con **ampy**. Aunque es un proyecto de primer cuatrimeestre, integra conceptos básicos pero importantes de electrónica y programación embebida, y sirve como base para futuras mejoras como control remoto o sensores adicionales.

# Carrito con ESP32, Puente H L298N y MicroPython

Proyecto de primer semestre donde se controla un carrito usando una placa **ESP32**, un puente H **L298N** y dos motores DC de **6 V**:

- Un motor para la **tracción** (avanzar y retroceder).
- Un motor para la **dirección** (giro de las llantas).

El programa está escrito en **MicroPython**, se flashea el firmware con **esptool** y se suben los archivos al ESP32 con **ampy**.

---

## Objetivo del proyecto

Construir y poner en funcionamiento un carrito controlado con una **ESP32** y un **puente H L298N** que permita:

- Avanzar y retroceder usando un motor DC de 6 V (tracción).
- Girar las llantas usando un segundo motor DC de 6 V (dirección).
- Controlar los motores mediante código en MicroPython.

---

## Alcance

Este proyecto se enfoca en lo esencial:

- Control básico de movimiento: adelante, atrás, giro izquierda/derecha y detenerse.
- Uso de un puente H L298N con una ESP32.
- Manejo sencillo de PWM para controlar la velocidad de los motores.
- Se controla con una interfaz desde el telefono, conectado a internet entre el ESP32 y el celular
---

## Requisitos previos

Para comprender y replicar este proyecto se necesitan conocimientos básicos de:

- Conexión de una **ESP32** a la computadora.
- Uso sencillo de la terminal / consola de comandos.
- Conceptos básicos de:
  - Entradas y salidas digitales.
  - PWM para variar la velocidad de un motor.
  - Funcionamiento general de un puente H (L298N).

---

## Materiales

- 1 × Placa **ESP32** (tipo DevKit)
- 1 × Módulo puente H **L298N**
- 2 × Motores DC **de 6 V**
  - 1 motor de tracción (mueve el carrito hacia adelante/atrás)
  - 1 motor de dirección (gira las llantas)
- 1 × Chasis de carrito con soporte para motores
- 1 × Batería para los motores, por ejemplo:
  - 4 pilas AA (≈ 6 V), o
  - otro pack que entregue alrededor de 6–7 V para los motores
- Cables jumpers macho–macho / macho–hembra
- 1 × Cable USB para programar el ESP32

---

## Software utilizado

En la computadora:

- **Python**
- Firmware de **MicroPython para ESP32** (`micropython-esp32.bin`)
- Herramientas de línea de comandos:
  - `esptool` → para flashear MicroPython en el ESP32
  - `ampy` → para subir los archivos `.py` al ESP32
- Editor de código:
  - VS Code, Thonny o similar

En la tarjeta:

- **ESP32** con **MicroPython**

