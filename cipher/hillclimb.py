# import external packages first. Doesn't matter for the code but is advised practice for readability
import numpy as np

#from cipher.minheap import MinHeapString


def hillclimb(start_node, score_func, neighbours_func, score_args=(), iterations=5):
    # score args will probably just be the ciphertext, but make sure it's in a tuple: score_args=(ciphertext)
    node = start_node
    current_score = score_func(node, *score_args)
    count = 0
    for it in range(iterations):
        while True:
            count += 1
            neighbours = neighbours_func(node)
            # scores = [None]*len(neighbours)
            scores = np.zeros(shape=len(neighbours))
            for i, n in enumerate(neighbours):
                scores[i] = score_func(node, *score_args)
            idx = np.argmax(scores)

            if scores[idx] < current_score:
                break
            current_score = scores[idx]
            node = neighbours[idx]
    return node