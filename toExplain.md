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

async function fetchData() {
  const response1 = await fetch('https://api.example.com/data1');
  const data1 = await response1.json();

  const response2 = await fetch('https://api.example.com/data2');
  const data2 = await response2.json();

  return [data1, data2];
}

async function fetchDataAndDisplay() {
  try {
    const [data1, data2] = await fetchData();
    console.log('Data 1:', data1);
    console.log('Data 2:', data2);
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

fetchDataAndDisplay();



```

What can go wrong if we dont use it:
