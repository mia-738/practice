import random
a=random.randrange(1,150)
b=random.randrange(0,100)
d=random.randrange(0,100)
x=160
c_hp=1500
m_hp=1500
while c_hp!=0 or m_hp!=0:
    print("敵のHP:"+str(c_hp)+"\n自分のHP:"+str(m_hp))
    print("威力"+str(a)+"命中率"+str(b)+"の技が使える。\n攻撃しますか？")
    print("攻撃:1  守る:2")
    while True:
        c=int(input())
        if c==1:
            if c<f:
                m_hp=m_hp-x
                print("\n外れた!!\n")
                break
            else:
                c_hp=c_hp-a
                print("当たった!!")
                break
        if c==2:
            print("敵の攻撃をよけた!!")
            break
    a=123*a%150
    b=123*b%100
    d=123*d%100
if c_hp==0:
    print("\n勝った!!")
else:
    print("\n負けた!!")
