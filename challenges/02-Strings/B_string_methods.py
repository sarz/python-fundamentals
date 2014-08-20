# We'll start off by grabbing your names from the last file

from A_defining_strings import your_first_name, your_last_name

# Using string methods
# # We're updating our administrative system, so we need to capitalize your last
## name. There's a simple way to do that with a string "method" called .upper()
print your_last_name.upper()
cap_last_name = your_last_name.upper()
print cap_last_name
## Set cap_last_name to an uppercase version of your_last_name



## You can print it to see how it looks



## And we'll need to check how long your name is to make sure there's enough
## space in our database! Be sure to count a space between your first and last
## name, and use the len() function to compute the lengths
print your_first_name, your_last_name
# full_name = str(your_first_name),str(your_last_name)

full_name = "{} {}".format(your_first_name, your_last_name)
print full_name
name_len = len(full_name)
print name_len
## Put the total length of your name in name_len. You can use multiple steps if
## you like.

s = "We'll need {mylen} characters for my name"
print s.format(mylen=len(full_name))

# Another way to do it:
#print "We'll need",name_len, "characters for my name"

## Note that we've been using print with commas. This puts a space between each
## string or variable. But what if we don't want a space? In this case, we can
## append two strings (including variables) using +. See if you can create a
## "last name first" version of your name, with a comma separating the two.
## For example, I'd be "CLARK, Dav"

print cap_last_name + ", " + your_first_name


