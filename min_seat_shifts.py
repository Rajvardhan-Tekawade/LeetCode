class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        students.sort()
        seats.sort()
        moves=0
        for i in range(len(seats)):
            moves=moves+abs(seats[i]-students[i])
        return moves