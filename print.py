# Summary of python print command based on the book "Learn Python the hardway".
# This is most useful for people from other script languages


print "Mary had a little lamb."                 # 1. print doesn't have ;
print "Its fleece was white as %s." % 'snow'    # 2. printf corresponding
print "And everywhere that Mary went."
print "." * 10 					# 3. print multiplication

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,    # 4. multiple line using ','
print end7 + end8 + end9 + end10 + end11 + end12  # 5. print summation

days = "Mon Tue Wed Thu Fri Sat Sun"              # 6. contatination using ","
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

# 7. print mulitiple lines
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
# 8. Single quote is preferred over double quote.
# 9. Single quote and double quote
print "Double quote " + 'single quote'


print 'This is a double quote " by single quote'

#  %[flags][width][.precision]type
# flags: #: oxX,  0 : 0 padded,   - : left justed
#         : no sign,  +:+/- sign  "space": space
# width:
# digit:

print "Art 1: %5d, Price per Unit: %8.2f " % (453, 59.058)
print "Art 2: %+5d, Price per Unit: %8.2f " % (453, 59.058)
print "Art 3: %-5d, Price per Unit: %8.2f " % (453, 59.058)
print "Art 4: %5d, Price per Unit: %8.4f " % (453, 59.058)
print "Art 5: %      5d, Price per Unit: %8.2f " % (453, 59.058)
print "Art 6: %#5X, Price per Unit: %8.2f " % (453, 59.058)

''' Answer Jesse's question:  difference %5d vs %    5d
'''

#  add positive and negative +/-
print ("%+2d" % (42))
#  add one   white space in front of the number
print ("% 2d" % (42))
#  multiple white space addes *one* white space in front of the number
print ("%       2d" % (42))
#  right aligned
print ("%2d" % (42))

''' Here are the output
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese Burger
Here are the days:  Mon Tue Wed Thu Fri Sat Sun
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug

There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.

Double quote single quote
This is a double quote " by single quote
Art 1:   453, Price per Unit:    59.06
Art 2:  +453, Price per Unit:    59.06
Art 3: 453  , Price per Unit:    59.06
Art 4:   453, Price per Unit:  59.0580
Art 5:   453, Price per Unit:    59.06
Art 6: 0X1C5, Price per Unit:    59.06
+42
 42
 42
42

'''
