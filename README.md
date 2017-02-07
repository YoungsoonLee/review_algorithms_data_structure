## Review Algorithms  
___  

### 1. 이진 검색(Binary Search)  
순차적인 항목 리스트에서 원하는 항목을 찾기에 효율적인 알고리즘.이 검색법은 후보 범위를 하나로 좁힐 때까지 찾고자 하는 항목을 포함하고 있는 리스트를 반으로 나누는 과정을 계속 반복.  

	Time complexity : O(logN)

### 2. 선택 정렬(Selected Sort)  
주어진 데이터에서 최소값을 찾이서 그 값을 맨 앞에 위치한 값과 바꾼다. 그 후 맨 처음 위치한 값을 뺀 나머지 값들을 같은 방법으로 바꾼다.  

	Time complexity : O(N^2)	


### 3. 삽입 정렬(Insertion Sort)
첫 숫자는 두고 두 번째 자리 숫자부터 그 숫자가 첫 숫자보다 비교해 크면 첫 숫자 오른쪽에, 작으면 왼쪽에 넣은 후 다시 세 번째 자리 숫자를 뽑아서 앞의 두 숫자와 크기를 비교해서 알맞은 자리에 넣는 것을 반복 해서 정렬 하는 알고리즘.  

	Time complexity : O(N^2)	


### 4. Merge Sort
Base on Divide and Conquer.  
>	1. Divide by finding the number q of the position midway between p and r.  
>	   Do this step the same way we found the midpoint in binary search: add p and r, divide by 2, and round down.  

> 	2. Conquer by recursively sorting the subarrays in each of the two subproblems created by the divide step.  
>	   that is, recursively sort the subarray array[p..q] and recursively sort the subarray array[q+1..r].  

>	3. Combine by merging the two sorted subarrays back into the single sorted subarray array[p..r]  

>	- condition of exit: p < r  
>	- need to more memory  


	Time complexity : O(NlogN)  

