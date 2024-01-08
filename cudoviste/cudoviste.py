x = input().split()
a = int(x[0])
b = int(x[1])
matrix = []
counter0 = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
for _ in range(a):
    row = input()
    matrix.append(row)
for i in range(a-1):
    for j in range(b-1):
        if matrix[i][j]!="#":
            if (matrix[i][j]=="." and matrix[i][j+1]=="." and matrix[i+1][j]=="." and matrix[i+1][j+1]=="."):
                counter0+=1
            elif (matrix[i][j]=="X" and matrix[i][j+1]=="." and matrix[i+1][j]=="." and matrix[i+1][j+1]== ".") or (matrix[i][j]=="." and matrix[i][j+1]=="X" and matrix[i+1][j]=="." and matrix[i+1][j+1]== ".") or (matrix[i][j]=="." and matrix[i][j+1]=="." and matrix[i+1][j]=="X" and matrix[i+1][j+1]== ".") or(matrix[i][j]=="." and matrix[i][j+1]=="." and matrix[i+1][j]=="." and matrix[i+1][j+1]== "X"):
                    counter1+=1
            elif (matrix[i][j]=="X" and matrix[i][j+1]=="X" and matrix[i+1][j]=="X" and matrix[i+1][j+1]== ".") or (matrix[i][j]=="." and matrix[i][j+1]=="X" and matrix[i+1][j]=="X" and matrix[i+1][j+1]== "X") or (matrix[i][j]=="X" and matrix[i][j+1]=="." and matrix[i+1][j]=="X" and matrix[i+1][j+1]== "X") or(matrix[i][j]=="X" and matrix[i][j+1]=="X" and matrix[i+1][j]=="." and matrix[i+1][j+1]== "X"):
                    counter3+=1   
            elif (matrix[i][j]=="X" and matrix[i][j+1]=="X" and matrix[i+1][j]=="X" and matrix[i+1][j+1]== "X"):
                    counter4+=1
            elif (matrix[i][j]=="X" and matrix[i][j+1]=="X" and matrix[i+1][j]=="." and matrix[i+1][j+1]== ".") or (matrix[i][j]=="." and matrix[i][j+1]=="X" and matrix[i+1][j]=="X" and matrix[i+1][j+1]== ".") or (matrix[i][j]=="." and matrix[i][j+1]=="." and matrix[i+1][j]=="X" and matrix[i+1][j+1]== "X") or(matrix[i][j]=="X" and matrix[i][j+1]=="." and matrix[i+1][j]=="." and matrix[i+1][j+1]== "X") or (matrix[i][j]=="X" and matrix[i][j+1]=="." and matrix[i+1][j]=="X" and matrix[i+1][j+1]== ".") or (matrix[i][j]=="." and matrix[i][j+1]=="X" and matrix[i+1][j]=="." and matrix[i+1][j+1]== "X"):
                    counter2+=1   
     
                    
print(counter0)
print(counter1)
print(counter2)
print(counter3)
print(counter4)