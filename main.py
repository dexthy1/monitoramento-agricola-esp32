import machine
import time
from dht import DHT22

# Configuração dos pinos dos sensores
# No Wokwi, os pinos geralmente precisam ser configurados conforme o mapeamento da simulação
dht_pin = machine.Pin(15)  # Utilize o pino conforme configurado no Wokwi
dht_sensor = DHT22(dht_pin)

pir_pin = machine.Pin(13, machine.Pin.IN)
ldr_pin = machine.ADC(machine.Pin(34))
ldr_pin.atten(machine.ADC.ATTN_11DB)  # Aumenta o range para 0-3.3V

hc_trig = machine.Pin(5, machine.Pin.OUT)
hc_echo = machine.Pin(18, machine.Pin.IN)


def read_dht():
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        print(f"Temperatura: {temp}°C, Umidade: {humidity}%")
        return temp, humidity
    except Exception as e:
        print("Erro ao ler DHT22:", e)
        return None, None


def read_pir():
    return pir_pin.value()


def read_ldr():
    return ldr_pin.read()


def read_hcsr04():
    # Controlando Trigger do Ultrassônico
    hc_trig.off()
    time.sleep_us(2)
    hc_trig.on()
    time.sleep_us(10)
    hc_trig.off()

    # Medindo o tempo de resposta
    while hc_echo.value() == 0:
        pass
    start = time.ticks_us()

    while hc_echo.value() == 1:
        pass
    end = time.ticks_us()

    # Calculando a distância com base no tempo medido
    distance = (time.ticks_diff(end, start)) * 0.0343 / 2
    return distance


while True:
    # Leitura dos Sensores
    temp, humidity = read_dht()
    if temp is not None and humidity is not None:
        pir = read_pir()
        ldr = read_ldr()
        distance = read_hcsr04()

        # Imprimindo os resultados no console
        print(f"Movimento: {'Detectado' if pir else 'Não Detectado'}")
        print(f"Luminosidade: {ldr}")
        print(f"Distância: {distance:.2f} cm")

    # Espera antes da próxima leitura
    time.sleep(2)
