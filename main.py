from person_factory import PersonFactory
from family_tree import FamilyTree

factory = PersonFactory()
factory.read_files()
tree = FamilyTree(factory)
print("Reading files...")
print("Generating family tree...")
tree.generate_tree()
tree.interactive_query()
