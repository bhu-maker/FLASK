from unicodedata import name
from app import parent,child,session
  
#parent1=parent(name="parent 1")

#parent2=parent(name="parent 2")

#session.add_all(
#    [parent1,parent2]
#)

#session.commit()
####
#parents=session.query(parent).all()

#print(parents)
#####

parent1=session.query(parent).filter(parent.id==1).first()
print(parent1)

#child1=child(name="child 1",parent=parent1)
#session.add(child1)
#session.commit()
#print(parent1.child)

child2=child(name="child 2",parent=parent1)
session.add(child2)
session.commit()

print(parent1.child)
