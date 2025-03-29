#!/bin/bash

# Set project root name
PROJECT_ROOT="japanese_app"

echo "📁 Creating project structure for: $PROJECT_ROOT"

# Create all required directories
mkdir -p $PROJECT_ROOT/app/core
mkdir -p $PROJECT_ROOT/app/api/routes
mkdir -p $PROJECT_ROOT/app/models
mkdir -p $PROJECT_ROOT/app/schemas
mkdir -p $PROJECT_ROOT/app/crud
mkdir -p $PROJECT_ROOT/tests

# Create top-level files
touch $PROJECT_ROOT/.env
touch $PROJECT_ROOT/requirements.txt
touch $PROJECT_ROOT/run.py

# Create app files
touch $PROJECT_ROOT/app/__init__.py
touch $PROJECT_ROOT/app/main.py
touch $PROJECT_ROOT/app/database.py

# Create core files
touch $PROJECT_ROOT/app/core/config.py
touch $PROJECT_ROOT/app/core/security.py

# Create api files
touch $PROJECT_ROOT/app/api/__init__.py
touch $PROJECT_ROOT/app/api/deps.py
touch $PROJECT_ROOT/app/api/routes/__init__.py
touch $PROJECT_ROOT/app/api/routes/users.py
touch $PROJECT_ROOT/app/api/routes/lessons.py
touch $PROJECT_ROOT/app/api/routes/quizzes.py
touch $PROJECT_ROOT/app/api/routes/vocab.py

# Create models
touch $PROJECT_ROOT/app/models/__init__.py
touch $PROJECT_ROOT/app/models/user.py
touch $PROJECT_ROOT/app/models/lesson.py
touch $PROJECT_ROOT/app/models/quiz.py
touch $PROJECT_ROOT/app/models/vocab.py

# Create schemas
touch $PROJECT_ROOT/app/schemas/user.py
touch $PROJECT_ROOT/app/schemas/lesson.py
touch $PROJECT_ROOT/app/schemas/quiz.py
touch $PROJECT_ROOT/app/schemas/vocab.py

# Create CRUD
touch $PROJECT_ROOT/app/crud/user.py
touch $PROJECT_ROOT/app/crud/lesson.py
touch $PROJECT_ROOT/app/crud/quiz.py
touch $PROJECT_ROOT/app/crud/vocab.py

# Create tests
touch $PROJECT_ROOT/tests/test_users.py

echo "✅ Project structure created successfully!"
