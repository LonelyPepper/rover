hummingbird.start_hummingbird()

def on_forever():
    if hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE) < 20:
        hummingbird.set_rotation_servo(FourPort.ONE, 0)
        hummingbird.set_rotation_servo(FourPort.TWO, 0)
        hummingbird.set_tri_led(TwoPort.ONE, 100, 0, 0)
        hummingbird.set_tri_led(TwoPort.TWO, 100, 0, 0)
        basic.pause(700)
        hummingbird.set_rotation_servo(FourPort.ONE, 50)
        hummingbird.set_rotation_servo(FourPort.TWO, 50)
        basic.pause(2500)
    else:
        hummingbird.set_rotation_servo(FourPort.ONE, 100)
        hummingbird.set_rotation_servo(FourPort.TWO, -100)
        hummingbird.set_tri_led(TwoPort.ONE, 0, 100, 0)
        hummingbird.set_tri_led(TwoPort.TWO, 0, 100, 0)
basic.forever(on_forever)
