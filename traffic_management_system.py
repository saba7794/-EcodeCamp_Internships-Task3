import random
import time

# Simulate traffic data collection from multiple intersections
def collect_traffic_data(num_intersections):
    traffic_data = {}
    for intersection_id in range(1, num_intersections + 1):
        traffic_data[f"intersection_{intersection_id}"] = {
            "cars_waiting": random.randint(0, 100),
            "signal_duration": random.randint(30, 90)  # in seconds
        }
    return traffic_data

# Display the collected traffic data
def display_traffic_data(data):
    for intersection, details in data.items():
        print(f"{intersection}: {details['cars_waiting']} cars waiting, signal duration: {details['signal_duration']}s")

# Analyze traffic patterns and identify congestion points
def analyze_traffic_patterns(traffic_data):
    congestion_points = []
    for intersection, details in traffic_data.items():
        if details["cars_waiting"] > 50:  # Threshold for congestion
            congestion_points.append(intersection)
    return congestion_points

# Optimize traffic signals based on congestion levels
def optimize_traffic_signals(traffic_data):
    optimized_signals = {}
    for intersection, details in traffic_data.items():
        # Adjust signal time based on cars waiting: more cars -> longer green light
        if details["cars_waiting"] > 50:
            optimized_signals[intersection] = 90  # max signal time
        else:
            optimized_signals[intersection] = 30  # minimum signal time
    return optimized_signals

# Simulate applying the optimized signal changes
def apply_signal_changes(optimized_signals):
    for intersection, signal_time in optimized_signals.items():
        print(f"Applying new signal timing at {intersection}: {signal_time}s")
        time.sleep(1)  # Simulate real-time adjustment

# Simulate traffic management system
def simulate_traffic_management(num_intersections, iterations=5, interval=5):
    for i in range(iterations):
        print(f"\n--- Simulation Round {i + 1} ---")
        
        # Step 1: Collect data
        traffic_data = collect_traffic_data(num_intersections)
        display_traffic_data(traffic_data)

        # Step 2: Analyze traffic patterns
        congested_intersections = analyze_traffic_patterns(traffic_data)
        print(f"Congested intersections: {congested_intersections}")

        # Step 3: Optimize traffic signals
        optimized_signals = optimize_traffic_signals(traffic_data)

        # Step 4: Apply signal changes
        apply_signal_changes(optimized_signals)

        # Wait before the next iteration
        time.sleep(interval)

# Run the simulation with 5 intersections and 5 iterations
simulate_traffic_management(5, iterations=5, interval=3)
