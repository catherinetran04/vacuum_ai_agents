This project involves installing and running the aima code. Within the agents.py module, we take a look at the ReflexVacuumAgent class:
  def ReflexVacuumAgent ():
  """
  [ Figure 2.8]
  A reflex agent for the two - state vacuum environment .
  >>> agent = ReflexVacuumAgent ()
  >>> environment = TrivialVacuumEnvironment ()
  >>> environment . add_thing ( agent )
  >>> environment . run ()
  >>> environment . status == {(1 ,0): ’ Clean ’ , (0 ,0) : ’Clean ’}
  True
  """
