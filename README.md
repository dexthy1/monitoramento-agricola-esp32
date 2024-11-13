README.TXT

### Objetivo do Projeto
Este projeto visa desenvolver um **sistema de monitoramento inteligente para agricultura** utilizando o microcontrolador **ESP32** e quatro tipos de sensores: **DHT22** (temperatura e umidade), **HC-SR04** (nível de líquido), **PIR** (movimento) e **LDR** (luminosidade). O sistema foi projetado para ajudar a otimizar o uso dos recursos hídricos, monitorar condições climáticas e melhorar a segurança da área monitorada. Utilizando o ESP32, o sistema coleta dados do ambiente e toma decisões automatizadas, como o controle da irrigação e a detecção de presença de intrusos.

### Funcionalidades do Sistema
1. **Monitoramento Climático**: Mede a temperatura e a umidade do ambiente para garantir que o clima está adequado para o crescimento das plantas.
2. **Controle de Irrigação Automatizado**: Verifica o nível de água no reservatório e aciona a irrigação de acordo com a necessidade.
3. **Detecção de Presença**: Detecta intrusos ou animais na área monitorada para aumentar a segurança do local.
4. **Ajuste de Irrigação com Base na Luminosidade**: Ajusta a irrigação conforme a quantidade de luz solar, evitando o desperdício de água.

### Como Configurar e Rodar o Projeto no Wokwi
1. **Acesse o Wokwi**:
   - Acesse o site do Wokwi: [https://wokwi.com/](https://wokwi.com/).
   - Clique em "New Project" e escolha a placa **ESP32**.

2. **Adicionar os Componentes**:
   - No editor de circuitos do Wokwi, adicione os seguintes componentes:
     - **ESP32**: Componente principal para o controle do sistema.
     - **DHT22**: Sensor de temperatura e umidade.
     - **HC-SR04**: Sensor de ultrassom para medir o nível de líquido.
     - **PIR**: Sensor de movimento para detectar presença.
     - **LDR**: Sensor de luz para monitorar a intensidade da luz solar.

3. **Conectar os Componentes**:
   - Conecte os sensores ao ESP32 de acordo com as especificações do projeto. Por exemplo:
     - **DHT22** no pino GPIO 15.
     - **HC-SR04**: `Trig` no GPIO 5 e `Echo` no GPIO 18.
     - **PIR** no GPIO 13.
     - **LDR** conectado ao ADC (GPIO 34).

4. **Inserir o Código**:
   - No editor do Wokwi, cole o código fornecido do projeto, que contém as leituras dos sensores e a lógica de controle da irrigação e segurança.

5. **Iniciar a Simulação**:
   - Clique em "Start Simulation" para iniciar o projeto e verificar o comportamento do sistema.

### Instalação das Dependências
- **Python**: Certifique-se de ter o **Python** instalado em sua máquina. Você precisará dele para instalar o firmware do MicroPython.
- **esptool.py**: Ferramenta usada para instalar o firmware no ESP32. Instale com o comando:
  ```sh
  pip install esptool
  ```
- **Firmware do MicroPython**:
  - Baixe o firmware do site oficial: [https://micropython.org/download/esp32/](https://micropython.org/download/esp32/).
  - Utilize o `esptool.py` para gravar o firmware no ESP32:
    ```sh
    esptool.py --port COMx erase_flash
    esptool.py --port COMx write_flash -z 0x1000 esp32-x.x.x.bin
    ```
    (Substitua `COMx` pela porta correta e `esp32-x.x.x.bin` pelo nome do arquivo de firmware que você baixou.)

### Instruções Detalhadas para Cada Parte do Projeto
1. **Leitura do Sensor DHT22**:
   - O sensor **DHT22** é usado para medir a **temperatura e umidade** do ambiente. Essas informações são importantes para ajustar a irrigação, garantindo que as plantas recebam água quando a umidade estiver baixa.

2. **Medição de Nível de Líquido (HC-SR04)**:
   - O sensor **HC-SR04** é um sensor de ultrassom que mede a **distância** até a superfície do líquido no reservatório. Assim, o sistema sabe quando é necessário reabastecer o reservatório de água para manter a irrigação funcionando.

3. **Detecção de Presença (PIR)**:
   - O sensor **PIR** é usado para detectar **movimento** na área monitorada. Ele é útil para aumentar a segurança da fazenda, alertando sobre a presença de pessoas ou animais que possam causar danos à plantação.

4. **Monitoramento de Luminosidade (LDR)**:
   - O sensor **LDR** é usado para medir a **intensidade da luz solar**. Com base nesses dados, o sistema ajusta a quantidade de água fornecida às plantas. Dias mais ensolarados podem precisar de menos irrigação, enquanto dias nublados podem exigir mais.

5. **Controle do Sistema via ESP32**:
   - O **ESP32** é o microcontrolador que integra todos os sensores e executa o código para processar as leituras e tomar decisões automatizadas sobre a irrigação e segurança.

6. **Ciclo de Funcionamento**:
   - O código é executado em um loop infinito, onde os sensores são lidos constantemente e as decisões são tomadas com base nas condições do ambiente.

### Observações Finais
- **Segurança**: Tenha cuidado ao manusear componentes elétricos e ao ligar o ESP32 a fontes de energia.
- **Ajustes**: Caso o sistema não esteja se comportando como esperado, verifique a conexão dos pinos no Wokwi e certifique-se de que o código esteja devidamente adaptado para os componentes utilizados.

Este projeto é uma forma de mostrar como o uso de sensores e microcontroladores pode tornar o cultivo agrícola mais eficiente e menos dependente de intervenções humanas, promovendo um uso mais sustentável dos recursos. Boa sorte na sua implementação e simulação!
