
def MergeSort(A, index):
  if(len(A) < 2):
    return A

  mid = len(A) / 2
  larray = MergeSort(A[0:mid], index)
  rarray = MergeSort(A[mid:len(A)], index)
  marray = Merge(larray, rarray, index)

  return marray

def Merge(A, B, index):
  C = list()
  i = j = 0

  for x in xrange(len(A) + len(B)):

    if(i < len(A) and (j >= len(B) or A[i][index] < B[j][index])):
      C.append(A[i])
      i += 1
    else:
      C.append(B[j])
      j += 1

  return C
