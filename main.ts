hummingbird.startHummingbird()
basic.forever(function on_forever() {
    if (hummingbird.getSensor(SensorType.Distance, ThreePort.One) < 20) {
        hummingbird.setRotationServo(FourPort.One, 0)
        hummingbird.setRotationServo(FourPort.Two, 0)
        hummingbird.setTriLED(TwoPort.One, 100, 0, 0)
        hummingbird.setTriLED(TwoPort.Two, 100, 0, 0)
        basic.pause(700)
        hummingbird.setRotationServo(FourPort.One, 50)
        hummingbird.setRotationServo(FourPort.Two, 50)
        basic.pause(2500)
    } else {
        hummingbird.setRotationServo(FourPort.One, 100)
        hummingbird.setRotationServo(FourPort.Two, -100)
        hummingbird.setTriLED(TwoPort.One, 0, 100, 0)
        hummingbird.setTriLED(TwoPort.Two, 0, 100, 0)
    }
    
})
