class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = sum(customer for customer, grumpy_status in zip(customers, grumpy) if grumpy_status == 0)
        max_extra_satisfied = 0
        window_extra_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                window_extra_satisfied += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                window_extra_satisfied -= customers[i - minutes]
            max_extra_satisfied = max(max_extra_satisfied, window_extra_satisfied)
        return total_satisfied + max_extra_satisfied