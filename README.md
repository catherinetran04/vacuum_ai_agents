# `Agents in a Trivial Vacuum Environment`
This project involves installing and running the aima code. Within the agents.py module, we take a look at the ReflexVacuumAgent class:

```
def ReflexVacuumAgent ():
"""
[ Figure 2.8]
A reflex agent for the two - state vacuum environment .
>>> agent = ReflexVacuumAgent()
>>> environment = TrivialVacuumEnvironment()
>>> environment.add_thing(agent)
>>> environment.run()
>>> environment.status == {(1 ,0):’Clean’ , (0,0) : ’Clean’}
True
"""
```
Loading in agent.py using the interactive python interpreter, there are comments available which show the commands you can use to 
- create a ReflexVacuumAgent object
- create an environment for it
- then run it in the environment

If you wanted to run the agent in that environment for a limited amount of time, you can pass an integer in as a parameter in the
environment.run call (e.g. environment.run(50))

This applies for other agents such as the model based vacuum agent and the random vacuum agent.

## Reflex Vacuum Agent
• Run the ReflexVacuumAgent in the TrivialVacuumEnvironment for 15 steps. Use the
TraceAgent class to print out its perceptions and actions at each time step. Return
the environment status.
```
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Dirty') and does Suck
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does Left
Reflex:  {(0, 0): 'Clean', (1, 0): 'Clean'}
```

## Model Based Vacuum Agent
• Run the ModelBasedVacuumAgent in the TrivialVacuumEnvironment for 15 steps.
Use the TraceAgent class to print out its perceptions and actions at each time step.
Return the environment status.
```
<Agent> perceives ((1, 0), 'Dirty') and does Suck
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does NoOp
Model:  {(0, 0): 'Clean', (1, 0): 'Clean'}
```

## Random Vacuum Agent
• Run the RandomVacuumAgent agent in the TrivialVacuumEnvironment for 15 steps.
Use the TraceAgent class to print out its perceptions and actions at each time step.
Return the environment status.
```
<Agent> perceives ((0, 0), 'Clean') and does Suck
<Agent> perceives ((0, 0), 'Clean') and does Suck
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does NoOp
<Agent> perceives ((1, 0), 'Clean') and does Suck
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does NoOp
<Agent> perceives ((0, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does Left
<Agent> perceives ((0, 0), 'Clean') and does Suck
<Agent> perceives ((0, 0), 'Clean') and does Suck
<Agent> perceives ((0, 0), 'Clean') and does Right
<Agent> perceives ((1, 0), 'Clean') and does Suck
<Agent> perceives ((1, 0), 'Clean') and does Left
Random:  {(0, 0): 'Clean', (1, 0): 'Clean'}

## Compare Agents
• Use the compare agents function to compare the three agents in the trivial environment. Return the results of the comparison.
```
Compare:  [(<function ModelBasedVacuumAgent at 0x11f98f5b0>, 9), (<function RandomVacuumAgent at 0x11f98f400>, -485.7), (<function ReflexVacuumAgent at 0x11f98f520>, -989)]
```
