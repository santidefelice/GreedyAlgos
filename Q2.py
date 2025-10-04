"""
Question 2: Minimizing Freight Truck Travel Cost in a Warehouse Network
Using Kruskal's Algorithm (Greedy MST Algorithm)
"""

class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure for efficient cycle detection
    Used in Kruskal's algorithm to check if adding an edge creates a cycle
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """Find the root parent of node x with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union two sets by rank"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True


def kruskal_mst(num_warehouses, edges):
    """
    Kruskal's Algorithm for Minimum Spanning Tree
    
    GREEDY STRATEGY:
    1. Sort all edges by weight (construction cost) in ascending order
    2. Pick the smallest edge that doesn't create a cycle
    3. Repeat until we have (n-1) edges (where n is number of warehouses)
    
    This greedy approach guarantees optimal solution because:
    - At each step, we choose the minimum cost edge that connects two components
    - The cut property ensures this edge must be in some MST
    - By always choosing minimum edges, we build the globally optimal MST
    
    Parameters:
    - num_warehouses: number of nodes (warehouses)
    - edges: list of tuples (warehouse1, warehouse2, cost)
    
    Returns:
    - mst_edges: list of edges in the MST
    - total_cost: minimum total construction cost
    """
    
    # Step 1: Sort edges by cost (greedy choice - always pick minimum cost edge)
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize Union-Find data structure for cycle detection
    uf = UnionFind(num_warehouses)
    
    mst_edges = []
    total_cost = 0
    
    # Step 2: Iterate through sorted edges
    for warehouse1, warehouse2, cost in sorted_edges:
        # Step 3: If adding this edge doesn't create a cycle, include it in MST
        if uf.union(warehouse1, warehouse2):
            mst_edges.append((warehouse1, warehouse2, cost))
            total_cost += cost
            
            # If we have n-1 edges, MST is complete
            if len(mst_edges) == num_warehouses - 1:
                break
    
    return mst_edges, total_cost


def print_graph(num_warehouses, edges):
    """Helper function to display the graph"""
    print("\n" + "="*60)
    print("WAREHOUSE NETWORK GRAPH")
    print("="*60)
    print(f"Number of Warehouses: {num_warehouses}")
    print(f"Number of Potential Routes: {len(edges)}")
    print("\nAll Potential Transportation Lines:")
    print(f"{'From':<10} {'To':<10} {'Cost':<10}")
    print("-" * 30)
    for w1, w2, cost in edges:
        print(f"{w1:<10} {w2:<10} ${cost:<10}")


def print_mst_result(mst_edges, total_cost):
    """Helper function to display MST results"""
    print("\n" + "="*60)
    print("MINIMUM SPANNING TREE SOLUTION")
    print("="*60)
    print(f"\nSelected Transportation Lines (Minimum Cost Network):")
    print(f"{'From':<10} {'To':<10} {'Cost':<10}")
    print("-" * 30)
    for w1, w2, cost in mst_edges:
        print(f"{w1:<10} {w2:<10} ${cost:<10}")
    
    print(f"\n{'='*30}")
    print(f"TOTAL MINIMUM COST: ${total_cost}")
    print(f"{'='*30}")
    print(f"Number of routes built: {len(mst_edges)}")


# ============================================================================
# TEST CASE 1: Example from assignment (5 nodes, 10 edges)
# ============================================================================
print("\n" + "#"*60)
print("# TEST CASE 1: Standard Warehouse Network")
print("#"*60)

# Graph representation: List of edges (warehouse1, warehouse2, cost)
# Warehouses labeled as: 0, 1, 2, 3, 4
num_warehouses_1 = 5

edges_1 = [
    (0, 1, 10),  # Warehouse 0 to 1: $10
    (0, 2, 6),   # Warehouse 0 to 2: $6
    (0, 3, 5),   # Warehouse 0 to 3: $5
    (1, 3, 15),  # Warehouse 1 to 3: $15
    (1, 4, 8),   # Warehouse 1 to 4: $8
    (2, 3, 4),   # Warehouse 2 to 3: $4
    (2, 4, 12),  # Warehouse 2 to 4: $12
    (3, 4, 7),   # Warehouse 3 to 4: $7
    (0, 4, 20),  # Warehouse 0 to 4: $20
    (1, 2, 9)    # Warehouse 1 to 2: $9
]

print_graph(num_warehouses_1, edges_1)

# Apply Kruskal's algorithm
mst_edges_1, total_cost_1 = kruskal_mst(num_warehouses_1, edges_1)

print_mst_result(mst_edges_1, total_cost_1)

print("\nGraph Visualization:")
print("""
Original Graph (showing all potential routes):

        10
    0 --------1
    |\\      / |\\
   6| \\5  9/  | \\8
    |  \\ /   15  \\
    2---3------4
      4  \\   /
          \\ /7
           X
          /12\\
         
Minimum Spanning Tree (selected routes):

    0       1
    |        \\
   6|         \\8
    |          \\
    2---3------4
      4  \\   /
          \\ /7

Total Cost: $25 (edges: 0-3:$5, 2-3:$4, 3-4:$7, 0-2:$6, 1-4:$8)
""")


# ============================================================================
# TEST CASE 2: Larger network with 7 warehouses
# ============================================================================
print("\n\n" + "#"*60)
print("# TEST CASE 2: Extended Warehouse Network (7 warehouses)")
print("#"*60)

num_warehouses_2 = 7

edges_2 = [
    (0, 1, 7),
    (0, 3, 5),
    (1, 2, 8),
    (1, 3, 9),
    (1, 4, 7),
    (2, 4, 5),
    (3, 4, 15),
    (3, 5, 6),
    (4, 5, 8),
    (4, 6, 9),
    (5, 6, 11),
    (0, 2, 12),
    (2, 5, 10)
]

print_graph(num_warehouses_2, edges_2)

mst_edges_2, total_cost_2 = kruskal_mst(num_warehouses_2, edges_2)

print_mst_result(mst_edges_2, total_cost_2)


# ============================================================================
# TEST CASE 3: Dense network scenario
# ============================================================================
print("\n\n" + "#"*60)
print("# TEST CASE 3: Dense Network (6 warehouses, multiple options)")
print("#"*60)

num_warehouses_3 = 6

edges_3 = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6),
    (2, 4, 5),
    (1, 4, 8),
    (0, 5, 10),
    (3, 5, 7)
]

print_graph(num_warehouses_3, edges_3)

mst_edges_3, total_cost_3 = kruskal_mst(num_warehouses_3, edges_3)

print_mst_result(mst_edges_3, total_cost_3)


# ============================================================================
# ALGORITHM ANALYSIS
# ============================================================================
print("\n\n" + "="*60)
print("ALGORITHM ANALYSIS")
print("="*60)

print("""
TIME COMPLEXITY:
- Sorting edges: O(E log E) where E is number of edges
- Union-Find operations: O(α(V)) ≈ O(1) amortized per operation
- Total: O(E log E) or O(E log V) since E ≤ V²

SPACE COMPLEXITY:
- O(V + E) for storing graph and Union-Find structure

OPTIMALITY PROOF (Why Greedy Works):
This problem CAN be optimally solved by greedy algorithm (Kruskal's).

Proof by Exchange Argument:
1. Assume there exists an MST T* that differs from our greedy solution G
2. Let e be the first edge in G (sorted order) that's not in T*
3. Adding e to T* creates a cycle
4. In this cycle, there must be another edge e' not in G
5. Since we considered edges in sorted order, weight(e) ≤ weight(e')
6. Replacing e' with e gives a tree with cost ≤ cost(T*)
7. Since T* was optimal, this new tree is also optimal
8. By repeating this exchange, we can transform T* into G
9. Therefore, G is also optimal (MST)

Greedy Choice Property:
At each step, choosing the minimum weight edge that doesn't create a
cycle is safe because it must be part of SOME minimum spanning tree.

Optimal Substructure:
Removing any edge from an MST splits it into two components, and the
remaining edges form MSTs of those components.

CONCLUSION: Kruskal's algorithm GUARANTEES an optimal solution for the
Minimum Spanning Tree problem, making it perfect for minimizing the
total construction cost while ensuring all warehouses are connected.
""")