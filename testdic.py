import model

model=model.model(100)
arr=model.getvector("110")
print(arr)
for i in range(len(arr)):
    arr[i]=arr[i]+1
print(model.getvector("110"))