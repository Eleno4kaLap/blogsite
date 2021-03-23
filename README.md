# My first Django project

Website (without version with celery) - http://elenka.pythonanywhere.com/
Admin panel - http://elenka.pythonanywhere.com/admin
Admin credentials:
- username - admin
- password - 123456


**Run in docker:**
1) clone project
2) execute command in the folder **dartblog**
`docker-compose up -d --build`
3) open the browser and go to http://localhost:8000
4) admin panel - http://localhost:8000/admin
Admin credentials:
- username - admin
- password - 123456
4) flower address - http://localhost:5555/

**Site functionality:**
1) display quote on the main image (quote changes every 1 minute after reload the page)
2) view list of pinned posts and other posts
3) view post details
4) search post by title
5) view popular posts (by view count)
6) view list of posts by tag
7) send one email about subscription
