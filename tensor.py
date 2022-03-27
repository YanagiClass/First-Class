from string import printable
import tensorflow as tf
#키와 신발사이즈의 관련성
#신발 = a키 + b
#선형회귀 예제구현

tall = 170
shoe = 260

#shoe = tall * a + b

a = tf.Variable(0.1)
b = tf.Variable(0.2)
def lossfunction():
    return tf.square(260 - (tall * a + b)) 

opt = tf.keras.optimizers.Adam(learning_rate=0.1) #경사하강법
for i in range(300):
    opt.minimize(lossfunction, var_list=[a,b])
    print(a.numpy(),b.numpy())


print(tall * a.numpy() + b.numpy())
