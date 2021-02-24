# Print N Lowest Numbers

Write C programm that prints the n lowest numbers from a given list of numbers
that come via stdin input.

```
void swap(int *xp, int *yp) {
    int temp = *xp; 
    *xp = *yp; 
    *yp = temp; 
}

void selectionSort(int arr[], int n) {
    int i, j, min_idx; 
    for (i = 0; i < n-1; i++) { 
      min_idx = i; 
      for (j = i+1; j < n; j++) {
        if (arr[j] < arr[min_idx]) {
          min_idx = j;
        }
      }
      swap(&arr[min_idx], &arr[i]); 
    }
}

void PrintNLowestNumbers(int arr[], unsigned int length, unsigned short nLowest) {
  int i;
  selectionSort(arr, length);
  for (i = 0; i < nLowest; i++) {
    printf("%d ", arr[i]);
  }
}
```