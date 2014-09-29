from Tkinter import Tk, Button, Entry, END, Label
import Tkinter
import math
import decimal
root = Tk()
#configures gui
root.title("Boat Calculator")
root.geometry("300x250")
# root.configure(background="blue")
Label(root, text="LOA:").grid(row=0)
Label(root, text="LWL:").grid(row=1)
Label(root, text="Beam:").grid(row=2)
Label(root, text="Displacement:").grid(row=3)
Label(root, text="Sail Area:").grid(row=4)


def click():
        """Handle button click"""

        # Get the input
        val1 = myentry1.get()
        val2 = myentry2.get()
        val3 = myentry3.get()
        val4 = myentry4.get()
        val5 = myentry5.get()
        # Defines equations
        hull = (1.34 * (float(myentry2.get()) )**.5 )
        disp = ((float(myentry4.get())/(2240))/ ((.01 * (float(myentry2.get())))**3))
        sail = (float(myentry5.get())/((float(myentry4.get())/64)**.67))
        capi = (float(myentry3.get())/((float(myentry4.get())/64)**.33))
        comi = (float(myentry4.get()) / (.65*(.7*(float(myentry2.get()))+(.3*(float(myentry1.get()))))*(float(myentry3.get())**1.33)))

        try:
        # Try to make it a float
                val1 = float(val1)
                val2 = float(val2)
                val3 = float(val3)
                val4 = float(val4)
                val5 = float(val5)
                print "LOA:"
                print round(val1, 2) 
                print"\nLWL:"
                print round(val2, 2)
                print "\nBeam:"
                print round(val3, 2)
                print "\nDisplacement:"
                print round(val4, 2)
                print "\nSail area:"
                print round(val5, 2)
                print "__________\n"
                print "Hull speed"
                print round(hull, 2)
                print "\nD/L:"
                print round(disp, 2)
                print "\nSA/D:"
                print round(sail, 2)
                print "\nCapsize Index:"
                print round(capi, 2)
                print "\nComfort index:"
                print round(comi, 2)


        except ValueError:
        # Print this if the input cannot be made a float
                print "incorrect input"

        # Clear the entrybox
        myentry1.delete(0, END)
        myentry2.delete(0, END)
        myentry3.delete(0, END)
        myentry4.delete(0, END)
        myentry5.delete(0, END)

# Made this to demonstrate
Button(text="Calculate", command=click).grid(row=6, column=1)
Button(root, text='Quit', command=root.quit).grid(row=5, column=0)
myentry1 = Entry()
myentry1.grid(row=0, column=1)
myentry2 = Entry()
myentry2.grid(row=1, column=1)
myentry3 = Entry()
myentry3.grid(row=2, column=1)
myentry4 = Entry()
myentry4.grid(row=3, column=1)
myentry5 = Entry()
myentry5.grid(row=4, column=1)



root.mainloop()
