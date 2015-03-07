
##################
# Status Effects #
##################

def make_slow(action):
    """Return a new action method that calls action every other turn.

    action -- An action method of some Bee
    """
    def new(self, colony):
        if colony.time % 2 == 1:
            pass
        else:
            action(colony)

    return new

def make_stun(action):
    """Return a new action method that does nothing.

    action -- An action method of some Bee
    """
    def new(self, colony):
        pass

    return new

def apply_effect(effect, bee, duration):
    """Apply a status effect to a Bee that lasts for duration turns."""
    "*** YOUR CODE HERE ***"

    count = 0
    original = bee.action
    modified = effect(original)

    def new_action(colony):
        nonlocal count      
        if duration > count:
            count += 1
            return modified(bee, colony)
        else:
            return original(colony)

    bee.action = new_action


class SlowThrower(ThrowerAnt):
    """ThrowerAnt that causes Slow on Bees."""

    name = 'Slow'
    "*** YOUR CODE HERE ***"
    implemented = True

    def throw_at(self, target):
        if target:
            apply_effect(make_slow, target, 3)


class StunThrower(ThrowerAnt):
    """ThrowerAnt that causes Stun on Bees."""

    name = 'Stun'
    "*** YOUR CODE HERE ***"
    food_cost = 6
    implemented = True

    def throw_at(self, target):
        if target:
            apply_effect(make_stun, target, 1)