#!/usr/bin/python3
"""
multiply matrix using numpy module (pip3 install numpy)
"""

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.

    Raises:
        ValueError: If matrices cannot be multiplied.

    Example:
        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        array([[ 7, 10],
               [15, 22]])
    """
    try:
        result = np.matmul(np.array(m_a), np.array(m_b))
        return result
    except ValueError:
        raise ValueError("Matrix shapes are invalid for multiplication")
