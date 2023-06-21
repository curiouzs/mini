arr_time=float(input("Enter the mean inter arrival time of objects from Feeder (in secs): ")) 
ser_time=float(input("Enter the mean inter service time of Lathe Machine (in secs) : ")) 
Robot_time=float(input("Enter the Additional time taken for the Robot (in secs) : ")) 
lam=1/arr_time
mu=1/(ser_time+Robot_time)
print("------------------------	") 
print("Single Server with Infinite Capacity - (M/M/1):(oo/FIFO)") 
print("--------------------------	") 
print("The mean arrival rate per second : %0.2f "%lam)
print("The mean service rate per second : %0.2f "%mu)
if (lam <  mu):
  Ls=lam/(mu-lam) 
  Lq=Ls-lam/mu 
  Ws=Ls/lam 
  Wq=Lq/lam
  print("Average number of objects in the system : %0.2f "%Ls) 
  print("Average number of objects in the conveyor : %0.2f "%Lq)
  print("Average waiting time of an object in the system : %0.2f secs"%Ws)
  print("Average waiting time of an object in the conveyor : %0.2f secs"%Wq)
  print("Probability that the system is busy : %0.2f "%(lam/mu) ) 
  print("Probability that the system is empty : %0.2f "%(1-lam/mu) )
else:
  print("Warning! Objects Over flow will happen in the conveyor")
print("	")
