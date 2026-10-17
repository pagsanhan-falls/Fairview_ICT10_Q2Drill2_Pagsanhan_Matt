from pyscript import document

# Predefined sets for each grade
Grade7 = {"Joshua", "Erik", "Kyle", "Matthew"}
Grade8 = {"Damian", "Hexum", "Sean"}
Grade9 = {"Avian", "Archie", "Bam", "Lebron", "John"}
Grade10 = {"Kater", "Leon", "Vito", "Gandy", "Handy", "Sandy", "Randy"}

def add_member(event):
    # Gets the inputed values from the form
    fname = document.querySelector("#first_name").value
    lname = document.querySelector("#last_name").value

    # Create a new set for the added member
    new_member_set = {f"{fname} {lname}"}

    # Combins the sets using the set union operator (|)
    all_members = Grade7 | Grade8 | Grade9 | Grade10 | new_member_set

    # Sort the members by alphabetical A-Z
    members_list = "<br>".join(sorted(all_members))

    # Total members count
    total_members = len(all_members)


    document.querySelector("#output1").innerHTML = f"<b>Total Members:</b> {total_members}<br><br><b>Members List:</b><br>{members_list}"