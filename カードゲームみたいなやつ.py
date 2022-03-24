import random
a=random.randrange(1,150)
b=random.randrange(0,100)
c=random.randrange(0,100)
d=3
x=160
c_hp=2100
m_hp=2100
while c_hp!=0 or m_hp!=0:
    print("敵のHP:"+str(c_hp)+"\n自分のHP:"+str(m_hp))
    print("威力"+str(a)+"命中率"+str(b)+"の技が使える。\n攻撃しますか？")
    print("攻撃:1 守る:2(後+"d"+回)")
    while True:
        act=int(input())
        if d==0:
            act=1
        if act==1:
            if b<c:
                m_hp=m_hp-x
                print("\n外れた!!\n")
                break
            else:
                c_hp=c_hp-a
                print("\n当たった!!\n")
                break
        if act==2:
            print("\n敵の攻撃をよけた!!\n")
            d-=1
            break
    a=123*a%150
    b=123*b%100
    c=123*c%100
if c_hp==0:
    print("\n勝った!!")
else:
    print("\n負けてしまった!!")
