# test_chapter3.py
import pytest
from inheritance import Vehicle, Car, Motorcycle

# Vehicle, Car, Motorcycle 클래스 테스트
def test_vehicles():
    # Vehicle 테스트
    vehicle = Vehicle("Generic", "Model X", 2023, 60)
    assert vehicle.make == "Generic"
    assert vehicle.model == "Model X"
    assert vehicle.year == 2023
    assert vehicle.fuel_capacity == 60
    assert vehicle.fuel_level == 0
    
    assert vehicle.fuel_up() == 60
    assert vehicle.fuel_level == 60
    
    # Car 테스트
    car = Car("Toyota", "Camry", 2023, 50, 4, 10)  # 10km/L
    assert car.make == "Toyota"
    assert car.model == "Camry"
    assert car.num_doors == 4
    assert car.fuel_efficiency == 10
    
    car.fuel_up()
    assert car.drive(100) == 40  # 100km 주행 시 10L 소모, 남은 연료 40L
    
    with pytest.raises(ValueError):
        car.drive(500)  # 연료 부족
    
    # Motorcycle 테스트
    bike = Motorcycle("Harley", "Sportster", 2023, 15, False, 20)  # 20km/L
    assert bike.make == "Harley"
    assert bike.model == "Sportster"
    assert bike.has_sidecar == False
    assert bike.fuel_efficiency == 20
    
    bike.fuel_up()
    assert bike.drive(60) == 12  # 60km 주행 시 3L 소모, 남은 연료 12L
