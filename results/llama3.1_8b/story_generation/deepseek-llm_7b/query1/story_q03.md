# Lesson Title: Understanding Containerization Technologies in HPC Environments

## Introduction (Hook)
Objective: To grab students' attention by introducing them to a real-world problem and highlighting the importance of containerization technologies in modern computing environments.

"Imagine you are working on a project that requires running complex scientific applications. These applications require specific hardware configurations, operating systems, and dependencies. How can we ensure these requirements are met consistently across different machines? This is where containerization comes into play."

## Core Content Delivery
Objective: To provide an overview of the core concepts - Docker, Singularity, and Linux Containers (LXC), in a logical teaching order.

1. **Docker**
	* Definition and basic concept
	* Dockerfile structure
	* Docker Compose for multi-container applications
2. **Singularity**
	* Definition and basic concept
	* Singularity image format and build process
	* Singularity Exec command
3. **Linux Containers (LXC)**
	* Definition and basic concept
	* Managing containers with `lxc` commands
	* Differences between LXC, Docker, and Singularity
4. **Use Cases in HPC Environments**
	* Containerization for reproducible research
	* Security considerations when using containerization technologies
5. **Comparison with Traditional Hypervisor-Based Virtualization**
	* Advantages and disadvantages of each approach
	* When to use which technology

## Key Activity/Discussion
Objective: To provide an interactive segment where students apply their knowledge by building a simple Docker image or Singularity recipe, discussing the pros and cons of different containerization technologies.

"Let's now build our own containers! In small groups, choose one of the following tasks to complete:
- Create a basic Dockerfile for a simple application you can run on your personal computer (e.g., Python script) and then use Docker Compose to create a multi-container application."

## Conclusion & Synthesis
Objective: To wrap up the lesson by connecting back to the Overall Summary, reinforcing the importance of containerization technologies in HPC environments, and encouraging further exploration.

"Containerization technologies offer a lightweight and portable way to deploy applications in HPC environments. By learning about Docker, Singularity, and Linux Containers, we have gained an understanding of their differences, use cases, and how they differ from traditional hypervisor-based virtualization. As we move forward with our research projects, remember the importance of containerization for reproducibility, security, and consistency."


---

## Teaching Module: Docker
1. The Story (Problem –> Solution –> Impact)
----------------------------------
In the world of software development, developers often faced challenges when it came to deploying and scaling applications. They would spend countless hours configuring servers, setting up environments, and maintaining infrastructure just to ensure that their application runs smoothly. This was a tedious process that took away from time spent on writing code.

One day, during an internal discussion at Docker, the idea of using containers for deployment emerged as a potential solution. Containers were lightweight virtual machines that allowed developers to package applications along with its dependencies and run them anywhere without any compatibility issues. This led to faster deployment and scaling of applications while eliminating the need to worry about underlying infrastructure.

The impact of this discovery was immense, as it changed the landscape of application development forever. It enabled developers to focus solely on writing code instead of spending time setting up environments. The concept of Docker provided a way for developers to take full control over their application's environment and deployment process.

2. Storytelling Hooks
-------------------
*Dramatic Question*: Can you imagine if there was a way to package your applications with all its dependencies, making it easy to deploy anywhere without any compatibility issues?

*Point of View*: From the perspective of a software engineer who wants to write code without worrying about tedious deployment tasks.

3. Classroom Delivery Tips
-------------------------
When explaining the concept of Docker in class, you can start by asking your students what they know about virtual machines and how they are different from physical computers. You can then introduce the idea of containers as a more lightweight version of VMs that allow developers to package their applications along with its dependencies.

To make it relatable for students, use an analogy such as: "Imagine you have all your books (applications) in one room (physical computer), and now imagine if you had multiple copies of the same book organized by chapters (dependencies) and could easily transport them to any other room without worrying about whether there is enough space or electricity."

Next, discuss Docker's strengths such as fast deployment and scaling of applications, followed by its weaknesses like limited support for legacy systems and security concerns. Finally, explain how the concept has changed the landscape of application development and why it matters in today's world.

### Interactive Activities for Docker
1. Debate Topic: "Is Docker worth the risk for deploying legacy systems?"
Statement: "Docker provides fast deployment and scaling of applications, but it is not suitable for supporting legacy systems due to limited support."
2. What If Scenario Question: Imagine a software company uses Docker to deploy their new application on a server with an outdated operating system. Due to compatibility issues, the application failed to run smoothly in production. Evaluate whether it would have been better if they had chosen another deployment method for this legacy system and discuss potential solutions to overcome these trade-offs.


---

## Teaching Module: Singularity
1. The Story (Problem - Solution - Impact)

--

Imagine you are an astrophysicist working on a groundbreaking project that requires massive amounts of computational power and precision. You've been using HPC environments to run your simulations, but every time you need to update the software or install new dependencies, it takes hours of manual labor just to get everything set up correctly again. This not only wastes valuable time but also makes it difficult for other researchers in your team to collaborate effectively on this project.

Enter Singularity - a containerization platform specifically designed for high-performance computing environments that solves these problems by providing a portable and reproducible way to run applications. It uses a unique approach to create containers that are isolated from the host operating system, allowing you to easily share your work with others without worrying about compatibility issues or wasted time on setup.

With Singularity, you can now spend more time focused on refining your simulations rather than dealing with software updates and dependencies. This not only speeds up your workflow but also allows for a higher degree of collaboration among team members.

--

2. Storytelling Hooks

*Dramatic Question*: Can cutting-edge technology help us solve complex scientific challenges more efficiently?

*Point of View*: From the perspective of an astrophysicist working on groundbreaking projects in HPC environments.

3. Classroom Delivery Tips

*Pacing*: Pause here to discuss how this concept could impact other students' experiences with high-performance computing and containerization technologies, or ask a question like: "What do you think are some potential advantages of using Singularity for scientific research?"

*Analogies*: Imagine containerization as a toolbox that allows scientists to work more efficiently on large-scale projects by keeping all the necessary tools in one place without cluttering their workspace.

### Interactive Activities for Singularity
1. Debate Topic: "Is Singularity Overhyped as an HPC Solution?"
The statement: "Despite supporting a wide range of file systems and networking protocols, Singularity is ultimately limited in its support for non-HPC applications." (Strengths vs Weaknesses)

2. 'What If' Scenario Question: "If the Singularity were to gain widespread adoption in personal computing, would it make sense for Linux users who primarily rely on command line operations?" (Trade-offs of Singularity)


---

## Teaching Module: Linux Containers (LXC)
1. The Story (Problem - Solution - Impact)

---

Once upon a time, in a world filled with servers and clusters of computers used by scientists and researchers for high performance computing (HPC), there was a problem that needed solving. These powerful machines were expensive to run, and it took an army of IT specialists to manage them all. Imagine the resources wasted on managing thousands of Linux systems when they could be focused on breakthrough research!

One day, in an engineering lab, a group of researchers stumbled upon a solution – a lightweight virtualization technology called Linux Containers (LXC). LXC promised to allow multiple isolated Linux systems to run on a single host. This meant that instead of having thousands of individual servers, they could have hundreds or even fewer but still achieve the same performance and efficiency!

The discovery was as exciting as it was simple: by using LXC, researchers would not only be able to reduce costs but also simplify their infrastructure management. They shared this 'Aha!' moment with colleagues at conferences and in online forums, spreading knowledge about what they had found. 

---

2. Storytelling Hooks

* "What if you could run multiple virtual machines on a single physical machine? The answer is Linux Containers (LXC), the game-changer that makes high performance computing more accessible!"

3. Classroom Delivery Tips:

* Pacing: When explaining LXC, start with the benefits of running multiple isolated Linux systems and then dive into its details. Use analogies such as "imagine you have hundreds or even fewer servers to run your applications instead of thousands."
* Analogy: Imagine each container in an ocean is a separate Linux system that can only interact with other containers within their own 'ocean.' The host machine, similar to the shoreline, provides infrastructure support for all these 'oceans' without mixing resources.

### Interactive Activities for Linux Containers (LXC)
1. Debate Topic: "Is Linux Containers (LXC) better suited for lightweight applications or complex systems?"

Strengths: Lightweight and efficient
Weaknesses: Limited support for non-Linux operating systems, Security concerns if not properly configured

2. What If Scenario Question: Imagine that a student wants to set up a multi-user system using Linux Containers (LXC). They are concerned about the limited support for non-Linux operating systems but believe it might be beneficial due to its lightweight and efficient nature. How would you guide them in their decision making process, given the trade-offs of this technology?