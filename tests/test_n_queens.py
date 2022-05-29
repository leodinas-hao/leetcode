import pytest

from leetcode.n_queens import Solution


@pytest.mark.parametrize('n,numSolutions', [
  (4, 2),
  (1, 1),
  (5, 10),
])
def test_n_queens(n, numSolutions):
  nQueenSolver = Solution()
  solutions = nQueenSolver.solveNQueens(n)
  assert len(solutions) == numSolutions
