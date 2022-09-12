a, b=map(int,input().split())
c, d=map(int,input().split())
e, f=map(int,input().split())
g, h=map(int,input().split())

list_result=[]
#과정
#1번역 거친 후 결과 result1
result1=b
list_result.append(result1)
#2번 역 거친 후 결과 result2
result2=result1-c+d
list_result.append(result2)
#3번 역 거친 후 결과 result3
result3=result2-e+f
list_result.append(result3)
#4번 역 거친 결과 result4
result4=result3-g
list_result.append(result4)

#출력
print("리스트",list_result)
print(max(list_result))

