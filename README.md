# BlogNest - Blogging Platform
## Summary
BlogNest is a versatile blogging platform that empowers bloggers to create and share their content effectively. It provides essential features for bloggers to streamline their blogging experience and grow their online presence. Whether you're a seasoned blogger or just starting, BlogNest has you covered.

## Key Features
Content Creation: Write and publish your blog posts with ease. The platform provides a user-friendly editor to craft your content.

Sharing: Share your blog posts with your audience and on social media platforms to increase your reach.

Commenting: Engage with your readers through comments. Encourage discussions and gather feedback.

UserProfile Management: Customize your profile, add a bio, profile picture, and manage your blog posts.

Edit & Delete Blog Contents: Easily edit and delete your published blog posts to keep your content up to date.

Edit & Delete Comments: Have control over the comments on your blog posts. Edit or remove them as needed.

Likes: Keep track of the number of views on your blog posts to understand their popularity.

Authorizations: Implement user roles and permissions for different levels of access and control.

## Requirements
To run the BlogNest application on your system, please ensure the following:

Install Dependencies: Run the requirements.txt file to install all required Python packages. You can do this with the following command:

```bash
   pip install -r requirements.txt

1.Database Connection: BlogNest uses PostgreSQL as the default database. If you want to use a different database, make sure to install the appropriate database library and provide the necessary credentials in the Django settings.

2. Mail Configuration: The application uses email functionality. If you want to use your own email for sending notifications, configure the SMTP email settings in the settings.py file. Replace the host email and password with your own.

3.Database Backup: Import the SQLBACKUP/data_backup.sql file into your database to populate it with predefined data. You can use the following command to import the data:
```bash
   psql -U your_username -d your_database_name < SQLBACKUP/data_backup.sql

Use the reference login credentials:
Username: snow123
Password: 12345
## Prerequisites
Before running the BlogNest application, make sure you have the following prerequisites installed on your system:

PostgreSQL (or your preferred database)
Django (Python web framework)
Run the Django development server to start the application:

```bash
   python manage.py runserver

Access the BlogNest application in your web browser at http://localhost:8000/.

Use the reference login credentials provided earlier to access the application for testing and exploration.

Start creating, sharing, and managing your blog content on BlogNest!

Please keep in mind that this is a basic README file, and you might want to provide more detailed instructions and configurations for deployment in a production environment.
