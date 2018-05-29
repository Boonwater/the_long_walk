def starve(pc):
    for _ in range(pc.sLVL):
        pc.eLVL += 1
        pc.hp -= 2
        pc.insanity += 10

def dehydrate(pc):
    for _ in range(pc.wLVL):
        pc.eLVL += 2
        pc.hp -= 3
        pc.insanity += 20

def exhaust(pc):
    for _ in range(pc.eLVL):
        pc.maxDistance -= 4
        pc.sleepNeed += 2