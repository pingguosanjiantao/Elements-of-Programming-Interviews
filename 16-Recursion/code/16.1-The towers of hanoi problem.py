NUM_PEGS = 3


def computeTowerHanoi(numRings):
    pegs = [[]] * NUM_PEGS
    for i in range(numRings, 0, -1):
        pegs[0] += [i]
    computeTowerHanoiSteps(numRings, pegs, 0, 1, 2)


# peg flow: from -> use -> to
def computeTowerHanoiSteps(numRingsToMove, pegs, fromPeg, toPeg, usePeg):
    if numRingsToMove > 0:
        computeTowerHanoiSteps(numRingsToMove - 1, pegs, fromPeg, usePeg, toPeg)
        pegs[toPeg] += [pegs[fromPeg].pop()]
        print 'move from peg ', fromPeg, "to peg ", toPeg
        computeTowerHanoiSteps(numRingsToMove - 1, pegs, usePeg, toPeg, fromPeg)


computeTowerHanoi(4)
