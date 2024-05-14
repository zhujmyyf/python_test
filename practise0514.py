import RPi.GPIO as GPIO
import time

# 配置GPIO引脚
TEMP_SENSOR_PIN = 4  # 假设温度传感器连接到GPIO 4
HEATER_PIN = 17  # 假设加热器连接到GPIO 17

# 初始化GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TEMP_SENSOR_PIN, GPIO.IN)
GPIO.setup(HEATER_PIN, GPIO.OUT)


# 假设我们使用一个模拟的读取温度传感器的函数
def read_temperature():
    # 实际代码会根据你的传感器类型读取数据
    # 这里我们简单返回一个模拟值
    return 25.0  # 模拟温度值


# 目标温度
TARGET_TEMPERATURE = 22.0

try:
    while True:
        # 读取当前温度
        current_temperature = read_temperature()
        print(f"Current Temperature: {current_temperature}°C")

        # 控制加热器
        if current_temperature < TARGET_TEMPERATURE:
            GPIO.output(HEATER_PIN, GPIO.HIGH)
            print("Heater ON")
        else:
            GPIO.output(HEATER_PIN, GPIO.LOW)
            print("Heater OFF")

        # 每隔1秒读取一次
        time.sleep(1)

except KeyboardInterrupt:
    # 清理GPIO配置
    GPIO.cleanup()
    print("Program terminated")