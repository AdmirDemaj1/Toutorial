https://github.com/academind/react-complete-guide-course-resources/tree/main/code

Google dashboard

creatormode2208

# 1 Day

Vanilla JS vs Reactjs

Vanilla: https://codesandbox.io/s/vanilla-js-demo-6049kj
React: https://codesandbox.io/s/react-vs-vanilla-demo-uc08fv

Exercise: https://codesandbox.io/s/first-react-app-start-7ec9fd

- Based on the provided code add another code for Vanilla Js and handle it when it is clicked.

# Virtual DOM

React components are displayed performantly using a virtual DOM (Document Object Model).
You may be familiar with the real DOM – it provides the structure for a web page. However, changes
to the real DOM can be costly, leading to performance problems in an interactive app. React solves
this performance problem by using an in-memory representation of the real DOM called a virtual
DOM. Before React changes the real DOM, it produces a new virtual DOM and compares it against
the current virtual DOM to calculate the minimum amount of changes required to the real DOM.
The real DOM is then updated with those minimum changes.

# Understanding JSX

```JavaScript
function App() {
return (
<div className="App">
<Alert type="information" heading="Success">
Everything is really good!
</Alert>
</div>
);
}
```

You can see that JSX looks a bit like HTML. However, it isn’t HTML because an HTML div element
doesn’t contain a className attribute, and there is no such element name as Alert. The JSX is also
embedded directly within a JavaScript function, which is a little strange because a script element
is normally used to place JavaScript inside HTML.

JSX is a JavaScript syntax extension. This means that it doesn’t execute directly in the browser – it
needs to be transpiled to JavaScript first. A popular tool that can transpile JSX is called Babel.

# Introduce to React Js

     1- Creating a componnet
     2- How to import and export a component
     3- Props
     4- States
     5- Using Events

# React - Router

Explain what React Router is and why it is used?
Show how routes are created with path and element.
Show what is the diff between <link> and <Link> from react-router-dom.
Create a header to navigate to these pages.
Explain how to make nested routes.
Show how to make Layouts and Outlet.
Show errorMessages with errorsElement.
Explain NavLinks.
programmatic Imperative navigation from a function using navigate from useNavigate().
Dynamic Routes.
Show how to get the id from routes using params from useParams().

Relative and Absolute paths.

->>> // Challenge / Exercise

// 1. Add five new (dummy) page components (content can be simple <h1> elements)
// - HomePage
// - EventsPage
// - EventDetailPage
// - NewEventPage
// - EditEventPage
// 2. Add routing & route definitions for these five pages
// - / => HomePage
// - /events => EventsPage
// - /events/<some-id> => EventDetailPage
// - /events/new => NewEventPage
// - /events/<some-id>/edit => EditEventPage
// 3. Add a root layout that adds the <MainNavigation> component above all page components
// 4. Add properly working links to the MainNavigation
// 5. Ensure that the links in MainNavigation receive an "active" class when active
// 6. Output a list of dummy events to the EventsPage
// Every list item should include a link to the respective EventDetailPage
// 7. Output the ID of the selected event on the EventDetailPage
// BONUS: Add another (nested) layout route that adds the <EventNavigation> component above all /events... page components

Show Data Fetching with Loader.

- Show how can you fetch data inside the object where you declare the routes and how to access these data into the component.

- Show how to use loader into the component.

Show how we could use naviagetion.state === 'Loading' to boost the user experience.

Show how to handle errors inside the loaders.

Show how to use a shared laoder and useRouteLoaderData() Hook

Show how can you use action() to submit a form .

Updating the UI state based on the submission status.

⚠️ Remember these are all provided prom react-router make that clear.

Validating User Input and outputting it.

# Adding Authentication To React Apps

Server Side Sessions vs Authentication Tokens

Query Parameters. localhost::3000/auth?mode=signup || localhost::3000/auth?mode=login

Example with authentication and authorization without using a database : https://codesandbox.io/s/hopeful-galois-k77m77?file=/src/routes/RoutePath.js:873-886

https://www.makeuseof.com/manage-user-session-data-react-using-cookies-session-storage/

Protecting cookies when crateing user sessions into cookies: https://blog.codinghorror.com/protecting-your-cookies-httponly/

# Data Fetching and HTTP Requests

Links:

React Suspense: https://blog.logrocket.com/data-fetching-react-suspense/

Reac Documentation: using Suspense to fetch data and using useDeferredValue() https://react.dev/reference/react/Suspense

Why do we need a backend and why we don't communicate directly with our database from our React application?

How to fetch data from our endpoints.

Show a wrong way to fetch data which results into infinit loop and ask why did it happend.

Show how we can use useEffect to fetch data.

Explain fetch().then() also async await to fetch data.

Handle Loading States and Errors.

use try and catch when fetch data because if we throw Error() it is going to crash our application.

Sending data with POST request.

# Working wih Forms

Forms Examples:
https://ibaslogic.com/simple-guide-to-react-form/
https://www.freecodecamp.org/news/how-to-build-forms-in-react/

1. Controlled vs UnControlled Components
2. Working with forms and what is tricky about them
3. Handling Form Submission (handling form with state, refs, browser features and ReactHookForm )
4. Form Validation (Working with react hook form and ajv validation) -> Vlidation on every keystoke, on lost focus and on form submission
5. Browser Built-in Features
6. Custom Solutions to deal with User Inputs and Validation
7. Validation -> User Interaction or making it work, pros and cons

Building multi steps form part 1 : https://claritydev.net/blog/build-a-multistep-form-with-react-hook-form
Building multi steps form part 2 (Advanced): https://claritydev.net/blog/advanced-multistep-forms-with-react

# Window built-in properties

Link mdn: https://developer.mozilla.org/en-US/docs/Web/API/Window

# Local Storage

What it is and how to use it: https://ibaslogic.com/persisting-react-state-in-local-storage/

Pros and Cons:
https://blog.stackademic.com/exploring-local-storage-%EF%B8%8F-session-storage-and-caching-in-react-b1bc6cb39a61

Security risks: https://dev.to/rdegges/please-stop-using-local-storage-1i04

# Web Workers
