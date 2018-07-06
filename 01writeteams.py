file = open("teams.txt","w")

for i in range(5):
    team= input("Please input team name: ") + "\n"
    file.write(team)

file.close()

