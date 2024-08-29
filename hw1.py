'''
Adapted from Professor Watters' code


'''

import sys 
sys.path.append('aima-python')
from agents import *

class HW1:

    def problem_a(self):

        agent = ReflexVacuumAgent()
        TraceAgent(agent)

        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status

    def problem_b(self):

        agent = ModelBasedVacuumAgent()
        TraceAgent(agent)

        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status

    def problem_c(self):

        agent = RandomVacuumAgent()
        TraceAgent(agent)

        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status

    def problem_d(self):
        environment = TrivialVacuumEnvironment
        agents = [ModelBasedVacuumAgent, RandomVacuumAgent, ReflexVacuumAgent]
        result = compare_agents(environment, agents)
        return result


def main():
    hw1 = HW1()
    print("Problem a:", hw1.problem_a())
    print("Problem b:", hw1.problem_b())
    print("Problem c:", hw1.problem_c())
    print("Problem d:", hw1.problem_d())

if __name__ == '__main__':
    main()
