# Hydro Power Generation & Efficiency Calculator
# Formula: P = n * rho * g * h * q

def calculate_hydro_power(head, flow_rate, efficiency=0.85):
    gravity = 9.81        # m/s^2
    water_density = 1000  # kg/m^3
    
    # Calculation in Watts
    power_watts = efficiency * water_density * gravity * head * flow_rate
    
    # Convert to Kilowatts
    power_kw = power_watts / 1000
    return round(power_kw, 2)

# Sample Input for Himachal Terrain
head_m = 50       # 50 meters head
flow_m3s = 0.2    # 0.2 cubic meters per second

result = calculate_hydro_power(head_m, flow_m3s)

print(f"--- Micro-Hydro Power Report ---")
print(f"Net Head: {head_m} meters")
print(f"Flow Rate: {flow_m3s} m^3/s")
print(f"Estimated Power Output: {result} kW")

