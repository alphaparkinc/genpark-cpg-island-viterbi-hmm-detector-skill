from client import CpGIslandViterbiDetector

def main():
    print("=== CpG Island Viterbi HMM Detector ===")
    detector = CpGIslandViterbiDetector()
    dna = "CGCGCGCGATATATAT"

    res = detector.decode(dna)
    print("Decoding result:", res["cpg_island_bases"], "bases marked as CpG island.")
    assert res["cpg_ratio"] >= 0.4
    print("CpG Island Viterbi Detector verified successfully!")

if __name__ == "__main__":
    main()
