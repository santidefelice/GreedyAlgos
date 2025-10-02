"""
Question 1: Music Festival Stage Scheduling
Greedy Algorithm: Activity Selection Problem
Author: [Your Name Here]
Partner: [Partner Name if applicable]
"""

class Band:
    """Data structure to store band performance information"""
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"{self.name} [{self.start}, {self.end}]"


def schedule_bands(bands):
    """
    Greedy algorithm to select maximum number of non-overlapping performances.
    
    Algorithm Logic:
    1. Sort bands by end time (earliest finish time first)
    2. Select the first band
    3. For each subsequent band, if its start time >= last selected band's end time, select it
    
    This greedy choice is optimal because selecting the activity that finishes earliest
    leaves the most room for subsequent activities.
    
    Time Complexity: O(n log n) due to sorting
    
    Args:
        bands: List of Band objects
    
    Returns:
        List of selected Band objects
    """
    if not bands:
        return []
    
    # Step 1: Sort by end time (greedy choice: earliest finish time)
    sorted_bands = sorted(bands, key=lambda x: x.end)
    
    # Step 2: Select first band
    selected = [sorted_bands[0]]
    last_end_time = sorted_bands[0].end
    
    # Step 3: Iterate through remaining bands
    for i in range(1, len(sorted_bands)):
        current_band = sorted_bands[i]
        
        # If current band starts after or when last selected band ends, select it
        if current_band.start >= last_end_time:
            selected.append(current_band)
            last_end_time = current_band.end
    
    return selected


def get_user_input():
    """Get band information from user input"""
    try:
        n = int(input("Enter the number of bands: "))
        bands = []
        
        print("\nEnter start and end times for each band:")
        for i in range(n):
            name = input(f"Band {i+1} name: ")
            start = int(input(f"  Start time: "))
            end = int(input(f"  End time: "))
            bands.append(Band(name, start, end))
        
        return bands
    except ValueError:
        print("Invalid input! Please enter numeric values for times.")
        return []


def print_results(bands, selected):
    """Display scheduling results"""
    print("\n" + "="*60)
    print("MUSIC FESTIVAL SCHEDULING RESULTS")
    print("="*60)
    
    print(f"\nTotal bands proposed: {len(bands)}")
    print(f"Maximum bands that can perform: {len(selected)}")
    
    print("\nSelected bands schedule:")
    for i, band in enumerate(selected, 1):
        print(f"  {i}. {band.name}: {band.start}:00 - {band.end}:00")
    
    print("\n" + "="*60)


# ============== TEST CASES ==============

def test_case_1():
    """Test Case 1: Standard case with overlapping bands"""
    print("\n" + "#"*60)
    print("TEST CASE 1: Standard Scenario")
    print("#"*60)
    
    bands = [
        Band("Rock Band A", 9, 11),
        Band("Jazz Band B", 10, 12),
        Band("Pop Band C", 11, 13),
        Band("Blues Band D", 12, 14),
        Band("Folk Band E", 13, 15)
    ]
    
    print("\nInput bands:")
    for band in bands:
        print(f"  {band}")
    
    selected = schedule_bands(bands)
    print_results(bands, selected)


def test_case_2():
    """Test Case 2: All bands overlap at the same time"""
    print("\n" + "#"*60)
    print("TEST CASE 2: All Overlapping")
    print("#"*60)
    
    bands = [
        Band("Band 1", 10, 15),
        Band("Band 2", 11, 14),
        Band("Band 3", 12, 13),
        Band("Band 4", 9, 16)
    ]
    
    print("\nInput bands:")
    for band in bands:
        print(f"  {band}")
    
    selected = schedule_bands(bands)
    print_results(bands, selected)


def test_case_3():
    """Test Case 3: No overlapping bands (all can be scheduled)"""
    print("\n" + "#"*60)
    print("TEST CASE 3: No Overlaps - All Can Perform")
    print("#"*60)
    
    bands = [
        Band("Morning Band", 8, 10),
        Band("Late Morning Band", 10, 12),
        Band("Afternoon Band", 12, 14),
        Band("Evening Band", 14, 16),
        Band("Night Band", 16, 18)
    ]
    
    print("\nInput bands:")
    for band in bands:
        print(f"  {band}")
    
    selected = schedule_bands(bands)
    print_results(bands, selected)


# ============== MAIN PROGRAM ==============

if __name__ == "__main__":
    print("="*60)
    print("MUSIC FESTIVAL STAGE SCHEDULING")
    print("Greedy Algorithm: Activity Selection")
    print("="*60)
    
    # Run automated test cases
    test_case_1()
    test_case_2()
    test_case_3()
    
    # Optional: Interactive mode
    print("\n" + "#"*60)
    print("INTERACTIVE MODE (Optional)")
    print("#"*60)
    
    user_input = input("\nWould you like to input your own bands? (yes/no): ").lower()
    if user_input == 'yes':
        bands = get_user_input()
        if bands:
            selected = schedule_bands(bands)
            print_results(bands, selected)
    
    # Optimality Analysis
    print("\n" + "="*60)
    print("OPTIMALITY ANALYSIS")
    print("="*60)
    print("""
This problem CAN be solved optimally using a greedy algorithm.

Greedy Choice: Always select the activity that finishes earliest among
remaining compatible activities.

Proof of Optimality (Exchange Argument):
1. Let A be the optimal solution and G be our greedy solution
2. If they differ, let the first difference be at position k
3. We can replace A's kth activity with G's kth activity (earlier finish)
4. This leaves more room for future activities, so A' is also optimal
5. By induction, we can transform A into G without losing optimality

Time Complexity: O(n log n)
- Sorting: O(n log n)
- Selection: O(n)
- Total: O(n log n)

This greedy algorithm guarantees the maximum number of non-overlapping
performances will be scheduled.
    """)
    print("="*60)