Library for translation in docs... (i18 next) (Weblate)

Resize Observer in React (https://codefrontend.com/resize-observer-react/)

https://www.youtube.com/watch?v=yJDofSGTSPQ

https://www.youtube.com/watch?v=_HkxuxZ5QO0

How to write in README.md ->> https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f

JavaScript HandBook: https://www.freecodecamp.org/news/the-complete-javascript-handbook-f26b2c71719c/
file: ///C:/Users/AdmirDemaj/Downloads/JavaScriptNotesForProfessionals.pdf

-- Vercel which is used to deploy your app from Github
@ https://vercel.com/new/templates

-- Using Composition in React to get rid of prop drilling
@ https://www.youtube.com/watch?v=3XaXKiXtNjw

Comments about this video: For simple examples, I think this works really well. I'd argue for larger examples Context would work better. The solution with composition ends up creating a larger JSX tree at the top level, which again, is fine while it's small. The problem compounds as you continue to get components of components of components.
I think in an ideal world there's a little bit of both. But I agree with what you're saying in theory - you don't need global state to avoid prop drilling.

@https://www.youtube.com/watch?v=vPRdY87_SH0

-- Encrypted Notes App in React
@https://www.youtube.com/watch?v=z7z0PiiaBgw

MongoDB

-- Scaling horizontaly and verticaly in mongoDB
@https://www.mongodb.com/basics/horizontal-vs-vertical-scaling#:~:text=What%20is%20horizontal%20scaling%3F,scale%20indefinitely%20once%20set%20up.
@https://www.mongodb.com/basics/scaling

Data Structures + Algorithms
@https://www.youtube.com/watch?v=pmN9ExDf3yQ&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H&index=2

# Javascript Foundations (Part 1)

--Function expression vs function declaration
@ https://www.freecodecamp.org/news/when-to-use-a-function-declarations-vs-a-function-expression-70f15152a0a0/#:~:text=In%20short%2C%20use%20function%20declarations,light%2C%20and%20maintain%20clean%20syntax.

Notes: Function expression is defined when you call it but the function declaration gets defined at the past time and they are "saved for later use", and will be executed later.
When an function is invoked we create a new execution context on top of global execution context which contains the:

- this keyword
- arguments
- Variables environment (this environment is for variables which are created inside the function)

For a better performance of javascript engine arguments are not recommended to be used because it looks like an array but its not actually an array. There are many things that you can do with the arguments keyword that might make the compiler or the javascript engine less able to optimise your code.
With the new Javascript, new tools were intreduced that can be used to avoid using the arguments. For example:

- Array.from(arguments)
- Using spread operator (...args)

_-- Lexical means where the function is written --_

--Hoisting
@https://developer.mozilla.org/en-US/docs/Glossary/Hoisting

Notes:
you should try to get rid of hoisting on your code, one way of doing this is by not using "var" but only const and let. You should use var in specific cases and you should have a
strong reason to use it.
Try to answer this question and logic it : https://replit.com/@aneagoie/hoisting-exe#index.js

-- Scope Chain
Notes: Scope chain links and gives us access to variables that are in our parent environment.

Because of lexical scope the javascript compiler looks at the code and attaches all these scope chains before it even runs the code. By doing this the compiler knows what environments are linked to each other and we know what data can be accessed by which function. The scope chain starts where the variable is defined and goes all the way down to the global context to see if the variable exists.

One reason that "eval()" and "with" are not recommended to use it's because of the issues that it has with scope, because the eval()
and with can actually change how scope work internally in javascript. And that makes things difficult for us because we have lexical scope, where the compiler can just look at our code and create the scope chain and understand what's going to happen.

Link : https://www.digitalocean.com/community/tutorials/js-eval

-- Fuction scope vs block scope

    Note: Remember, scope means what variables we have access to.

In ES6 javascript introduced that by using let and const we can have a block scope.

Example:

1. Block scope

```JavaScript

if (5> 4){
    const num = 3;
}

console.log(num);

```

2. function scope

```JavaScript
if (5> 4){
    var num = 3;
}

console.log(num);
```

-------0---------

```JavaScript

function loop() {
    for(var i = 1; i< 5; i++){
        console.log(i);
    }
    console.log("Final", i);
}


loop();

```

This means that by using var into a function we create an function scope which means we should be very careful using it.

-- IIFE (immidietly invoked function expression)

```JavaScript
(function(){
  var a = 1;
})();

console.log(a); //You cannot access a here
```

Libraries like Jquery used to use IIFE a lot.
It enables us to attach private data to a function and it creates a fresh environment for us so that we dont pollute our global execution context.

The goal is to minimize the amount of data that we place in global execution context and IIFE makes it able to scope things into their own environment.

Link: https://www.javascripttutorial.net/javascript-immediately-invoked-function-expression-iife/

-- call() and apply()

    Notes: used to pass methods from one object to another to not brake the rule of dry code. It is very useful to pass functions from one object to another.

Example:

```JavaScript
const wizard = {
 name: 'Merlin',
 health: 50,
 heal(num1, num2) {
   retun this.health += num1 + num2;
 }
}

const archer = {
 name: 'Robin Hood',
 health: 30
}
```

wizard.heal.apply(archer, [100, 30]) //This takes the function from wizard and applys it to archer and increases the health based on the props that we have passed.

apply() as parametes accepts array but call() doesn't accept them.

wizard.heal.call(archer, 100, 30)

call() and apply() call the function immediatly in this case so if you try to log the archer after the command you will see the increase in health but there is also bind() which doesn't call the function directly it just assigns it to it.

Give it a try:

```JavaScript

 wizard.heal.bind(archer, 100, 30);
 console..log(wizard);

```

You will see that the wizard health is not increased because bind() doesn't get called immediately.

```JavaScript

 const healArcher = wizard.heal.bind(archer, 100, 30);
 healArcher();

```

By doing this you can see the result.

To review: call and apply are useful for borrowing methods from an object. While bind is useful for us to call functions later on with a certain context or certain keyword.

Another Example for apply():

```JavaScript

// object definition
const personName = {
  firstName: "Taylor",
  lastName: "Jackson",
};

// function definition
function greet(wish, message) {
  return `${this.firstName}, ${wish}. ${message}`;
}

// calling greet() function by passing two arguments
let result = greet.apply(personName, ["Good morning", "How are you?"]);

console.log(result);

// Output:
// Taylor, Good morning. How are you?

```

Another usecase of bind() is function currying:

Example:

```JavaScript

function multiply(a,b){
    return a*b;
}

let multiplyByTwo =  multiply.bind(this, 2);

console.log(multiplyByTwo(4));

```

Link (learn what function currying is and how does it work) : https://builtin.com/software-engineering-perspectives/currying-javascript

-- Context vs Scope
Notes: Context is most often determined by how a function is invoked with the value of this keyword and scope refers to the visibility of variables.

########################################################################################################################################################################

# Types in Javascript

## Primitive and Non-Primitive types

Primitive types: Non-Primitive:

- number - Object
- boolean - Array
- string - Function
- undefined
- null
- Symbol

Primitive type its a data that only represents a single value.
Think of them like atoms where they can't be broken down into smaller parts.

A non primitive type doesn't contain the actual value directly. It has a reference similar to a pointer to somewhere in memory that the object is held. For example {object.value}

## Pass by reference vs pass by value

Primitive types are passed by value, non-primitive types are passed by reference. We cannot change the value of an primitive type, the only way we can change the value of them is by moving it from memory and create something new.

Lets suppose we have:

```JavaScript

 var a = 5;
 var b = a;

 b++;

 console.log(a); /5
 console.log(b); /6


```

Link (pass by value) : https://www.javascripttutorial.net/javascript-pass-by-value/

Object on the other hand are passed by reference.
This is a good thing about the memory but it has its downside, the downside is by the way we use it. By passing by reference it is very easy to trigger an error and very hard to figure out where the error is coming from.
Lets have some examples so we can see how to avoid these problems.

Examples

```JavaScript

 let obj1 = {a: 'a', b: 'b', c: 'c'};
 let obj2 = obj1;

 obj1.a = 'aa';

 console.log(obj1);
 console.log(obj2);

```

This is an nice example to understand how passing by reference works.
In this case obj1 is assigned in memory and obj2 copies it by reference an in each case that obj1 is going to change obj2 is going to change also. Sometimes we might not expect this and we get into unexpected errors.

Is there any way to get rid of this trouble? Yes, by using Object.assign or spread "(...obj)" operator.

### Object.assign()

```JavaScript

 let obj = {a: 'a', b: 'b', c: 'c'};
 let clone = Object.assign({}, obj);

 obj.c = 5;
 console.log(clone);

```

You will see that if "obj" is going to change "clone" is not going to change its values. This way is also called cloning.
You can learn more about clone and deep cloning in javascript.

### Spread operator

```JavaScript

const food = { beef: '🥩', bacon: '🥓' };

const cloneFood = { ...food };

food.beef = 'Not beef';

console.log(food);
//{ beef: 'Not beef', bacon: '🥓' }

console.log(cloneFood);
// { beef: '🥩', bacon: '🥓' }

```

You can have a look at the link below how cloning works in javascript.

Link: https://www.samanthaming.com/tidbits/70-3-ways-to-clone-objects/

Question: Will the same thing happen if we have object inside an object, for example:

```JavaScript

let obj = {
    a : 'a',
    b : 'b',
    c : {
        deep: 'Clone this'
    }
};

let clone = Object.assign({}, obj);
let clone2 = {...obj};

obj.c.deep = "Lets change this text";

console.log(obj);
console.log(clone);
console.log(clone2);

```

What do you think will happend in this case?
Give it a try and try to analyse the output.

Explanation: Although we cloned the object, the initial object, this is what we call a shallow copy/cloning.
You are going to think "But this doesn't make any sense? We are still copying the entire object...".
What happens is that it clones the first level of the object and it is not able to clone nested objects.

There is another concept for this case which is called deep cloning:

```JavaScript

let obj = {
    a : 'a',
    b : 'b',
    c : {
        deep: 'Clone this'
    }
};

let clone = Object.assign({}, obj);
let clone2 = {...obj};
let superClone = JSON.parse(JSON.stringify(obj));

obj.c.deep = "Lets change this text";

console.log(obj);
console.log(clone);
console.log(clone2);
console.log(superClone);

```

O- Warninggg...

Deep cloning is good but you should be careful because it can lead to some performance implications.
If the main object that we are trying to clone is a large objects which contains nested objects it is going to take a long time to clone everything.

In real life applications you wont see it a lot, if you face a issue where you need to implement this method there's most likely some other ways that you should be doing things.

### Comparing Objects

```JavaScript

var user1 = {name : "foo", org: "bar"};

var user2 = {name : "foo", org: "bar"};

var eq = user1 == user2;

alert(eq); // gives false

```

Notes: This is going to print false because when we have to do with objects we are not comparing the contents of the objects but also the reference.
Two objects are equal if they refer to the exact same object.

How can we compare these two objects?

```JavaScript

var eq = Object.toJSON(user1) == Object.toJSON(user2);
alert(eq); // gives true

JSON.stringify(obj1) === JSON.stringify(obj2)

```

Exercise: What is the output of this code?

```JavaScript

const number = 100
const string = "Jay"
let obj1 = {
  value: "a"
}
let obj2 = {
  value: "b"
}
let obj3 = obj2;

function change(number, string, obj1, obj2) {
    number = number * 10;
    string = "Pete";
    obj1 = obj2;
    obj2.value = "c";
}

change(number, string, obj1, obj2);

//Guess the outputs here before you run the code:
console.log(number);
console.log(string);
console.log(obj1.value);

```

Output:

100
"Jay"
"a"

Explanation :

1.Constants cannot be re-assigned, so number will output 100 and string will output "Jay"

2.Obj1 and obj2 are declared separately in the global scope, and they have two different references and point to different memory locations. Therefore, the value of Obj1 will still be "a".

Since it did not define let obj2 = obj1 in the global name space, they will be referring to different points in memory.

```JavaScript

const number = 100
const string = "Jay"
let obj1 = {
  value: "a"
}
let obj2 = obj1;
let obj3 = obj2;

function change(number, string, obj1, obj2) {
    number = number * 10;
    string = "Pete";
    obj1 = obj2;
    obj2.value = "c";
}

change(number, string, obj1, obj2);

//Guess the outputs here before you run the code:
console.log(number);
console.log(string);
console.log(obj1.value);


```

Output:
100
"jay"
"c"

obj2 is refering to the same point in memory as obj1 and obj1.value is going to be "c".

# Dynamic vs Static Typing

Javascript is dynamic type language which means when we declare an variable we dont have to specify the type of that variable for example:

var a = 100;

Now lets see another example with C++ which is statically typed language:

int a;
a = 100;

You see with statically typed language you have to specify what kind of type the variable is going to be.

How does this happend?
You always have to remember something about this case:
Dynamically-typed languages perform type checking at runtime, while statically typed languages perform type checking at compile time.

**_ Explain this More _** ⚠️
Dynamically-typed languages might not alwayes be ideal and it might cause a problem 😲

Here I have to introduce to you TypeScript: TypeScript allows us to make Javascript to behave like an statically typed language.

Link: https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html

# Strong and Weak typing

Javascript is a dynamic typed language or dynamically typed language that is weakly typed.

In Javascript we can do this:

```JavaScript
var a = "booo";
a+17;

//"booo17"
```

🤯

This is what weakly type language does.
In a strongly typed language you cannot do this.

## Don't declare functions inside a loop

```JavaScript
// Not a good way to go 📛

for(let i=0; i<5; i++) {

    function a() {
        console.log("Yess");
    }
    a();
}

```

The problem here is that inside the for loop you are initializing the a() function 5 times.

```JavaScript
// Good way to go 👍

 function a() {
        console.log("Yess");
    }

for(let i=0; i<5; i++) {
    a();
}

```

## Give default values to function params

Lets suppose we have this function:

```JavaScript

function a(param){
    return param;
}

a()

```

In this case the output is going to be undefined because you are not passing any params when you are actually calling that function.

A lot of developers get into this mistake easily, to get rid of this we can follow this way:

```JavaScript

function a(param = 6){
    return param;
}

a();


```

🔥

## HOF (Higher Order Functions)

In Javascript it is possible to retrun functions from another function and this is very useful when we deal with higher order functions.

For example lets make a function which multiplies two numbers.

```JavaScript
const multiplyBy = function(num1) {
return function(num2){
    return num1*num2;
}
}

const multiplyByTwo = multiplyBy(2);
multiplyByTwo(4);
multiplyByTwo(10);
```

MultiplyBy is an HOF because it is returning another function.

We can write this code in a cleaner way using arrow functions:
Look how much it is going to shorten our code.

```Javascript

 const multiplyBy = (num1) => (num2) => num1*num2;

 multiplyBy(4)(6);

```

High Order Functions are very useful to keep our code dry and to make it more readable.

#########################################################################################################################################################################

Now lets jump to another topic, what makes JavaScript so powerful language?

# Closures and Prototypal Inheritance

## Closures

Clousers are a combination between function() and Lexical Scope.

Clousers cannot be cleaned by garbage collection.

```JavaScript

function callMeMaybe() {
    const callMe = 'Hi! I am now here!';

setTimeout(
    function() {
        console.log(callMe);
    }, 4000
);
}

callMeMaybe();

```

In this case setTimeout function is acting as a closure.

Question:

```JavaScript
//What will be the output in this case?

function callMeMaybe() {

  setTimeout(
    function() {
        console.log(callMe);
    }, 4000
  );

 const callMe = 'Hi! I am now here!';
}

callMeMaybe();

```

Did you expect this output? 😕
Well it doesn't matter where we define the variable in this case.

### Closures and Memory

Closures have to main benefits:

1. Memory efficient
2. Encapsulation

#### Memory efficient

Lets say we have this function:

```JavaScript

//This is an heavy operation ("lets assume 😄"). Maybe this function is accessing an massive array.

function heavyDuty(index) {
    const bigArray = new Array(7000).fill('Smile');
    console.log('created!'); // You will see that this is going to be loged 6 times based on the times we called the function.

    // IMPORTANT !! -> What is the problem with this function? Well everytime that it runs, it creates a new memory location for the "bigArray" and then we return it. And because nothing is referencing it, it gets destroyed.
    return bigArray[index];
}

havyDuty(873);
//What if we want to access this index many times we would repeat ourself:
havyDuty(873);
havyDuty(873);
havyDuty(873);
havyDuty(873);
havyDuty(873);

```

But what is the solution in this case??
-Well it would be great if we could find a way for us to create this "bigArray" and because we know it's going to be used a lot to only create it once and just have it in a memory there so we can just constantly access it and not create a new one everytime the function runs.

Closures come into rescue.

```Javascript

function heavyDuty() {
    const bigArray = new Array(7000).fill('Smile');
    console.log('created!');
    return function(index) {
        return bigArray[index];
    };
}

const getHeavyDuty = heavyDuty();
getHeavyDuty(688);
getHeavyDuty(300);
getHeavyDuty(974);

```

Isn't this cool, by using closures we can crate the memory in location for bigArray only once and we can access it how many time we want and this is one example which makes the closures memory efficient.

#### Encapsulation

Link: https://stackoverflow.com/questions/34218876/what-is-the-difference-between-encapsulation-and-closure#:~:text=A%20closure%20is%20an%20example,%22slots%22%20in%20an%20object.

Exercises with Closures:

Exercise 1:

```JavaScript

// Bad Way 👎

let view;
function initialize() {
    view = 'Image of View';
    console.log('View has been sent!');
}

initialize();
initialize();
initialize();
console.log(view);

```

```JavaScript

// Good Way 👎

let view;
function initialize() {
    let called = 0;
return function() {
    if(called > 0) {
        return;
    } else {
        view="This view";
        called++;
        console.log("View has been sent!");
    }
}
}
const sendView = initialize();
sendView();
console.log(view);

```

Exercise 2:

```JavaScript

const array = [1,2,3,4];
for(var i=0; i < array.length; i++ ){
    setTimeout(function(){
        console.log("I am at index" + i);
    }, 3000)
}

//Is the output what you expected? Can you make it so it shows 0, 1, 2 ,3?

```

One way is by replacing var with let.

How can we solve it with closures? Hmmm...

```JavaScript

const array = [1,2,3,4];
for(var i=0; i < array.length; i++ ){
    (function(closureI) {
    setTimeout(function(){
        console.log("I am at index" + i);
    }, 3000)
    })(i)
}


```

Practice Exercises:

```JavaScript

//Exercise 1

function test() {
   console.log(a);
   console.log(foo());

   var a = 1;
   function foo() {
      return 2;
   }
}

test();

//Exercise 2

var a = 1;

function someFunction(number) {
  function otherFunction(input) {
    return a;
  }

  a = 5;

  return otherFunction;
}

var firstResult = someFunction(9);
var result = firstResult(2);


```

## Prototypal Inheritance

Prototypal inheritance in javascript is the linking of prototypes of a parent object to a child object to share and utilize the properties of a parent class using a child class. Prototypes are hidden objects that are used to share the properties and methods of a parent class to child class.

Lets have a look at this example so we can see how we can pass properties from an parent objects to the child.

Example:

```JavaScript

 let dragon = {
  name:'Eroptus',
  fire: true,
  fight() {
    return 5
  },
  sing() {
    if (this.fire) {
      return  `I am ${this.name}, the breather of fire `
    }
  }
 }

 let lizard = {
  name: 'Kiki',
  fight() {
    return 1
  }
 }

lizard.__proto__ = dragon;

for(let prop in lizard){
  console.log(prop)
}

//You will see that the methods of dragon object are passed to the lizard object and this is able by using prototypal inheritance.

⚠️
//Importantt!!! Remember, the properties are not part of lizard , what javascript does is going up the prototype chain and useing the methods of Dragon. We can prove this very easily using "hasOwnProperty()" method:

for(let prop in lizard){
  if(lizard.hasOwnProperty(prop)) {
    console.log(prop)
  }
}

```

But remember what I have showed in this example try to avoid it in you're code base. I am just creating this example to make it understand how prototypal inheritance works but it is bad for performance and there's different ways when we want to inherit when it comes to prototypal inheritance.

Basically we never want to manually assign the prototype chain and create that chain ourselves.

But why is prototypal inheritance important????
-> The fact that objects can share prototypes means that you can have objects with properties that are pointing to the same location in memory and being more efficient.

A saffer way to do it:

```JavaScript

let human = {
  mortal: true
}

let socrates = Object.create(human);
socrates.age = 45;
console.log(socrates);

```

# Functional Programming

## Seperation of concerns is an important topic in all languages and what that means is seperating our code into chunks so that everything is well organized. Functional programming comes into help in this case.

5 benefits of functional programming:

🏆 Clear + Understandable
🏆 Easy to Extend
🏆 Easy to Maintain
🏆 Memory Efficient
🏆 DRY (this principle doesn't exist when we drink beers 🍺)

But remember functional programming has a lot of restraints, a lot of rules and things that you can't do. And this at first might sound wrong or wierd but we have to make sure that we have code that doesn't get out of hand.
One of these rules is called _Pure Functions _

## Pure Functions

What are pure functions❔

- A function has to always return the same output, given the same input and the function cannot modify anything outside of itself.
- No side effects.

Example:

```Javascript
// no side effects
// input gives the same output

const array = [1,2,3];
function mutateArray(arr) {
 arr.pop()
}
mutateArray(array);
console.log(array);

// This function has an side effect because it modifies something outside of itself. This way can cause a lot of bugs because we might be using the "array" in different places or functions and we get an unexpected result.

//It might sound wierd now but have a lot at the example below.

```

But how can we write an function which has no side effects.

```JavaScript

const array = [1,2,3];

function removeLastItem(arr){
 const newArray = [].concat(arr);
 newArray.pop()
 return newArray
}

function multiplyBy2(arr){
 return arr.map(item => item*2)
}

const array2 = removeLastItem(array);
const array3 = multiplyBy2(array);

console.log(array, aaray2, array3);
```

### In Pure Functions Input Gives the Same Output

In other terms this is called referential transparency.

## Imperative vs Declerative

Imperative code is code that tells the machine what to do and how to do it.
Declerative code tells it what to do and what should happen.

Remember: A computer is better at being `imperative` which means it needs to know how to do things.
Humans in the other hand are more `declerative`.

Functional programming helps us be more _declerative_. (Example of ReactJs)

## Immutability

## Currying

Currying takes a function that receives more than one parameter and breaks it into a series of unary(one parameter) functions.

Example:

```JavaScript

const buildCar = (wheels) => {
  return (doors) => {
    return (engine) => {
      return `${wheels},${doors},${engine}`
    }
  }
}

const myCar = buildCar("Michelin")("Maybach")("V8 biturbo");

console.log(myCar);

```

This function works but there is a problem with it 😲, it gets ugly and nested the further we go.

Lets refactor it:

```JavaScript

const buildCar = wheels => doors => engine => `${wheels},${doors},${engine}`;

const myCar = buildCar("Michelin")("Maybach")("V8 biturbo");

console.log(myCar);

```

Function Composition with curried functions:

But what is function composition at first?

- Function composition is an approach where the result of one function is passed on to the next function, which is passed to another until the final function is executed for the final result. Function compositions can be composed of any number of functions.

Example:

```JavaScript

const addCustomer = fn => (...args) => {
  console.log('saving customer info ...');
  return fn(...args);
}

const processOrder = fn => (...args) => {
  console.log(`processing order #${[...args].toString()} completed.`)
  return fn(...args);
}

let completeOrder = (...args) => {
  console.log(`Order #${[...args].toString()} completed.`)
}

completeOrder = (processOrder(completeOrder));
completeOrder = (addCustomer(completeOrder));
completeOrder("1000");

```

## Function Composition and Pipe Functions

Function Composition is used a lot in pure functions (functional programming)

```JavaScript

const add2 = (x) => x+2;
const subtract1 = (x) => x-1;
const multiplyBy5 = (x) => x*5;

//Notice how the functions execute from inside to outside and right to left.

const result = multiplyBy5(subtract(add2(4)));

console.log(result);
```

But the above function is not an composed function I was just giving an introduction how the composed function should be running so you have it more easy to understand.

But be careful before you start learning about these examples you should know what higher order functions and currying are.

```JavaScript
// This is how the upper function would look like when we use composed function.

const compose = (...this) => val => fns.reduceRight((prev, fn) => fn(prev), val);

const compResult = compose(multiplyBy5, subtract1, add)(4);

console.log(compResult);

//This will show teh same output. Great Job!!!

```

In the other hand are piped functions and the only difference is that it uses reduce not reduceRight. So by using reduce it reads from left to right.

Example:

```JavaScript

const pipe = (...fns) => (val) => fns.reduce((prev, fn) => fn(prev), val);

const pipeResult = pipe(add2, subtract1, multiplyBy5)(5);

console.log(pipeResult);

```

Word Counter example with piped functions.

```JavaScript

const ipsum = "On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish.";

const pipe = (...fns) => (val) => fns.reduce((prev, fn) => fn(prev), val);

const splitWords = (text) => string.split(' ');
const count = (array) => array.length;

const wordCount = pipe(
  splitWords,
  count
);

console.log(wordCount(ipsum));


// The pipe function is also reusable

const anotherText = "Count how many words are in this text."

console.log(wordCount(anotherText));

```

Check for palindrome example using pipe function:

```JavaScript

const pal1 = "taco cat";
const pal2 = "UFO tofu";
const pal3 = "Dave";

const split = (string) => string.split('');
const join = (string) => string.join('');
const lower = (string) => string.toLowerCase();

const fwd = pipe(
  splitOnSpace,
  join,
  lower
);

const rev = pipe(
  fwd,
  split,
  reverse,
  join
);

console.log(fwd(pal1) === rev(pal1));
console.log(fwd(pal2) === rev(pal2));
console.log(fwd(pal3) === rev(pal3));

```

- Link to learn more about pipe and composed functions: https://www.youtube.com/watch?v=kclGXphtmVg

Lets have another example with function composition:

Lets create a function which takes an negative number, multiplies it by three and converts it to positive numbers. So we will try to use two functions into one.

```JavaScript

const compose = (f,g) => (data) => f(g(data));

const multiplyBy3 = (num) => num*3;
const makePositive = (num) => Math.abs(num);

const multiplyBy3AndAbsolute = compose(multiplyBy3, makePositive);

multiplyBy3AndAbsolute(-50);

//Think of function composition just like moving little product around an assembly line. You have multiple functions which you can run together to have the final output by having pure functions and seperation of concerns.
```

# Asynchronous JavaScript

What asynchronous means:

- Asynchronous basically means that we dont have the data right now.

For example:

Lets say you are building an React web page and when the page loads you also have to make a request to database or to a third party API to retreive the data.- All of these require asynchronous code because it's information we don't have yet.

Assume we have this code and we want to find the output:

```JavaScript

setTimeout(() => {console.log("1, First one")}, 0);
setTimeout(() => {console.log("2, Second one")}, 0);


Promise.resolve('hi').then((data) => console.log("3", data));

console.log("3, Third One");


```

To understand the output of tis code better you should learn a bit about call stack and memory heap. Remember JavaScript is designed to be a single threaded programming language, there are other languages which are multi threaded in which they have multiple call stacks unlike JavaScript which has only one.

But isn't more better than one? Running cod eon a single thread can be quite easy since you dont have to deal with complicated scenarios that arise from multithreaded environments like `deadlocks`.

`Deadlock` basically occurs when two threads each lock a different variable at the same time and then try to lock the variable that the other thread already locked. As a result, each thread stops executing and waits for the other thread to release the variable.

But 🤔 there is a big problem with what I explained. Having single threaded language might face us with a loot of issues. Lets suppose we have a big function which goes through a million items inside an array and modifies them. This will slow down our application a lot because the other functions should wait for this function to finish. But "Javascript is a single threaded language that can be non-blocking" and asynchronous commes into our rescue.

This doesn't mean that synchronous in bad, it is very readable but it gets slower and by combining it with async we can kick ass. 🤟

`setTimeout()` is asynchronous.
Have a look at this.

```JavaScript

console.log("1");
setTimeout(() => {
  console.log("2");
}, 2000);
console.log("3");

```

Yess it is possible.

⚠️ Remember `setTimeout()` is not part of JavaScript engine it is part of WebAPI.

## Async/Await

An async function is a function that returns a promise and it is very easy to read.

```JavaScript

async function playerStart() {
  const firstMove = await movePlayer(100,"Left");
  await movePlayer(400,"Left");
  await movePlayer(10,"Right");
  await movePlayer(330,"Left");
}

```

- Lets have a look how we can fetch data with async/await.

```JavaScript

async function fetchData() {

  const resp = await fetch('....url');
  const data = await resp.json();
  console.log(data);

}

```

- Fetching an array of json.

```JavaScript

const urls = [
  //array with urls.
];


const getData = async function(){

  //also we are going to catch errors with async/await.
  try {
     const [users, posts, albums] = await Promise.all(urls.map(url =>
     const response = await fetch(url);return response.json();
     ));

     console.log(users);
     console.log(posts);
     console.log(albums);
  }
  catch(err) {
    console.log("Error!!" , err);
  }

};

getData();

```

### for await of

```JavaScript

const urls = [
//Array of urls
];

const loopThroughUrls = url => {
  for(url of urls) {
    console.log(url);
  }
}

loopThroughUrls(urls);

```

Knowing about this concept now we can do this top fetch data from multiple api.

```JavaScript
const urls = [
  //urls to fetch
];

const getData2 = async function() {
  const arrayOfPromises = urls.map(url => fetch(url));
  for await (let request of arrayOfPromises) {
    const data = wait request.json();
    console.log(data);
  }
}

getData2(urls);

```

### Promises

There are three type of promises :

- Parallel
- Sequence
- Racing

### Threads, Cuncurrency and Paralelism

# Working with Objects

## Object rest properties

- In JavaScript the rest parameter is denoted by three dots (`...`) preceding a parameter name in a function definition. It allows you to represent an indefinite number of arguments as an array.

```JavaScript

//Example 1

let { fname, lname, ...rest } = { fname: "Hemanth", lname: "HM", location: "Earth", type: "Human" };
fname; //"Hemanth"
lname; //"HM"
rest; // {location: "Earth", type: "Human"}


//Example 2
//In this example , the `sum` function takes an indefinite number of arguments, which are represented by the ...numbers parameter. Inside the function, the numbers parameter is treated as an array, so we can use methods like reduce() to compute the sum of all the numbers.

function sum(...numbers) {
  return numbers.reduce((total, number) => total + number);
}

console.log(sum(1, 2, 3)); // 6
console.log(sum(4, 5, 6, 7)); // 22


//Example 3
//The rest operator can be used with destructuring to extract a subset of properties from an object or an array.
const person = { name: 'John', age: 30, city: 'New York', country: 'USA' };

const { name, ...address } = person;

console.log(name); // 'John'
console.log(address); // { age: 30, city: 'New York', country: 'USA' }


//Example 4
//The rest operator can also be used with default parameter values to specify a default value for the rest parameter.
function concat(separator = ',', ...strings) {
  return strings.join(separator);
}

console.log(concat(';', 'foo', 'bar', 'baz')); // 'foo;bar;baz'
console.log(concat()); // ''


```

- A good question might arise from you when we talk about rest operator. How can we destructure nested objects with the rest operator ❓❔
  This is a great question and very useful when you build an application.

Have a look at these examples:

```JavaScript

//Example 1
//In this example, we use destructuring to extract the name property of the person object, and the city property of the nested address object, and the rest of the properties of the nested address object into a new object called restAddress.

const person = { name: 'John', age: 30, address: { city: 'New York', country: 'USA', postalCode: '10001' } };

const { name, ...{ address: { city, ...restAddress } } } = person;

console.log(name); // 'John'
console.log(city); // 'New York'
console.log(restAddress); // { country: 'USA', postalCode: '10001' }

//Example 2

const user = {
  id: 123,
  name: 'John Doe',
  contact: {
    email: 'johndoe@example.com',
    phone: '123-456-7890',
    address: {
      street: '123 Main St',
      city: 'Anytown',
      state: 'CA',
      zip: '12345'
    }
  }
};

// using destructuring with rest operator
const { contact: { email, ...restContact } } = user;

console.log(email); // 'johndoe@example.com'
console.log(restContact); // { phone: '123-456-7890', address: { street: '123 Main St', city: 'Anytown', state: 'CA', zip: '12345' } }


//Example 3

const employee = {
  id: 456,
  name: 'Jane Smith',
  department: {
    name: 'Engineering',
    supervisor: {
      name: 'John Doe',
      title: 'Engineering Manager'
    },
    employees: [
      {
        id: 123,
        name: 'Alice Johnson',
        title: 'Software Engineer'
      },
      {
        id: 789,
        name: 'Bob Lee',
        title: 'Software Engineer'
      }
    ]
  }
};

// using destructuring with rest operator

const employee = {
  id: 456,
  name: 'Jane Smith',
  department: {
    name: 'Engineering',
    supervisor: {
      name: 'John Doe',
      title: 'Engineering Manager'
    },
    employees: [
      {
        id: 123,
        name: 'Alice Johnson',
        title: 'Software Engineer'
      },
      {
        id: 789,
        name: 'Bob Lee',
        title: 'Software Engineer'
      }
    ]
  }
};

const {
  name: employeeName,
  department: {
    supervisor: { name: supervisorName, ...restSupervisor },
    employees: [{ name: employee1Name }, { name: employee2Name }, ...restEmployees]
  }
} = employee;

console.log(employeeName); // 'Jane Smith'
console.log(supervisorName); // 'John Doe'
console.log(restSupervisor); // { title: 'Engineering Manager' }
console.log(employee1Name); // 'Alice Johnson'
console.log(employee2Name); // 'Bob Lee'
console.log(restEmployees); // []


```

But why do I need to use the rest operator to destructure the objects in my application , I can just use optional chaining operator and I get the value that I want ????

There is a big reason about that:

- You may not always need to use destructuring with the optional chaining operator, but sometimes it can make your code more concise and readable.

- While the optional chaining operator can help you safely access nested properties without causing errors, it can also result in long and repetitive code, especially when you need to access multiple nested properties.

- On the other hand, destructuring can help you extract specific properties from an object in a more concise and readable way. This can make your code easier to understand and modify, especially when working with complex objects.

- For example, suppose you have a complex object with nested objects, and you want to extract some properties from the nested object while keeping the remaining properties intact. Here's an example:

```JavaScript

const user = {
  id: 123,
  name: 'John Doe',
  contact: {
    email: 'johndoe@example.com',
    phone: '123-456-7890',
    address: {
      street: '123 Main St',
      city: 'Anytown',
      state: 'CA',
      zip: '12345'
    }
  }
};

// extract email and phone from contact, and keep the rest of the address
const { contact: { email, phone, address: { street, city, state, ...restAddress } } } = user;

console.log(email); // 'johndoe@example.com'
console.log(phone); // '123-456-7890'
console.log(street); // '123 Main St'
console.log(city); // 'Anytown'
console.log(state); // 'CA'
console.log(restAddress); // { zip: '12345' }

```

### Spread Operator

- Allows an iterable such as an array or a string to be expanded in places where zero or more arguments or elements are expected.

It can be used for 5 reasons:

1.  Spread an array into separate elements:

    ```JavaScript
    const nums = [1, 2, 3];
    console.log(...nums); // 1 2 3
    ```

2.  Combine multiple arrays into one array:

    ```JavaScript
     const arr1 = [1, 2];
     const arr2 = [3, 4];
     const arr3 = [5, 6];
     const combined = [...arr1, ...arr2, ...arr3];
     console.log(combined); // [1, 2, 3, 4, 5, 6]
    ```

3.  Copy an array:

    ```JavaScript
    const original = [1, 2, 3];
    const copy = [...original];
    console.log(copy); // [1, 2, 3]
    ```

4.  Convert an iterable into an array:

    ```JavaScript
     const str = 'hello';
     const arr = [...str];
     console.log(arr); // ['h', 'e', 'l', 'l', 'o']
    ```

5.  Pass arguments to a function as an array:
    ```JavaScript
    function sum(a, b, c) {
      return a + b + c;
    }
    const nums = [1, 2, 3];
    console.log(sum(...nums)); // 6
    ```

⚠️❗ The spread operator can also be used with objects, but it is important to note that it creates a shallow copy of the object rather than a deep copy. This means that nested objects and arrays will still be references to the original objects and arrays, not new copies. ⚠️❗

To deep clone an object, you can use a combination of the spread operator and recursion or a third-party library like Lodash.
Here's an example of using recursion to deep clone an object:

```JavaScript

function deepClone(obj) {
  if (typeof obj !== 'object' || obj === null) {
    return obj;
  }

  const clone = Array.isArray(obj) ? [] : {};

  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      clone[key] = deepClone(obj[key]);
    }
  }

  return clone;
}

const original = {
  name: 'John',
  age: 30,
  address: {
    city: 'New York',
    state: 'NY'
  },
  hobbies: ['reading', 'traveling']
};

const cloned = deepClone(original);

console.log(cloned); // { name: 'John', age: 30, address: { city: 'New York', state: 'NY' }, hobbies: [ 'reading', 'traveling' ] }
console.log(cloned === original); // false
console.log(cloned.address === original.address); // false
console.log(cloned.hobbies === original.hobbies); // false


```

⚠️⚠️⚠️
If you are considering how expensive your application is becoming you have to keep in mind that deep cloning an object can be computationally expensive, so it should be used when necessary.

Deep cloning an object is expensive in terms of memory and performance because it requires creating new copies of all the nested objects and arrays. This means that for a large and complex object, deep cloning can be a time-consuming and memory-intensive process.

There are three ways to do deep cloning an object in a memory-efficient way:

1. Use a third-party library like `Lodash`.

2. Use Object pooling, `Object pooling` is a technique where you reuse objects instead of creating new ones. Instead of creating a new object every time you need to deep clone an object, you can use an object pool to recycle previously created objects.

3. Use a custom cloning function: If you need more control over the cloning process, you can write your own custom cloning function. You can use techniques such as memoization and recursion to optimize the cloning process and reduce memory usage.

Here is an example how you can use object pooling to deep clone an object in a memory-efficient way while also avoiding unnecessary cloning of primitive values:

```JavaScript
// Create an object pool for reusing cloned objects
const objectPool = new Map();

function deepClone(object) {
  // Check if the object is already in the pool
  if (objectPool.has(object)) {
    // If it is, return the cloned object from the pool
    return objectPool.get(object);
  }

  let clonedObject;

  // Check the type of the object
  if (Array.isArray(object)) {
    // If it's an array, clone each item recursively
    clonedObject = [];
    for (let i = 0; i < object.length; i++) {
      clonedObject.push(deepClone(object[i]));
    }
  } else if (typeof object === 'object' && object !== null) {
    // If it's an object, clone each property recursively
    clonedObject = {};
    Object.keys(object).forEach(key => {
      // Check if the property is a primitive value
      if (typeof object[key] !== 'object' || object[key] === null) {
        // If it is, simply copy the value instead of cloning it
        clonedObject[key] = object[key];
      } else {
        // If it's an object or array, clone it recursively
        clonedObject[key] = deepClone(object[key]);
      }
    });
  } else {
    // If it's a primitive value, simply copy it
    clonedObject = object;
  }

  // Add the cloned object to the pool for reuse
  objectPool.set(object, clonedObject);

  return clonedObject;
}

//When we want to deep clone an object, we first check if the object is already in the pool. If it is, we simply return the cloned object from the pool instead of creating a new one. This helps reduce memory usage by reusing previously created objects.

```

# 🥇 Memory - efficient and cost - effective code 🥇

- If you are considering how much memory and cost effective is your code I would really suggest you to have a look and learn about `Algorithm efficiency`.

Examples:

```JavaScript

//Example 1
// Lets say you want to find the sum of an array.

function sum(arr) {
  let total = 0;
  for (let i = 0; i < arr.length; i++) {
    total += arr[i];
  }
  return total;
}

// This code has a time complexity of O(n), where n is the length of the array. For very large arrays, this algorithm can become very slow. A more efficient alternative is to use a divide-and-conquer algorithm like the recursive sum algorithm, which has a time complexity of O(log n) and can calculate the sum of large arrays much more quickly:

function recursiveSum(arr, start, end) {
  if (start === end) {
    return arr[start];
  }
  let mid = Math.floor((start + end) / 2);
  return recursiveSum(arr, start, mid) + recursiveSum(arr, mid + 1, end);
}

function sum(arr) {
  return recursiveSum(arr, 0, arr.length - 1);
}


//Example 2
// Finding the maximum value in an array: When finding the maximum value in an array, using an efficient algorithm can significantly improve performance. For example, consider the following code snippet that finds the maximum value in an array using a linear search:

function linearMax(arr) {
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i];
    }
  }
  return max;
}

//This code has a time complexity of O(n), where n is the length of the array. If the array is very large, this algorithm can become very slow. A more efficient alternative is to use a divide-and-conquer algorithm like the recursive maximum value algorithm, which has a time complexity of O(log n) and can find the maximum value of large arrays much more quickly:

function recursiveMax(arr, start, end) {
  if (start === end) {
    return arr[start];
  }
  let mid = Math.floor((start + end) / 2);
  let leftMax = recursiveMax(arr, start, mid);
  let rightMax = recursiveMax(arr, mid + 1, end);
  return Math.max(leftMax, rightMax);
}

function max(arr) {
  return recursiveMax(arr, 0, arr.length - 1);
}


//Example 3

//Filtering an array: When filtering an array, using an efficient algorithm can significantly improve performance. For example, consider the following code snippet that filters an array using a linear search:

function linearFilter(arr, fn) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    if (fn(arr[i])) {
      result.push(arr[i]);
    }
  }
  return result;
}


//This code has a time complexity of O(n), where n is the length of the array. If the array is very large, this algorithm can become very slow. A more efficient alternative is to use a divide-and-conquer algorithm like the recursive filter algorithm, which has a time complexity of O(log n) and can filter large arrays much more quickly:


function recursiveFilter(arr, fn, start, end) {
  if (start === end) {
    if (fn(arr[start])) {
      return [arr[start]];
    } else {
      return [];
    }
  }
  let mid = Math.floor((start + end) / 2);
  let left = recursiveFilter(arr, fn, start, mid);
  let right = recursiveFilter(arr, fn, mid + 1, end);
  return left.concat(right);
}

function filter(arr, fn) {
  return recursiveFilter(arr, fn, 0, arr.length - 1);
}

```

- There are a loot of things to take into considoration when you want to write better code for example:

1.  Best practices for minimizing memory usage - One of the most important aspects of writing efficient JavaScript code is minimizing memory usage. In order to do this, it's important to understand how JavaScript manages memory. JavaScript uses a garbage collector to automatically free up memory that is no longer being used. However, if there are objects or variables that are still being referenced, they will remain in memory even if they are no longer needed.
    Some best practices for minimizing memory usage include using object pooling, which involves reusing objects instead of creating new ones, avoiding circular references, which can cause memory leaks, and being careful with closures, which can create unnecessary references.

2.  Network performance optimization

    - In modern web development, network performance is a critical factor in the user experience. There are several strategies for optimizing network performance in JavaScript applications, including using lazy loading, which involves loading resources only when they are needed, caching, which involves storing frequently used resources locally to reduce network requests, and reducing the size of network requests by using compression, minification, or other techniques.

3.  Minimizing code execution time

    - In addition to minimizing memory usage, it's also important to minimize the time it takes for JavaScript code to execute. Some techniques for doing this include using memoization, which involves caching the results of expensive computations so they don't need to be recomputed, avoiding unnecessary DOM manipulation, which can be slow, and reducing the use of loops, which can be inefficient for large datasets.

4.  Profiling and benchmarking

    - Profiling and benchmarking are techniques for identifying performance bottlenecks in JavaScript code. Profiling involves using tools to analyze the code and identify where time and resources are being spent. Benchmarking involves measuring the performance of different versions of the code to determine which is faster. Once performance bottlenecks are identified, developers can optimize their code to improve performance.

5.  Measuring performance
    - Measuring and monitoring the performance of JavaScript applications is important for identifying and addressing performance issues. Tools like Chrome DevTools and Lighthouse can be used to measure performance metrics like page load time, time to interactive, and first contentful paint. Developers can use these metrics to identify areas of the application that are slow and optimize them for better performance.

# Data Structures in JavaScript

## Arrays

There are 2 types of arrays Static and Dynamic

### Static

One limitation of static array is that they're fixed in size which means you have to specify the number of elements your array with hold

- Lookup : O(1)
- Push : O(1)
- Insert : O(n)
- Delete : O(n)

### Dynamic

A dynamic array allows us to copy and rebuild an array at a new location.

- Lookup : O(1)
- Append\* : O(1)
- Insert : O(n)
- Delete : O(n)

* can be O(n).

## Stacks

- Lookup : O(1)
- Push : O(1)
- Insert : O(n)
- Delete : O(n)

## Queues

- Lookup : O(1)
- Push : O(1)
- Insert : O(n)
- Delete : O(n)

## Linked Lists

- Lookup : O(1)
- Push : O(1)
- Insert : O(n)
- Delete : O(n)

## Trees

## Tries

## Graphs

## Hash Tables
