objects = [[] for _ in range(4)]

# fill here
collision_pairs = {}

def add_collision_pair(group, a = None , b = None): # a, b 사이에 충돌 검사 필요 등록
    if group not in collision_pairs:
        print(f'Added new group {group}')
        collision_pairs[group] = [ [], [] ]
    if a :
        collision_pairs[group][0].append(a)
    if b :
        collision_pairs[group][1].append(b)

def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()

# fill here
def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()



# fill here
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False


    return True

