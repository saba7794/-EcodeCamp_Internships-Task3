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
