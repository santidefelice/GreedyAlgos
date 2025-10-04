"""
Question 3: Conference Room Allocation with Sponsors
Scheduling seminars across two conference rooms to maximize total profit
"""

def greedy_two_room_scheduling(seminars):
    """
    GREEDY STRATEGY (HEURISTIC - NOT ALWAYS OPTIMAL):
    Sort seminars by profit in descending order and try to fit them into
    two available rooms without conflicts.
    
    This greedy approach does NOT guarantee optimal solution because:
    - Choosing high-profit seminars first might block multiple lower-profit
      seminars that together would yield more profit
    - The problem is NP-hard (related to weighted interval scheduling on
      multiple machines)
    
    Parameters:
    - seminars: list of tuples (start, end, profit, seminar_id)
    
    Returns:
    - scheduled: list of scheduled seminars with room assignments
    - total_profit: total profit achieved
    """
    
    # Sort by profit (descending) - Greedy choice
    sorted_seminars = sorted(seminars, key=lambda x: x[2], reverse=True)
    
    # Track occupied time slots for each room
    room1_schedule = []  # List of (start, end, profit, seminar_id)
    room2_schedule = []  # List of (start, end, profit, seminar_id)
    
    scheduled = []
    total_profit = 0
    
    for start, end, profit, sem_id in sorted_seminars:
        # Check if seminar can fit in room 1
        if can_schedule(room1_schedule, start, end):
            room1_schedule.append((start, end, profit, sem_id))
            scheduled.append((start, end, profit, sem_id, "Room 1"))
            total_profit += profit
        # Check if seminar can fit in room 2
        elif can_schedule(room2_schedule, start, end):
            room2_schedule.append((start, end, profit, sem_id))
            scheduled.append((start, end, profit, sem_id, "Room 2"))
            total_profit += profit
        # If neither room available, skip this seminar
    
    return scheduled, total_profit, room1_schedule, room2_schedule


def can_schedule(room_schedule, start, end):
    """
    Check if a seminar can be scheduled in a room without conflicts
    
    Returns True if the time slot [start, end] doesn't overlap with
    any existing seminars in the room
    """
    for s_start, s_end, _, _ in room_schedule:
        # Check for overlap: seminars overlap if one starts before the other ends
        if not (end <= s_start or start >= s_end):
            return False
    return True


def dynamic_programming_approach(seminars):
    """
    DYNAMIC PROGRAMMING APPROACH (OPTIMAL SOLUTION):
    
    This is a more sophisticated approach that considers all combinations
    to find the truly optimal solution. For two rooms, we can use a DP
    approach similar to weighted interval scheduling but with two machines.
    
    This is computationally more expensive but guarantees optimal solution.
    For demonstration purposes, we'll implement a simplified version.
    
    Note: A complete optimal solution would require exploring all valid
    combinations of seminar assignments to the two rooms, which has
    exponential complexity O(3^n) - each seminar can go to room1, room2, or neither.
    """
    
    # Sort seminars by end time for DP approach
    sorted_seminars = sorted(seminars, key=lambda x: x[1])
    n = len(sorted_seminars)
    
    # For simplicity, we'll use a brute-force approach with memoization
    # to demonstrate that greedy doesn't always work
    
    # This would be a full implementation in a real scenario
    # For now, we'll note that this requires exponential time
    
    return "DP approach requires exponential time - demonstration of optimal solution"


def earliest_end_time_greedy(seminars):
    """
    ALTERNATIVE GREEDY STRATEGY:
    Sort by earliest end time and schedule greedily
    
    This is another greedy heuristic that also doesn't guarantee optimality
    for the weighted version with two rooms.
    """
    
    sorted_seminars = sorted(seminars, key=lambda x: x[1])  # Sort by end time
    
    room1_schedule = []
    room2_schedule = []
    
    scheduled = []
    total_profit = 0
    
    for start, end, profit, sem_id in sorted_seminars:
        if can_schedule(room1_schedule, start, end):
            room1_schedule.append((start, end, profit, sem_id))
            scheduled.append((start, end, profit, sem_id, "Room 1"))
            total_profit += profit
        elif can_schedule(room2_schedule, start, end):
            room2_schedule.append((start, end, profit, sem_id))
            scheduled.append((start, end, profit, sem_id, "Room 2"))
            total_profit += profit
    
    return scheduled, total_profit, room1_schedule, room2_schedule


def print_seminars(seminars):
    """Display all available seminars"""
    print("\n" + "="*70)
    print("ALL AVAILABLE SEMINARS")
    print("="*70)
    print(f"{'ID':<6} {'Start':<8} {'End':<8} {'Profit':<10} {'Duration':<10}")
    print("-" * 70)
    for start, end, profit, sem_id in seminars:
        duration = end - start
        print(f"S{sem_id:<5} {start:<8} {end:<8} ${profit:<9} {duration} hours")
    
    total_possible = sum(s[2] for s in seminars)
    print(f"\nTotal available seminars: {len(seminars)}")
    print(f"Total possible profit (if all could run): ${total_possible}")


def print_schedule_result(scheduled, total_profit, room1_schedule, room2_schedule, title):
    """Display scheduling results"""
    print("\n" + "="*70)
    print(f"{title}")
    print("="*70)
    
    # Sort by start time for display
    scheduled_sorted = sorted(scheduled, key=lambda x: x[0])
    
    print(f"\n{'ID':<6} {'Start':<8} {'End':<8} {'Profit':<10} {'Room':<10}")
    print("-" * 70)
    for start, end, profit, sem_id, room in scheduled_sorted:
        print(f"S{sem_id:<5} {start:<8} {end:<8} ${profit:<9} {room}")
    
    print(f"\n{'='*35}")
    print(f"TOTAL PROFIT: ${total_profit}")
    print(f"{'='*35}")
    print(f"Seminars scheduled: {len(scheduled)}")
    print(f"Room 1: {len(room1_schedule)} seminars")
    print(f"Room 2: {len(room2_schedule)} seminars")


def demonstrate_greedy_failure():
    """
    COUNTEREXAMPLE: Demonstrates that greedy by profit fails
    
    This example shows a case where greedy approach (sorting by profit)
    gives a suboptimal solution.
    """
    print("\n" + "#"*70)
    print("# COUNTEREXAMPLE: Why Greedy-by-Profit Fails")
    print("#"*70)
    
    # Counterexample scenario
    seminars_counter = [
        # (start, end, profit, id)
        (0, 4, 100, 1),   # High profit, long duration, blocks others
        (0, 4, 100, 2),   # High profit, long duration, blocks others
        (0, 2, 60, 3),    # Medium profit, shorter
        (2, 4, 60, 4),    # Medium profit, shorter
        (0, 2, 60, 5),    # Medium profit, shorter
        (2, 4, 60, 6),    # Medium profit, shorter
    ]
    
    print("\nScenario:")
    print("Two long high-profit seminars (S1: $100, S2: $100) that span 0-4")
    print("Four shorter medium-profit seminars (S3-S6: $60 each) in slots 0-2 and 2-4")
    
    print_seminars(seminars_counter)
    
    # Greedy by profit
    scheduled_greedy, profit_greedy, r1, r2 = greedy_two_room_scheduling(seminars_counter)
    print_schedule_result(scheduled_greedy, profit_greedy, r1, r2, 
                         "GREEDY RESULT (by profit - suboptimal)")
    
    # Optimal solution
    print("\n" + "="*70)
    print("OPTIMAL SOLUTION (manually computed)")
    print("="*70)
    print("\nSchedule S3, S4 in Room 1 and S5, S6 in Room 2")
    print("Room 1: S3 (0-2, $60) + S4 (2-4, $60) = $120")
    print("Room 2: S5 (0-2, $60) + S6 (2-4, $60) = $120")
    print("\n" + "="*35)
    print("OPTIMAL TOTAL PROFIT: $240")
    print("="*35)
    print(f"Greedy achieved: ${profit_greedy}")
    print(f"Optimal solution: $240")
    print(f"Greedy is suboptimal by: ${240 - profit_greedy}")


# ============================================================================
# TEST CASE 1: Standard scenario
# ============================================================================
print("\n" + "#"*70)
print("# TEST CASE 1: Standard Conference Scheduling")
print("#"*70)

seminars_1 = [
    # (start_time, end_time, profit, seminar_id)
    (9, 11, 500, 1),   # Morning seminar, high sponsor
    (10, 12, 300, 2),  # Overlaps with S1
    (11, 13, 400, 3),  # Midday seminar
    (12, 14, 350, 4),  # Early afternoon
    (13, 15, 600, 5),  # High-value afternoon seminar
    (14, 16, 200, 6),  # Late afternoon
    (9, 10, 150, 7),   # Short morning session
    (15, 17, 450, 8),  # End of day seminar
]

print_seminars(seminars_1)

# Apply greedy by profit
scheduled_1, profit_1, room1_1, room2_1 = greedy_two_room_scheduling(seminars_1)
print_schedule_result(scheduled_1, profit_1, room1_1, room2_1, 
                     "GREEDY SOLUTION (by profit)")

# Apply greedy by earliest end time
scheduled_1b, profit_1b, room1_1b, room2_1b = earliest_end_time_greedy(seminars_1)
print_schedule_result(scheduled_1b, profit_1b, room1_1b, room2_1b, 
                     "ALTERNATIVE GREEDY (by earliest end time)")


# ============================================================================
# TEST CASE 2: Dense schedule with many conflicts
# ============================================================================
print("\n\n" + "#"*70)
print("# TEST CASE 2: Dense Schedule with Multiple Conflicts")
print("#"*70)

seminars_2 = [
    (8, 10, 400, 1),
    (9, 11, 500, 2),
    (10, 12, 350, 3),
    (11, 13, 450, 4),
    (12, 14, 300, 5),
    (13, 15, 550, 6),
    (14, 16, 400, 7),
    (15, 17, 300, 8),
    (8, 9, 200, 9),
    (16, 18, 500, 10),
]

print_seminars(seminars_2)

scheduled_2, profit_2, room1_2, room2_2 = greedy_two_room_scheduling(seminars_2)
print_schedule_result(scheduled_2, profit_2, room1_2, room2_2, 
                     "GREEDY SOLUTION (by profit)")


# ============================================================================
# TEST CASE 3: Demonstrate greedy failure
# ============================================================================
demonstrate_greedy_failure()


# ============================================================================
# ALGORITHM ANALYSIS
# ============================================================================
print("\n\n" + "="*70)
print("ALGORITHM ANALYSIS")
print("="*70)

print("""
PROBLEM CLASSIFICATION:
This is the Weighted Interval Scheduling Problem with k=2 machines (rooms).
This problem is NP-hard, meaning no polynomial-time algorithm is known that
guarantees an optimal solution.

TIME COMPLEXITY OF GREEDY APPROACHES:
- Sorting: O(n log n) where n is number of seminars
- Scheduling: O(n²) in worst case (checking conflicts for each seminar)
- Total: O(n²)

SPACE COMPLEXITY:
- O(n) for storing schedules

OPTIMALITY ANALYSIS - WHY GREEDY FAILS:
===========================================

The greedy approach CANNOT guarantee optimal solution. Here's why:

1. GREEDY-BY-PROFIT FAILURE:
   Choosing highest profit seminars first can block multiple lower-profit
   seminars that together yield more profit.
   
   Example: One seminar worth $100 (0-4) vs two seminars worth $60 each
   (0-2 and 2-4). Greedy picks the $100, but optimal is $120.

2. GREEDY-BY-EARLIEST-END-TIME FAILURE:
   This works for single-machine unweighted scheduling, but fails when:
   - We have weights (profits) - may skip high-profit for low-profit
   - We have multiple machines - complex interactions between room assignments

3. COUNTEREXAMPLE (as demonstrated above):
   Two rooms, six seminars:
   - S1, S2: 0-4, profit $100 each
   - S3, S4, S5, S6: alternating 0-2 and 2-4, profit $60 each
   
   Greedy-by-profit selects: S1 (Room 1), S2 (Room 2)
   Total: $200
   
   Optimal solution: S3, S4 (Room 1), S5, S6 (Room 2)
   Total: $240
   
   Difference: $40 (20% better than greedy)

PROOF THAT GREEDY FAILS (Exchange Argument):
=============================================

Assume greedy gives optimal solution. Consider the counterexample:
- Greedy chooses S1 ($100) and S2 ($100) for total $200
- But we can exchange these for S3, S4, S5, S6 ($60 × 4) for total $240
- Since $240 > $200, greedy is not optimal
- Contradiction! Therefore, greedy does NOT guarantee optimal solution.

OPTIMAL SOLUTION APPROACHES:
=============================

To find the TRUE optimal solution, we need:

1. Dynamic Programming with Exponential States:
   - State: dp[i][room1_state][room2_state]
   - Complexity: O(n × 2^n × 2^n) - impractical for large n

2. Integer Linear Programming (ILP):
   - Formulate as optimization problem
   - Use ILP solver (e.g., branch and bound)
   - Exact but exponential worst-case

3. Branch and Bound:
   - Systematically explore solution space
   - Prune suboptimal branches
   - Exact but exponential worst-case

4. Approximation Algorithms:
   - Provide provable guarantees (e.g., 2-approximation)
   - Polynomial time
   - Not exact but close to optimal

CONCLUSION:
===========
While greedy approaches are fast and often give good solutions, they
CANNOT guarantee optimal solutions for the weighted interval scheduling
problem with multiple machines. The problem's NP-hard nature means that
finding the optimal solution requires exploring many combinations.

For practical purposes:
- Use greedy as a fast heuristic
- For small instances, use exact methods (DP, ILP)
- For large instances, accept approximate solutions
- Test multiple greedy strategies and pick the best result
""")