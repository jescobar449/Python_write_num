#Name: Jose Melquiades Escobar

#Define main ():
def main ():
    #Open a file named as num_list in write mode.
    output_file = open ('num_list.text', 'w')
    
    #Use for loop to write a range of numbers from 1 through 101 into the file.
    for num in range ( 1, 101):
        output_file.write(str(num))     #write each number 
        output_file.write('\n')         #add a new line after each number
    
    #Close file
    output_file.close()

#End main()
main ()
