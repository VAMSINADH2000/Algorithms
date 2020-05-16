def bubblesort(a):
     for i in range(len(a)):
          for j in range(0,len(a)-i-1):
               if(a[j]>a[j+1]):
                    a[j],a[j+1] = a[j+1],a[j]
               
     print(a)
b = [2,5,4,1,0,87,21,34,6,78,123,56,25]
bubblesort(b)
               
     
