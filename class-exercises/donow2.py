import csv 

# open fle in write mode
csvfile= open('donow2.py', 'w')

# create the csv writer 
csvwriter= csv.writer(csvfile, delimiter= ',')

# write to the file 
# create a header
csvwriter.writerow(['winter', 'spring', 'summer', 'fall', 'more fall'])

# for each value of a:
for a in range(1, 101):
  
    # get each value of b:
    for b in range(1, 101):
        hypotenuse= math.sqrt(a**2 + b**2)
        csvwriter.writerow([a, b, hypotenuse])
    
# close the file 
for a in range(1, 101): 
    csvfile.close() 


