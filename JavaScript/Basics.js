var variable1;
variable1 = 'hello'
var var2 = 'Hello World'

console.log('var2', var2)

// array
var array = [1,2,3,4,5]
console.log('array', array)

var array1 = [1,'two', var2, 3]
console.log('array1', array1)
console.log('array1[1]', array1[1])

// objects or a dictionary in python
var dict1 = {name: "Drake", age:16}
console.log('dict1', dict1)

var dict2 = {
  age: 18,
  Color: "grey",
  likes: ["cake", "milk"],
  "Bday dates": {"month": 7, "day": 17, year: 1994}
}
// you don't need quotes ''  for the key, only if you have whitespaces, name  vs  'person name'
delete dict2.Color
console.log('dict2.age', dict2.age)

// if/else if/else
x = 1
y = 2
if (y == x) { console.log("Equal") } // checks if x = y
else if (x != y) { console.log("Not equal") }  //  chcks if x not equal y
else { console.log("Dunno") } 

// function
function hello(){console.log("Hellow")}
hello()
function func1(str) {console.log(str) }
func1("passing in arg")


// while loop
var thing = 0;
while (y < 10) {
    console.log(y);
    y += 1;
}

// for loop
for (var x = 0; x < 10; x += 1) {
    console.log('for loop:', x);
}

// DOUBLE FOR LOOP ALL THE WAY!!!!
for (var x = 0; x < 10; x++) {
    for (var y = 0; y < 15; y++) {
        console.log('double for loop:', x, y);
    }
}

var loopList = [1,2,3,5,2,59,'hi', 'lol', 'um']
for (var i = 0; i < loopList.length; i++) {console.log('list.length:', loopList[i]) }

// loop through list
for (i of loopList) {console.log('of:', i)}
// similar to for i in loopList: print(i) in python



