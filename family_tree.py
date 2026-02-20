import random
from person_factory import PersonFactory

"""
FamilyTree class
Creates generations of people starting with two and expanding
based on data gatherd in factory
"""


class FamilyTree:
    """
    main data structure will be queue to iterate through 
    people being processed
    """

    def __init__(self, factory):
        self.factory = factory  # reference to PersonFactory
        self.everyone = []  # list of every person objects
        self.queue = []  # queue of all people to process
        self.initial_last_name = None

    def generate_tree(self):
        # create first person born in 1950s
        gender01 = random.choice(['male', 'female'])
        person01 = self.factory.get_person(1950, gender01)
        # store family last name
        self.initial_last_name = person01.last_name
        # add to queue
        self.everyone.append(person01)
        self.queue.append(person01)

        # create second person
        gender02 = random.choice(['male', 'female'])
        person02 = self.factory.get_person(
            1950, gender02, last_name=self.initial_last_name)

        # add to queue
        self.everyone.append(person02)
        self.queue.append(person02)

        # iterate through people in queue
        while len(self.queue) > 0:
            curr_person = self.queue.pop(0)

            # stop if reached 2120
            if curr_person.year_born > 2120:
                continue

            # determine if person gets spouse and children
            self.process_person(curr_person)

    # helper method to determine if current person in queue should get a spouse and children
    def process_person(self, person):
        # skip if already married
        if person.spouse is not None:
            return
        # line for formating generating in colab's gemini AI
        decade = f"{(person.year_born // 10)*10}s"
        marriage_rate = self.factory.get_marriage_rate(decade)

        if random.random() <= marriage_rate:
            # get spouse

            # give random gender and year within 10 years of current person
            spouse_gender = random.choice(['male', 'female'])
            spouse_year = person.year_born + random.randint(-10, 10)
            # give relationship for person.spouse and spouse.spouse
            spouse = self.factory.get_person(spouse_year, spouse_gender)
            # set spouse as person
            person.set_spouse(spouse)
            spouse.set_spouse(person)
            # add spouse to queue
            self.everyone.append(spouse)
            self.queue.append(spouse)

        # determine how many children processed person gets
        birth_rate = self.factory.get_birth_rate(decade)
        min_children = max(1, int(birth_rate - 1.5))
        max_children = int(birth_rate + 1.5)
        num_children = random.randint(min_children, max_children)

        # create child
        for i in range(num_children):
            # calculate child's birth year between parents years 25 and 45
            child_year = random.randint(
                person.year_born + 25, person.year_born + 45)
            # do not make child if birth year is beyond 2120
            if child_year > 2120:
                continue
            # generate random gender and get child
            child_gender = random.choice(['male', 'female'])
            child = self.factory.get_person(
                child_year, child_gender, last_name=self.initial_last_name)
            # add child to spouse and add to queue
            person.add_child(child)
            # check if there is a spouse to add children
            if person.spouse is not None:
                person.spouse.add_child(child)
            # add child to queue regardless
            self.everyone.append(child)
            self.queue.append(child)

    # return total people
    def get_total_people(self):
        return len(self.everyone)

    # total people by decade
    def get_people_by_decade(self):
        # store people in dictionary
        decade_counts = {}
        # line for formating generating in colab's gemini AI
        for person in self.everyone:
            decade = f"{(person.year_born // 10) * 10}s"
            if decade in decade_counts:
                decade_counts[decade] += 1
            else:
                decade_counts[decade] = 1
        return decade_counts

    # get names that are duplicates by full name
    def get_duplicate_names(self):
        # store people in dictionary
        name_counts = {}
        # line for formating generating in colab's gemini AI
        for person in self.everyone:
            full_name = f"{person.first_name} {person.last_name}"
            if full_name in name_counts:
                name_counts[full_name] += 1
            else:
                name_counts[full_name] = 1

        dupes = [name for name, count in name_counts.items() if count > 1]
        return dupes

    # interactive function for user to query tree
    def interactive_query(self):
        while True:
            print("\nAre you interested in:")
            print("[T]otal number of people in the tree")
            print("Total number of people in the tree by [D]ecade")
            print("[N]ames duplicated")
            print("[Q]uit")
            choice = input("> ").strip().upper()

            if choice == "T":
                print(f"\nTotal people in tree: {self.get_total_people()}")

            elif choice == "D":
                decades = self.get_people_by_decade()
                for decade in sorted(decades.keys()):
                    print(f"\n{decade}: {decades[decade]}")

            elif choice == "N":
                dupes = self.get_duplicate_names()
                print(f"\nTotal duplicate names in tree: {len(dupes)}")
                for name in dupes:
                    print(name)

            elif choice == "Q":
                print("\nExiting...")
                break

            else:
                print("Invalid option. Enter T, D, N, or Q")
