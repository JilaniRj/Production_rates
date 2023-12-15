import random 
import time

def simulate_production_rate(initial_rate, time_steps): production_rate = initial_rate

for step in range(1, time_steps + 1):
    # Simulate variations in production rate (you can customize this based on your scenario)
    variation = random.uniform(-0.1, 0.1)
    production_rate += variation

    # Ensure production rate is within acceptable limits
    production_rate = max(0, production_rate)

    print(f"Step {step}: Production Rate = {production_rate:.2f} widgets per hour")

    time.sleep(1)  # Simulate the passage of time (1 second delay between steps)

return production_rate
Example usage
initial_production_rate = 50 # Initial production rate in widgets per hour simulation_time_steps = 10 # Number of simulation time steps

final_production_rate = simulate_production_rate(initial_production_rate, simulation_time_steps)

print(f"\nSimulation completed. Final Production Rate = {final_production_rate:.2f} widgets per hour")
