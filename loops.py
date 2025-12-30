#Loop through a tuple
mytuple = ("Nairobi", "Cairo", "Lagos", "Rabat")
for x in mytuple:
  print(x)  #output each item in the tuple :
            #Nairobi
            #Cairo
            #Lagos
            #Rabat

#Loop through the index numbers
for i in range(len(mytuple)):
  print(mytuple[i]) #output each item in the tuple :
                    #Nairobi
                    #Cairo
                    #Lagos
                    #Rabat            

#Loop through both index and value
for i in enumerate(mytuple):
  print(i)  #output each item in the tuple with its index :
            #(0, 'Nairobi')
            #(1, 'Cairo')
            #(2, 'Lagos')
            #(3, 'Rabat')