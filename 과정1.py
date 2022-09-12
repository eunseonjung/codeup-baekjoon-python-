#https://codeup.kr/problem.php?id=4711&rid=0
#기차 안에 사람이 가장 많을 때의 사람 수 
#입력
a, b=map(int,input().split())
c, d=map(int,input().split())
e, f=map(int,input().split())
g, h=map(int,input().split())

print(a,b,c,d,e,f,g,h)

for i in range(30):
  print("_",end="")

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

