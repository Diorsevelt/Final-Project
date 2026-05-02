

print("MBTIMATTER cares for your personality. Find out now.")


choice = input("Do you want to enter your name? (Y/N): ").upper()

if choice == "Y":
    name = input("PLEASE GIVE YOUR FULL NAME: ")

elif choice == "N":
    name = "User"

else:
    print("INVALID INPUT. AUTOMATICALLY SET TO DEFAULT.")
    name = "User"

print("Hello,", name)
print("ANSWER EACH QUESTION WITH A OR B")



I = 0
E = 0
S = 0
N = 0
T = 0
F = 0
J = 0
P = 0


print("\nQUESTION 1: What do you prefer?")
print("A. Spending time alone")
print("B. Spending time with friends")
answer = input("Answer: ").upper()

if answer == "A":
    I = I + 1
else:
    E = E + 1

print("\nQUESTION 2: After a long day, you recharge by:")
print("A. Quiet time")
print("B. Socializing")
answer = input("Answer: ").upper()

if answer == "A":
    I = I + 1
else:
    E = E + 1

print("\nQUESTION 3: In class, you:")
print("A. Think before speaking")
print("B. Speak freely")
answer = input("Answer: ").upper()

if answer == "A":
    I = I + 1
else:
    E = E + 1

print("\nQUESTION 4: You enjoy:")
print("A. Small groups")
print("B. Large gatherings")
answer = input("Answer: ").upper()

if answer == "A":
    I = I + 1
else:
    E = E + 1

print("\nQUESTION 5: You are more:")
print("A. Reserved")
print("B. Outgoing")
answer = input("Answer: ").upper()

if answer == "A":
    I = I + 1
else:
    E = E + 1


print("\nQUESTION 6: You focus more on:")
print("A. Facts")
print("B. Ideas")
answer = input("Answer: ").upper()

if answer == "A":
    S = S + 1
else:
    N = N + 1

print("\nQUESTION 7: You prefer:")
print("A. Practical tasks")
print("B. Imaginativasks")
answer = input("Answer: ").upper()

if answer == "A":
    S = S + 1
else:
    N = N + 1

print("\nQUESTION 8: You trust:")
print("A. Experience")
print("B. Intuition")
answer = input("Answer: ").upper()

if answer == "A":
    S = S + 1
else:
    N = N + 1

print("\nQUESTION 9: You notice:")
print("A. Details")
print("B. Patterns")
answer = input("Answer: ").upper()

if answer == "A":
    S = S + 1
else:
    N = N + 1

print("\nQUESTION 10: You prefer instructions that are:")
print("A. Clear and step-by-step")
print("B. Flexible and open")
answer = input("Answer: ").upper()

if answer == "A":
    S = S + 1
else:
    N = N + 1



print("\nQUESTION 11: You decide based on:")
print("A. Logic")
print("B. Feelings")
answer = input("Answer: ").upper()

if answer == "A":
    T = T + 1
else:
    F = F + 1

print("\nQUESTION 12: You value more:")
print("A. Fairness")
print("B. Harmony")
answer = input("Answer: ").upper()

if answer == "A":
    T = T + 1
else:
    F = F + 1

print("\nQUESTION 13: When giving feedback:")
print("A. Honest")
print("B. Gentle")
answer = input("Answer: ").upper()

if answer == "A":
    T = T + 1
else:
    F = F + 1

print("\nQUESTION 14: You are more:")
print("A. Objective")
print("B. Compassionate")
answer = input("Answer: ").upper()

if answer == "A":
    T = T + 1
else:
    F = F + 1

print("\nQUESTION 15: You prefer:")
print("A. Rules")
print("B. People")
answer = input("Answer: ").upper()

if answer == "A":
    T = T + 1
else:
    F = F + 1


print("\nQUESTION 16: You prefer:")
print("A. Planning")
print("B. Going with the flow")
answer = input("Answer: ").upper()

if answer == "A":
    J = J + 1
else:
    P = P + 1

print("\nQUESTION 17: Your work style:")
print("A. Organized")
print("B. Flexible")
answer = input("Answer: ").upper()

if answer == "A":
    J = J + 1
else:
    P = P + 1

print("\nQUESTION 18: Deadlines:")
print("A. Finish early")
print("B. Last-minute")
answer = input("Answer: ").upper()

if answer == "A":
    J = J + 1
else:
    P = P + 1

print("\nQUESTION 19: You like:")
print("A. Structure")
print("B. Freedom")
answer = input("Answer: ").upper()

if answer == "A":
    J = J + 1
else:
    P = P + 1

print("\nQUESTION 20: You are:")
print("A. Decisive")
print("B. Adaptable")
answer = input("Answer: ").upper()

if answer == "A":
    J = J + 1
else:
    P = P + 1

if I > E:
    letter1 = "I"
else:
    letter1 = "E"

if S > N:
    letter2 = "S"
else:
    letter2 = "N"

if T > F:
    letter3 = "T"
else:
    letter3 = "F"

if J > P:
    letter4 = "J"
else:
    letter4 = "P"

personality = letter1 + letter2 + letter3 + letter4

print("\n-----------------------------")
print("RESULTS FOR:", name)
print("Your MBTI Type is:", personality)

print("\nI:", I, "| E:", E)
print("S:", S, "| N:", N)
print("T:", T, "| F:", F)
print("J:", J, "| P:", P)

print("\nThis is for self-awareness only.")


if personality == "INTJ":
    print("\nType: INTJ (The Strategist)")
    print("Future Jobs: Engineer, Scientist, Architect")
    print("Group Role: Planner / Leader")
    print("Study Method: Independent study")

elif personality == "INTP":
    print("\nType: INTP (The Thinker)")
    print("Future Jobs: Programmer, Researcher, Analyst")
    print("Group Role: Idea Generator")
    print("Study Method: Concept-based learning")

elif personality == "ENTJ":
    print("\nType: ENTJ (The Commander)")
    print("Future Jobs: Manager, CEO, Lawyer")
    print("Group Role: Leader")
    print("Study Method: Structured planning")

elif personality == "ENTP":
    print("\nType: ENTP (The Debater)")
    print("Future Jobs: Entrepreneur, Marketer, Inventor")
    print("Group Role: Innovator")
    print("Study Method: Discussion-based learning")

elif personality == "INFJ":
    print("\nType: INFJ (The Advocate)")
    print("Future Jobs: Counselor, Psychologist, Writer")
    print("Group Role: Advisor")
    print("Study Method: Reflection")

elif personality == "INFP":
    print("\nType: INFP (The Mediator)")
    print("Future Jobs: Artist, Writer, Designer")
    print("Group Role: Supporter")
    print("Study Method: Creative learning")

elif personality == "ENFJ":
    print("\nType: ENFJ (The Protagonist)")
    print("Future Jobs: Teacher, Coach, Leader")
    print("Group Role: Motivator")
    print("Study Method: Group learning")

elif personality == "ENFP":
    print("\nType: ENFP (The Campaigner)")
    print("Future Jobs: Journalist, Actor, Entrepreneur")
    print("Group Role: Energizer")
    print("Study Method: Interactive learning")

elif personality == "ISTJ":
    print("\nType: ISTJ (The Inspector)")
    print("Future Jobs: Accountant, Engineer")
    print("Group Role: Organizer")
    print("Study Method: Routine learning")

elif personality == "ISFJ":
    print("\nType: ISFJ (The Protector)")
    print("Future Jobs: Nurse, Teacher")
    print("Group Role: Helper")
    print("Study Method: Step-by-step learning")

elif personality == "ESTJ":
    print("\nType: ESTJ (The Executive)")
    print("Future Jobs: Manager, Officer")
    print("Group Role: Director")
    print("Study Method: Structured learning")

elif personality == "ESFJ":
    print("\nType: ESFJ (The Consul)")
    print("Future Jobs: HR, Teacher")
    print("Group Role: Coordinator")
    print("Study Method: Group study")

elif personality == "ISTP":
    print("\nType: ISTP (The Virtuoso)")
    print("Future Jobs: Technician, Engineer")
    print("Group Role: Problem Solver")
    print("Study Method: Hands-on learning")

elif personality == "ISFP":
    print("\nType: ISFP (The Adventurer)")
    print("Future Jobs: Artist, Musician")
    print("Group Role: Creative Contributor")
    print("Study Method: Visual learning")

elif personality == "ESTP":
    print("\nType: ESTP (The Entrepreneur)")
    print("Future Jobs: Business, Athlete")
    print("Group Role: Action Taker")
    print("Study Method: Real-world practice")

elif personality == "ESFP":
    print("\nType: ESFP (The Entertainer)")
    print("Future Jobs: Performer, Host")
    print("Group Role: Morale Booster")
    print("Study Method: Fun learning")



