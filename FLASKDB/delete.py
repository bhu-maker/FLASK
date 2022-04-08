from app import parent,child,session
print(f"parents {session.query(parent).all()}")
print(f"children {session.query(child).all()}")


parent_to_delete=session.query(parent).filter(parent.id==1).first()

print(parent_to_delete)
print(parent_to_delete.child)