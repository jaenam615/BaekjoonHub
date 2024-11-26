function solution(arr)
{
    var answer = [];

    for(let idx = 0; idx < arr.length; idx ++){
        if (arr[idx] == arr[idx +1]){
            arr[idx] = -1;
        }
    }
    
    answer = arr.filter(i => i != -1);
    
    return answer;
}