colors = ['red','blue','green','yellow','black']
states = ['andhra','karnataka','tamilnadu','kerala','telangana']
neighbors={}
neighbors['andhra']=['karnataka','tamilnadu','telangana']
neighbors['karnataka']=['andhra','tamilnadu','kerala']
neighbors['tamilnadu']=['andhra','karnataka','kerala']
neighbors['kerala']=['karnataka','tamilnadu']
neighbors['telangana']=['andhra','tamilnadu']

color_of_states={}
def promising(state,color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = color_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True
def get_color_for_state(state):
    for color in colors:
        if promising(state,color):
            return color
def main():
    for state in states:
        color_of_states[state] = get_color_for_state(state)
    print(color_of_states)
main()
