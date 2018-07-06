file = open("teams.txt","r")

outfile=""
file.readline()
outfile=outfile+file.readline()
file.readline()
outfile=outfile+file.readline()

file=open("teams.txt","w")
file.write(outfile)
file.close()
