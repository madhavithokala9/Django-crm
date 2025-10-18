Build a Powerful Teacher Management System with Django

# Overview
This repository contains the code for a complete Teacher Management System (TMS) developed using the Django framework. 

# Key Features
The system is designed with multiple user roles, each having a dedicated dashboard and specific functionalities:
1. Multi-Role Dashboards
# Admin Dashboard: Provides an overview showing the total number of Teachers, awards, departments, and revenue. It includes visualization tools to display demographics (e.g., total teachers, students, boys, or girls).
# Teacher Dashboard: Allows exploration of teacher name, subject and contact information.
# CRUD Operations: Full functionality for adding, listing, detailing, editing, and deleting student records
# Authentication and Security
The system uses a custom Django authentication model.
• User Flows: Implements views for sign-up, login, and logout.
• Password Management: Includes functionality for sending a password reset link to the user's email and processing the password reset.
• Authorization: Defines distinct roles: Student, Teacher, and Admin.
# Notification System
A built-in notification system helps manage updates.
• Notifications are created automatically upon certain actions (e.g., adding or deleting a student).
• Notifications are filtered based on the authenticated user.
• Users can mark notifications as read or clear all notifications.

# Installation and Setup
Prerequisites
• Python 3.x
• The following libraries are required:
    ◦ Django
    ◦ Pillow (Needed for handling image/media files)

     # Steps
1. Initialize the Project Environment: Open the project folder (e.g., schools) in VS Code. Create and activate a virtual environment:
2. Install Dependencies: Install Django and Pillow within the activated environment:
3. Start Django Project Structure: The project structure includes a project named home and several apps: school, student, and homeo (for authentication). These must be installed in settings.py. The project uses templates and static folders for rendering HTML and handling static files, which are configured in settings.py.
4. Perform Migrations: Run the migration commands to create the database schema, including the custom user model and the Student/Parent models:
5. Create Superuser: Create a superuser to access the Django admin panel:
6. (Note: For security purposes when hosting, it is recommended not to use "admin" as the username or password).
Running the Application

#Acknowledgments
This project is based on the step-by-step video tutorial provided by the Brokly Master YouTube channel
1. Start the Server: Run the Django development server:
2. Access the Application: Open your browser and navigate to the local server address (e.g., http://127.0.0.1:8000/). The application is typically configured to show the login/registration page first.
3. Admin Access: The admin panel can be accessed via the /admin/ path (e.g., http://127.0.0.1:8000/admin/)
