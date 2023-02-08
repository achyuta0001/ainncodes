import random

def display(room):
    print(room)

room=[
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
]

print("all  roomas are dirty")
display(room)
x=0
y=0

while x < 4:
    while y < 4:
        room[x][y]=random.choice([0,1])
        y=y+1
    x=x+1
    y=0

print("be4 cleaning")
display(room)
x=0
y=0
z=0

while x < 4:
    while y < 4:
        if room[x][y]==1:
            print("vaccum in",x,y)
            room[x][y]=0
            print("clean",x,y)
            z=z+1
        y=y+1
    x=x+1
    y=0
display(room)
perf=(100-((z/16)*100))
print(perf)