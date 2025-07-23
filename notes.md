## Notes

- uvicorn main:app --reload to run
- Also fastapi dev example_main.py can run and show interactive docs for post and get stuff

# Errors

1. 400 errors (bad requests) indicates client (web browser) sent an invalid request
2. 500 errors are internal errors, where server encountered an issue while trying to fufill client rquest, so server fault

# Server

1. Origin site can be used at reference for relative url fetch("/save"); and be fine

# HTTP

1. Content-Type: "application/json" is part of protocal not JavaScript or FastAPI
2. So HTTP Javascript and server all interact.
3. application/json teslls the server body of this requests is JSON, not other stuff like XML or plain text
4. Without specifiecd header, FastAPI/backend could ignore body, misinterpret
or throw validation error!!!

## What AI said that was helpful

- FastAPI is running at that location and has a POST /save route. So FastAPI receives it, checks the method (POST), checks the header (Content-Type), and reads the JSON body accordingly.

## Javascript

1. async (e) => {...} handles that event
2. e.preventDefault(); prevents reload page which is default response
3. getElementByID("ticker").value; grabs that element
4. parseFloat() converts string to decimal or number
5. Event listener sets up function that will be called whenever specified event is delivered to target
6. All JS does is sends HTTP request

# Ideas

1. Vanilla js here runs inside browser page
2. Uses DOM API, how JS talks to page structure.
3. getElementById() grabs specific element, but .value gets the value inside input field


## Big Ideas

- fetch() buit in function that lets JavaScript make HTTP requests eg. GET a webpage or API data, POST a form, etc. By default fetch() is a GET request
- await pauses function until Promise is finised
