import taichi as ti

ti.init()
a = ti.var(dt=ti.f32,shape =(42, 63))
b = ti.Vector(3,dt=ti.f32,shape=4) 

C = ti.Matrix(2,2,dt=ti.f32,shape=(3,5))

loss = ti.var(dt=ti.f32,shape=())

a [3,4] = 1
print('a [ 3 , 4] =', a[3,4])

b[2]=[6,7,8]
print('b [ 0 ] =',b[0][0],b[0][1],b[0][2])

loss[None]=3

print(loss[None])