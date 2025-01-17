class player:
    '''
    Multi-state Finite state machine to represent the player
    '''
    def __init__(self):
        self.active_states = set()

    def add_state(self, state):
        self.active_states.add(state)

    def remove_state(self, state):
        self.active_states.discard(state)

    def is_state_active(self, state):
        return state in self.active_states

    def get_active_states(self):
        return self.active_states.copy()
