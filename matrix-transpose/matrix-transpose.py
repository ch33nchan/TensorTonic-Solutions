import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.asarray(A,dtype=float)
    N,M = A.shape
    result = np.zeros((M,N))
    for i in range(N):
        for j in range(M):
            result[j][i] = A[i][j]
    pass
    return result
