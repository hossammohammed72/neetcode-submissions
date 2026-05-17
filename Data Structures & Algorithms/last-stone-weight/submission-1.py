class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heappush(heap, item):
            return heapq.heappush(heap, -item)
        def heappop(heap):
            return -heapq.heappop(heap)
        head = []
        for i in range(len(stones)):
            heappush(head,stones[i])
        while len(head) >1:
            first = heappop(head)
            second = heappop(head)
            if first > second:
                heappush(head,first-second)
        if len(head):
            return -head[0]
        return 0


        