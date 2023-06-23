def solution(arr, queries):
    
    ans=[]
    for query in queries :
        s = query[0]
        e = query[1]
        k = query[2]
        result = []
        
        for i in range(s,e+1):
            if arr[i] > k :
                result.append(arr[i])
                   
                
        if len(result) == 0 :
            ans.append(-1)
            
        else :
            result.sort()
            ans.append(result[0])
        
    return ans