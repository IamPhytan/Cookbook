import numpy as np


# pylint: disable=invalid-name
def trilateration_3D(coordinates: np.array, distances: np.array) -> np.array:
    """Determine the 3D coordinates of an object
    from the distances and the coordinates of 3 known landmarks

    Examples:
        >>> coords = np.array([[3, 0, 0], [0, -5, 0], [0, 0, 4]])
        >>> distances = np.array([3, 5, 4])
        >>> trilateration_3D(coords, distances)
        array([0, 0, 0])
        >>> coords = np.array([[0, 0, 0], [3, 5, 0], [3, 0, 4]])
        >>> distances = np.array([3, 5, 4])
        >>> trilateration_3D(coords, distances)
        array([3, 0, 0])

    Args:
        coordinates: A 3x3 array where each row contains the coordinates (x,y,z) of a landmark
        distances: A 3x1 array containing the distances between
        each landmark and the point to localize

    Returns:
        3D Coordinates `(x,y,z)` determined by trilateration

    Raises:
        ValueError: An error occurs when the rank of `coordinates` is less than 3
    """
    coords_rank = np.linalg.matrix_rank(coordinates)
    if coords_rank < 3:
        raise ValueError(f"coordinates array has a rank of {coords_rank}. Rank should be at least 3")

    sum_of_squares = np.square(coordinates).sum(axis=1)
    d_prime = distances - sum_of_squares

    A = np.vstack([coordinates, coordinates[0, :]])
    A = -1 * np.diff(A, axis=0)

    B = d_prime / -2
    X = np.linalg.inv(A) @ B
    return X


if __name__ == "__main__":
    coords = np.array([[3, 0, 0], [0, -5, 0], [0, 0, 4]])
    distances = np.array([3, 5, 4])
    trilateration_3D(coords, distances)
    coords = np.array([[0, 0, 0], [3, 5, 0], [3, 0, 4]])
    trilateration_3D(coords, distances)
