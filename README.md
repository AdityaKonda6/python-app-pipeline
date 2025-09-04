-----

# CI/CD Pipeline for a Python Web Application

This repository contains the source code for a simple web application built with **Python** and **Flask**.

The primary purpose of this project is to serve as a practical, hands-on demonstration of a complete, end-to-end **Continuous Integration and Continuous Deployment (CI/CD) pipeline** built with Jenkins, Docker, and AWS.

## 🚀 The CI/CD Pipeline

This project is fully automated. The pipeline takes code from a `git push` and automatically deploys it as a live Docker container on a cloud server.

**Workflow:** `Git Push` -\> `GitHub Webhook` -\> `Jenkins Server (AWS EC2)` -\> `Build Docker Image` -\> `Push to Docker Hub` -\> `Deploy to AWS EC2`

1.  **Continuous Integration (CI):**

      * A GitHub **webhook** is configured to notify a **Jenkins** server (hosted on an AWS EC2 instance) on every `git push` to the `main` branch. This automatically triggers a new pipeline run.

2.  **Build & Package:**

      * The Jenkins pipeline, defined as code in the `Jenkinsfile`, checks out the latest source code.
      * It then uses the `Dockerfile` to build a new **Docker image** containing the Python application and all of its dependencies from the `requirements.txt` file.

3.  **Registry:**

      * The newly built and tagged Docker image is then pushed to a repository on **Docker Hub**.

4.  **Continuous Deployment (CD):**

      * The final stage of the pipeline pulls the latest image from Docker Hub onto the EC2 server.
      * It then automatically stops the old running container and starts a new container from the new image, making the changes live instantly.

-----

## 🛠️ Technology Stack

  * **Application:** Python, Flask
  * **CI/CD & Cloud:** Jenkins, Docker, AWS (EC2), Git, GitHub (Webhooks)
  * **Operating System:** Linux (Ubuntu)

-----

## ⚙️ Getting Started (Local Development)

To run the Python application on your local machine without the pipeline.

### Prerequisites

  * Python 3 and `pip` installed.
  * `git` installed.

### Installation & Running

1.  Clone the repository:
    ```sh
    git clone https://github.com/AdityaKonda6/python-app-pipeline.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd python-app-pipeline
    ```
3.  Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4.  Run the application:
    ```sh
    python app.py
    ```
5.  Open `http://127.0.0.1:80` in your browser.

-----



## Hey there 👋, I'm [<a href="https://adityakonda04.vercel.app/">Aditya!</a>](https://github.com/AdityaKonda6)

[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-0e76a8?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/aditya-adi-konda/)
[![Twitter Badge](https://img.shields.io/badge/-Twitter-00acee?style=flat-square&logo=Twitter&logoColor=white)](https://twitter.com/AdityaKonda7)
[![Instagram Badge](https://img.shields.io/badge/-Instagram-e4405f?style=flat-square&logo=Instagram&logoColor=white)](https://www.instagram.com/konda_aditya/)
<img align="right" height="250" width="375" alt="" src="https://github.com/AdityaKonda6/AdityaKonda6/blob/main/giphy2.webp" />


### Glad to see you here! &nbsp; ![](https://visitor-badge.glitch.me/badge?page_id=adityakonda.adityakonda&style=flat-square&color=0088cc)

I’m a **2025 IT Graduate** passionate about **DevOps, Cloud, and Software Development** 🚀.  
My mission? To **bridge the gap between development and operations**—building scalable systems, automating workflows, and ensuring quality from code to deployment.

With a strong foundation in **Java, SQL, Linux**, and hands-on experience with **CI/CD pipelines, Selenium automation, cloud services, and Android development**, I thrive in solving problems end-to-end—from writing code to deploying it in production.

Recently, at **CWD Limited**, I worked on:
- **Automation Testing Frameworks** (Selenium, Java, Maven)
- **Linux-based system configurations & debugging**
- **Hardware-software integration testing**
- API testing with Postman  
…and in the process, strengthened my DevOps skill set.

💡 Curious mind. Fast learner. Always ready to build, break, and rebuild—better.

---

### 🚀 What I’m Working On:
- Building **DevOps projects** (Jenkins, Docker, Kubernetes, AWS, Ansible)
- Enhancing **automation frameworks** for testing & deployment
- Crafting **Android apps** and backend services
- Expanding my **Linux administration** skills

---

### 💼 My Tech Stack:
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/java/java.png" alt="Java"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/linux/linux.png" alt="Linux"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/docker/docker.png" alt="Docker"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/kubernetes/kubernetes.png" alt="Kubernetes"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/aws/aws.png" alt="AWS"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/python/python.png" alt="Python"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/javascript/javascript.png" alt="JavaScript"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/react/react.png" alt="React"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/sql/sql.png" alt="SQL"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/master/topics/git/git.png" alt="Git"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/nodejs/nodejs.png" alt="nodejs"></code>
<code><img height="27" src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSTTzPAw-55ssm1Im594xYZ9eRQu2JylrkYLg&usqp=CAU" alt="mongodb"></code>
<code><img height="27" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png" alt="terminal"></code>

---

<img align="right" height="250" width="375" alt="" src="https://raw.githubusercontent.com/iampavangandhi/iampavangandhi/master/gifs/coder.gif" />

### 📌 Highlights:
- 🛠 Built **dynamic Selenium automation scripts** integrated with Maven
- 🚀 Created & deployed **full-stack and Android applications**
- 🐧 Comfortable with **Linux system administration & shell scripting**
- 📦 Implemented CI/CD workflows for smoother deployments
- ☁️ Learning & applying **cloud infrastructure concepts**

--

### 📫 How to Reach Me:
- Email: **adityakonda04@gmail.com**
- Portfolio: [adityakonda04.vercel.app](https://adityakonda04.vercel.app/)
- LinkedIn: [Aditya Adi Konda](https://www.linkedin.com/in/aditya-adi-konda/)

---

### 📊 GitHub Stats:
<details>
  <summary><b>⚡ GitHub Stats</b></summary>
  <br />
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=adityakonda6&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=adityakonda6&show_icons=true&hide_border=true&layout=compact&langs_count=8"/>
</details>

<details>
  <summary><b>🔥 GitHub Streaks</b></summary>
  <br />
  <img height="180em" src="https://github-readme-streak-stats.herokuapp.com/?user=adityakonda6&hide_border=true" />
</details>

<details>
  <summary><b>☄️ LeetCode Stats</b></summary>
  <br />
   <p align="center"><img align="center" src="https://leetcard.jacoblin.cool/adityakonda04?theme=wtf&font=Coda%20Caption&ext=heatmap" /></p>
</details>

---

💬 Always open to collaborations, tech discussions, and exploring new opportunities in **DevOps, Cloud, and Software Development**.


Like My Work?

<a href="https://www.buymeacoffee.com/adityakonda04" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="60px" width="217px" ></a>

<p align="left"> <img src="https://komarev.com/ghpvc/?username=AdityaKonda6&label=Profile%20views&color=0e75b6&style=flat" alt="AdityaKonda6" /> </p>

<p align="left"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=AdityaKonda6" alt="AdityaKonda6" /></a> </p>


<div align="center">

### Show some ❤️ by starring some of the repositories!
### <a href="https://adityakonda04.vercel.app/">My Portfolio</a>
</div>
