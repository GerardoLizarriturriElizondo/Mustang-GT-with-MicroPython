import network
import socket
import machine

IN1 = machine.Pin(27, machine.Pin.OUT)
IN2 = machine.Pin(26, machine.Pin.OUT)
ENA = machine.PWM(machine.Pin(14), freq=1000)

IN3 = machine.Pin(33, machine.Pin.OUT)
IN4 = machine.Pin(32, machine.Pin.OUT)
ENB = machine.PWM(machine.Pin(25), freq=1000)

LED_LEFT = machine.Pin(4, machine.Pin.OUT)
LED_RIGHT = machine.Pin(5, machine.Pin.OUT)

MAX_DUTY = 65535

SPEED_SLOW = 0.6
SPEED_FAST = 1.0


def duty_from_factor(factor):
    if factor < 0:
        factor = 0
    if factor > 1:
        factor = 1
    return int(MAX_DUTY * factor)


def leds_off():
    LED_LEFT.off()
    LED_RIGHT.off()


def stop_motors():
    IN1.off()
    IN2.off()
    IN3.off()
    IN4.off()
    ENA.duty_u16(0)
    ENB.duty_u16(0)
    leds_off()


def traction_forward(factor):
    IN3.on()
    IN4.off()
    ENB.duty_u16(duty_from_factor(factor))


def traction_backward(factor):
    IN3.off()
    IN4.on()
    ENB.duty_u16(duty_from_factor(factor))


def traction_stop():
    IN3.off()
    IN4.off()
    ENB.duty_u16(0)


def steer_left(factor):
    IN1.on()
    IN2.off()
    ENA.duty_u16(duty_from_factor(factor))


def steer_right(factor):
    IN1.off()
    IN2.on()
    ENA.duty_u16(duty_from_factor(factor))


def steer_center_off():
    IN1.off()
    IN2.off()
    ENA.duty_u16(0)


def move_forward_slow():
    steer_center_off()
    leds_off()
    traction_forward(SPEED_SLOW)


def move_forward_fast():
    steer_center_off()
    leds_off()
    traction_forward(SPEED_FAST)


def move_backward():
    steer_center_off()
    leds_off()
    traction_backward(SPEED_SLOW)


def turn_left():
    LED_LEFT.on()
    LED_RIGHT.off()
    steer_left(SPEED_FAST)
    traction_forward(SPEED_FAST)


def turn_right():
    LED_RIGHT.on()
    LED_LEFT.off()
    steer_right(SPEED_FAST)
    traction_forward(SPEED_FAST)


stop_motors()

HTML = """HTTP/1.1 200 OK\r
Content-Type: text/html\r
Connection: close\r
\r
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>ESP32 Car</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; }
    h1 { margin-top: 20px; }
    .btn {
      display: inline-block;
      padding: 10px 18px;
      margin: 6px;
      font-size: 16px;
      text-decoration: none;
      border-radius: 8px;
      border: 1px solid #333;
    }
    .fwd1 { background:#a5ffb5; }
    .fwd2 { background:#7bff90; }
    .back { background:#ffb5b5; }
    .stop { background:#ffe4a5; }
    .left { background:#b5d9ff; }
    .right { background:#b5d9ff; }
  </style>
</head>
<body>
  <h1>ESP32 Car Control</h1>

  <h2>Adelante</h2>
  <div>
    <a class="btn fwd1" href="/?cmd=fwd1">Lento</a>
    <a class="btn fwd2" href="/?cmd=fwd2">Rápido</a>
  </div>

  <h2>Dirección (Turbo)</h2>
  <div>
    <a class="btn left" href="/?cmd=left">Izquierda</a>
    <a class="btn right" href="/?cmd=right">Derecha</a>
  </div>

  <h2>Otros</h2>
  <div>
    <a class="btn back" href="/?cmd=back">Atrás</a>
    <a class="btn stop" href="/?cmd=stop">Stop</a>
  </div>

  <p>Conéctate a la red WiFi <b>ESP32-CAR</b> y entra a <b>http://192.168.4.1/</b></p>
</body>
</html>
"""

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32-CAR', password='12345678', authmode=network.AUTH_WPA_WPA2_PSK)

print("AP encendido")
print("SSID: ESP32-CAR")
print("PASS: 12345678")
print("IP:", ap.ifconfig()[0])

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Servidor escuchando en puerto 80...")

while True:
    try:
        cl, addr = s.accept()
        request = cl.recv(1024)
        request = request.decode('utf-8')
        first_line = request.split('\r\n')[0]
        parts = first_line.split(' ')
        path = parts[1] if len(parts) > 1 else "/"
        cmd = None
        if "/?cmd=" in path:
            cmd = path.split("/?cmd=")[1]
            if "&" in cmd:
                cmd = cmd.split("&")[0]
        if cmd is not None:
            cmd = cmd.lower()
            print("Comando recibido:", cmd)
            if cmd == "fwd1":
                move_forward_slow()
            elif cmd == "fwd2":
                move_forward_fast()
            elif cmd == "back":
                move_backward()
            elif cmd == "left":
                turn_left()
            elif cmd == "right":
                turn_right()
            elif cmd == "stop":
                stop_motors()
        cl.sendall(HTML)
        cl.close()
    except Exception as e:
        print("Error en servidor:", e)
        try:
            cl.close()
        except:
            pass
