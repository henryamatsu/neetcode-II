class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_row = 0
        r_row = len(matrix) - 1

        row_index = -1
        while l_row <= r_row:
            m_row = (l_row + r_row) // 2
            first_val = matrix[m_row][0]
            last_val = matrix[m_row][-1]

            if target < first_val:
                r_row = m_row - 1
            elif target > last_val:
                l_row = m_row + 1
            else:
                row_index = m_row
                break

        row = matrix[row_index]
        l = 0
        r = len(row) - 1

        print(row)

        while l <= r:
            m = (l + r) // 2
            m_val = row[m]

            if target == m_val:
                return True
            elif target < m_val:
                r = m - 1
            else:
                l = m + 1

        return False