class CpGIslandViterbiDetector:
    """Viterbi HMM decoder for detecting High (CpG) and Low CG methylation regimes."""
    def __init__(self):
        self.states = ('CpG_High', 'CpG_Low')
        self.start_p = {'CpG_High': 0.5, 'CpG_Low': 0.5}
        self.trans_p = {
            'CpG_High': {'CpG_High': 0.8, 'CpG_Low': 0.2},
            'CpG_Low': {'CpG_High': 0.1, 'CpG_Low': 0.9}
        }
        self.emit_p = {
            'CpG_High': {'A': 0.15, 'C': 0.35, 'G': 0.35, 'T': 0.15},
            'CpG_Low': {'A': 0.30, 'C': 0.20, 'G': 0.20, 'T': 0.30}
        }

    def decode(self, dna_sequence: str) -> dict:
        obs = [c.upper() for c in dna_sequence if c.upper() in 'ACGT']
        if not obs:
            return {"path": [], "cpg_ratio": 0.0}

        V = [{}]
        path = {}
        for y in self.states:
            V[0][y] = self.start_p[y] * self.emit_p[y].get(obs[0], 0.01)
            path[y] = [y]

        for t in range(1, len(obs)):
            V.append({})
            newpath = {}
            for y in self.states:
                (prob, state) = max(
                    (V[t-1][y0] * self.trans_p[y0][y] * self.emit_p[y].get(obs[t], 0.01), y0)
                    for y0 in self.states
                )
                V[t][y] = prob
                newpath[y] = path[state] + [y]
            path = newpath

        (max_prob, best_state) = max((V[len(obs) - 1][y], y) for y in self.states)
        best_path = path[best_state]
        cpg_count = sum(1 for s in best_path if s == 'CpG_High')

        return {
            "sequence_length": len(obs),
            "cpg_island_bases": cpg_count,
            "cpg_ratio": round(cpg_count / len(obs), 4),
            "states_path": best_path
        }
