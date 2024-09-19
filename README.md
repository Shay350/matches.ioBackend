# MatchesIO

💡 Inspiration 💡
We all know the struggle of searching for jobs that truly align with our skills. We wanted to create something that could make this easier, ESPECIALLY for non-software engineering roles. Matches.io was created out of the desire to not just find job listings, but to ensure we find relevant ones that are aligned to your resume.

🤳 What it does 🤳
Matches uses semantic search powered by the Cohere API to compare your resume with job descriptions. This allows the platform to determine how well-suited you are for various positions, eliminating the guesswork in applying for jobs. You upload your resume, and we handle the rest! The system ranks available job listings based on a similarity score, offering you the best matches to focus on. It also allows users to add reviews for companies, search by role and skill set, and even sort listings by the most popular or highest-paying options.

🛠 How we built it 🛠
Our frontend was built using React.js. We used a MySQL database to store job listings and embeddings via MySQL Workbench. The backend is developed in Python using Flask. It routes user data, handles API requests, and manages the communication between the frontend and database. We used the Cohere API for semantic analysis.

⚠️ Challenges we ran into ⚠️
One of the biggest challenges was connecting the backend with the frontend - CORS the goat. We also faced a few hiccups with GitHub since everyone was working on the codebase, we ran into a lot of merge conflicts. Debugging API integration, particularly with Cohere, was also tricky, especially when dealing with structured outputs for semantic analysis.

🏅 Accomplishments that we're proud of 🏅
We successfully implemented semantic search using Cohere’s cosine similarity algorithm, which calculates how well a job description matches a resume. Most of our team had a backend focus, so we were proud of how quickly we adapted to frontend development using React.js. We developed a seamless user experience and backend logic.

🧠 What we learned 🧠
We learned a lot about semantic search and how to leverage AI to compare job listings with resumes. We also became more proficient in connecting a frontend with a backend and using SQL databases for managing complex queries and API calls. Plus, we learned about creating scalable solutions for job seekers that can easily be extended to new features like salary comparisons and user reviews.

🚀 What's next for Matches.io 🚀
Next steps for matches.io includes improving the user experience on the frontend, allowing for even more roles to be posted. Adding a upload salaries option so users can get an idea of what the salaries are for companies that don't post them, as well as add an AI to improve user's resume depending on the jobs they want.

Built With
alchemyapi
cohere
css
flask
html
javascript
python
react
sql
workbench
