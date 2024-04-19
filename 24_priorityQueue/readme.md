### 우선순위 큐 
- 일반 스택과 큐와 비슷한 추상 데이터 타입이지만, 각 항목마다 연관된 우선순위가 있음(우선순위가 같으면 큐의 순서를 따름)
- 힙(완전이진트리)으로 구현
  ```python
  import heapq
  heapq.heappush(heap, data)
  heapq.heappop(heap)   #힙에서 루트 노드 값을 제거 
  heapify(l:list)       #배열(리스트) l를 힙 구주로 만듦
  ```
