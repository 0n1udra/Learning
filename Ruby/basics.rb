# Data
int1 = 1 # integer
float1 = 3.14 # float
str1 = 'hi' # string
bool1 = false # boolean
array1 = [1,2,3, 'four','five','six',int1,float1] # an array or list
classHash1 = { '1' => 'one', '2' => 'two', 'age' => 12, 'name' => 'bob' } # basically a dictonary
# printing
puts int1 # prints on new line
print str1 # prints on same line
print ' see'
puts array1[1]
puts classHash1['1']
puts ""

name = 'Drake'
puts "Hello #{name}"


# methods/statements
# if, elsif, else statment
x = 1
if x == 1
	print 'x is 1'
elsif x == 2
	print 'x is 2'
else
	print 'x is something else'
end

# until 
puts ""
y = 5
until y == 0
	print y
	y -= 1
end

puts ""
# unless
z = 10
unless z == 11
	puts 'z is not 11'
end

# while loop
xz = 1
while xz < 10
	puts xz
	xz += 1
end
puts ""

# for loop
for i in 1..10
	print i
end

for i in 1..10
	if i == 5 then
		break
	end
	print i
end
# Comparators
# && = and. \\ = or. ! = not

10.times do puts " lol" end