
# Let R be a relation from a set A to a set B and S a relation from B to a set C. The composite
# of R and S is the relation consisting of ordered pairs (a, c), where a ∈ A, c ∈ C, and for
# which there exists an element b ∈ B such that (a, b) ∈ R and (b, c) ∈ S. We denote the
# composite of R and S by S ◦R
def composite(A, B, C, R, S):
    composition = set()
    for pair in R:
        for pair2 in S:
            # there exists a b 
            if pair[1] == pair2[0]:
                a = pair[0]
                b = pair[1]
                c = pair2[1]
                #(a, b) ∈ R and (b, c) ∈ S
                if a in A and c in C and (a, b) in R and (b, c) in S:
                    composition.add((a, c))
    return composition


graph = (1, 2, 3, 4)
relations = ((1,1), (2,1), (3,2), (4,3))
r2 = composite(graph, graph, graph, relations, relations)
r3 = composite(graph, graph, graph, relations, r2)
print("r2=%s" % r2)
print("r3=%s" % r3)

