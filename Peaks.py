def solution(A):
    P=[]
    for i in range(1,len(A)-1):
        if (A[i]>A[i-1] and A[i]>A[i+1]):
            P.append(i)
    if len(P)==0:
        return 0
    for k in range(len(P),0,-1):
        if len(A)%k!=0:
                continue

        lenslice=len(A)//k
        slices =[0]*k
        ss=0

        for ip in P:
            slice_id=ip//lenslice
            if slices[slice_id]==0:
                slices[slice_id]=1
                ss += 1
        if ss == k:
            return k
    return 0
    pass