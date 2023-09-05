
# ProjectName - BlogNest  
## Summary

BlogNest is a versatile blogging platform that empowers bloggers to create and share their content effectively. It provides essential features for bloggers to streamline their blogging experience and grow their online presence. Whether you're a seasoned blogger or just starting, BlogNest has you covered.

## Key Features

1. Content Creation: Write and publish your blog posts with ease. The platform provides a user-friendly editor to craft your content.

2. Sharing: Share your blog posts with your audience and on social media platforms to increase your reach.

3. Commenting: Engage with your readers through comments. Encourage discussions and gather feedback.

4. UserProfile Management: Customize your profile, add a bio, profile picture, and manage your blog posts.

5. Edit & Delete Blog Contents: Easily edit and delete your published blog posts to keep your content up to date.

6. Edit & Delete Comments: Have control over the comments on your blog posts. Edit or remove them as needed.

7. likes: Keep track of the number of views on your blog posts to understand their popularity.

8. Authorizations: Implement user roles and permissions for different levels of access and control.

## Prerequisites
Before running the BlogNest application, make sure you have the following prerequisites installed on your system:

      * PostgreSQL (or your preferred database)
      * Django (Python web framework)

  ```bash
  python manage.py runserver
  ```

## Requirements

To run the BlogNest application on your system, please ensure the following:

Install Dependencies: Run the requirements.txt file to install all required Python packages. You can do this with the following command:

```bash
pip install -r requirements.txt
```


1. Database Connection: BlogNest uses PostgreSQL as the default database. If you want to use a different database, make sure to install the appropriate database library and provide the necessary credentials in the Django settings.

2. Mail Configuration: The application uses email functionality. If you want to use your own email for sending notifications, configure the SMTP email settings in the settings.py file. Replace the host email and password with your own.

3. Database Backup: Import the SQLBACKUP/data_backup.sql file into your database to populate it with predefined data.


### Use the reference login credentials:
     Username: snow123
     Password: 1234



Access the BlogNest application in your web browser at http://localhost:8000/.

Use the reference login credentials provided earlier to access the application for testing and exploration.

Start creating, sharing, and managing your blog content on BlogNest!

