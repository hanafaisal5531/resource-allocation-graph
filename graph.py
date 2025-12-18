from typing import Dict, List, Set

class ResourceAllocationGraph:
    def __init__(self):
        self.processes: Dict[str, dict] = {}
        self.resources: Dict[str, dict] = {}
        self.edges: List[dict] = []

    def add_process(self, pid: str):
        self.processes[pid] = {"id": pid}

    def add_resource(self, rid: str):
        self.resources[rid] = {"id": rid}

    def remove_node(self, node_id: str):
        self.processes.pop(node_id, None)
        self.resources.pop(node_id, None)
        self.edges = [
            e for e in self.edges
            if e["source"] != node_id and e["target"] != node_id
        ]

    def add_edge(self, source: str, target: str, edge_type: str):
        if not any(e for e in self.edges if e["source"] == source and e["target"] == target):
            self.edges.append({
                "source": source,
                "target": target,
                "type": edge_type
            })

    def remove_edge(self, source: str, target: str):
        self.edges = [
            e for e in self.edges
            if not (e["source"] == source and e["target"] == target)
        ]

    def build_adjacency_list(self) -> Dict[str, List[str]]:
        adj = {}
        for edge in self.edges:
            adj.setdefault(edge["source"], []).append(edge["target"])
        return adj

    def detect_deadlock(self) -> List[str]:
        adj = self.build_adjacency_list()
        visited = {}
        stack: Set[str] = set()
        deadlocked: Set[str] = set()

        def dfs(node: str):
            visited[node] = 1
            stack.add(node)

            for nbr in adj.get(node, []):
                if visited.get(nbr, 0) == 0:
                    dfs(nbr)
                elif nbr in stack:
                    deadlocked.update(stack)

            stack.remove(node)
            visited[node] = 2

        for node in list(self.processes) + list(self.resources):
            if visited.get(node, 0) == 0:
                dfs(node)

        return list(deadlocked)

    def snapshot(self):
        return {
            "processes": list(self.processes.values()),
            "resources": list(self.resources.values()),
            "edges": self.edges,
            "deadlocked_nodes": self.detect_deadlock()
        }
