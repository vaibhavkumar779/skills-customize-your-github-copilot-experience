# 📘 Assignment: FastAPI Database API

## 🎯 Objective

Build a FastAPI application that stores and retrieves data in a SQLite database using SQLAlchemy and Pydantic.

## 📝 Tasks

### 🛠️ Define the Database Model

#### Description

Create a SQLAlchemy model and configure the database connection for the FastAPI app.

#### Requirements
Completed program should:

- Use SQLite as the database engine
- Define a SQLAlchemy `Item` model with fields for `id`, `name`, `description`, and `price`
- Create the database tables automatically when the app starts

### 🛠️ Create CRUD Endpoints

#### Description

Implement routes for creating, reading, updating, and deleting items.

#### Requirements
Completed program should:

- Add `GET /items` and `GET /items/{item_id}` endpoints
- Add `POST /items` to create a new item
- Add `PUT /items/{item_id}` to update an existing item
- Add `DELETE /items/{item_id}` to remove an item

### 🛠️ Use Pydantic Schemas

#### Description

Validate request and response data with Pydantic models.

#### Requirements
Completed program should:

- Define Pydantic schemas for incoming item data and response objects
- Return validated JSON responses from endpoints
- Handle invalid input with appropriate HTTP error responses
