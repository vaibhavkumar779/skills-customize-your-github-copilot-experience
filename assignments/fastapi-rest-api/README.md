# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a simple REST API using FastAPI to learn how to define routes, handle requests, and return JSON responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description

Define routes for a FastAPI application that return data for different resource paths.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `main.py`
- Define at least two routes using `@app.get()`
- Return JSON responses for each endpoint
- Example: `GET /items` returns a list of items

### 🛠️ Handle Path and Query Parameters

#### Description

Add route handlers that accept path and query parameters to customize API behavior.

#### Requirements
Completed program should:

- Define a route with a path parameter, such as `/items/{item_id}`
- Accept an optional query parameter, such as `q`
- Return a JSON response that includes the path and query values
- Example: `GET /items/5?q=search` returns `{ "item_id": 5, "q": "search" }`

### 🛠️ Use Pydantic Models for Request Data

#### Description

Create a Pydantic model to validate request payloads and accept JSON data in a POST request.

#### Requirements
Completed program should:

- Define a Pydantic model for a request body, such as `Item`
- Add a `POST` route that accepts the model as JSON input
- Return the created data in the response
- Example: `POST /items` with JSON body returns the same item data
