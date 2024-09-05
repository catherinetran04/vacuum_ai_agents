# `Reflex Vacuum Agent`
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
