I am excited to share my certificate from Educative! I just completed "Mastering OpenAI Codex for Agentic Coding" and earned my certificate. 

# What Is the Course

In this course,we were supposed to create A Flask pixel art app for drawing on a 32x32 grid, saving canvases, browsing a gallery, and downloading artwork as PNG files. Built as a learning-by-doing Codex project.

# Structure of the Course
In this course, we first deep dive into to understand What is Codex, setting up the codex in the local either through web, cli or desktop. I have choosed the Desktop application for the working. 

As all the configuration have a single `config.toml` for consistent behaviour for all the platforms and working context. Introduction about `AGENTS.md` and it's usecase and understanding the different conventions at project level, repository level and file level configuration. 

Introduction about Skills, Plugins and Automations. Skills is basically packaging repetable workflows of the project in a file and you can build your own skills at project level, folder level or even file level. It works as a entry point for AI agent to understand what is supposed to do, it can be lengthy of in detail with all the information about it's working and it's limitations. Plugins are basically a way to extend the functionality of the project and can be used to add new features or modify existing ones. Automations are a way to automate repetitive tasks and can be used to streamline the workflow of the project. 

After that, got to learn about MCP and how to use it with Codex. MPC is a way of connecting Codex agent with external environments or repositories to access the relevant tools and resources via STDIO or HTTP Servers. So, that, it can execute the task with tool calling and without unecessary context switching.

As, we all know that, Codex is a powerful tool and we can not just use it for one task at a time, but to run or work with 5-6 different (6 is the current limitation for how much one can run parallel task in Codex) tasks at a time. All the tasks are run in parallel in their own Git worktrees so that, no task can interfere with each other and can be run in parallel.

# Structure of the Project


Use the below prompt to create Flask app with no module just one requirements.txt file and an AGENTS.md file with all the instructions for the agent to work on the project.


First Prompt given to the agent after the setup:
```
We are building a Flask pixel art canvas app. The app will let users draw on a 32×32 grid, save their artwork with a name, browse a gallery of saved canvases, and export any canvas as a PNG file. The stack is Flask, SQLite, Flask-SQLAlchemy, HTML5 Canvas, vanilla JavaScript, and Pillow.

For this first task, scaffold the base app:

1. app.py: Flask app with SQLAlchemy configured and the database initialised on startup

2. models.py: A Canvas model with fields: id (integer, primary key), name (string, required), pixel_data (JSON, stores the 32×32 grid as a 2D array of hex colour strings), created_at (timestamp, auto-set)

3. templates/index.html: A minimal base HTML page that the index route serves

4. An index route in app.py that returns the index template

The app should starts without errors when we run python3 app.py.
```

# Development and Comments

I have created a detailed AI_CONVERSATION_REFERENCE.md file (could be found in the repo), which contains all the conversation from the very first prompt which I had with AI and gives a step by step approach how to use Codex to build a project from scratch. 

# Outcome

After testing it locally(screenshot attached below), I was able to land on a small/cute Pixel Art Canvas app which is able to draw on a 32x32 grid, save the canvas with a name, browse the gallery of saved canvases and export any canvas as a PNG file. But, it was just a basic working propotype with no functionality of SignIn functionality, Deleting a canvas or Editing a canvas etc. 

# Learning

As mentioned in the begging in the structure of the course section, I have learned about the Codex and it's setup and how to use it for the development or creating a project from scratch. I have learned about the different conventions at project level, repository level and file level configuration. I have learned about Skills, Plugins and Automations and how to use them in the project. I have learned about MCP and how to use it with Codex. 


# Limitation and Boundaries of OpenAI Codex 
Being a Master's graduate, I have learned about how to understand the project not just on the implementation level but also on the design / system level, so that one can find the tradeoff and further make your system robust and error proof. I have learn that Codex is a powerful tool and we can not just use it for one task at a time, but to run or work with 5-6 different (6 is the current limitation for how much one can run parallel task in Codex) tasks at a time. All the tasks are run in parallel in their own Git worktrees so that, no task can interfere with each other and can be run in parallel. But soon realised it would be difficult in the current setup and environment, few of the learning below (feel to free suggest/point mistakes on them).

I have learnt that UI of the Codex Desktop application is not that user friendly, as it was very difficult to see the diff in the code/file, may be I was using at Laptop could be a constraint. During the setup process, as default port `5000` was already in use, but the Codex was not been able to find and identify even after having access to the system. So, I have to manually change the port in the `app.py` file. Also, found even after mentioning to refer the `AGENTS.md` file for the instructions for the interaction. Codex was not skipping it and didn't read the instructions or been able to recall the instructions properly. It could be I was using the defaut/free version of the Codex which was 5.5 Medium Thinking, may be higher version could be used better. Also, I believe it was quite difficult to come back to the right context but if by any chance you made some wrong prompt in the starting, may be starting from scratch could be a better option than just trying to fix the agent. 

In the final, I believe in a hour in less than 10 medium size prompts and a project with less than 10 files and overall, I was able to consume the token for a month, not sure, how much token, but I tried to use Repomix and Tokencalcuator.net, to calculate the total output token from Repomix.md file which was about (8512 tokens) in total. Even considering the input tokens, I believe it was quite a lot of tokens consumed for a small project.

Thanks again for reading till the end. I will continue believing and exploring the AI and it's capabilities to make our life easier and productive and how it can be used to build project at a scale.


GitHub Repo Link: https://github.com/irahulcse/OpenAI_Codex_Pixel_Art_Canvas
Repo Mix Link: https://github.com/irahulcse/OpenAI_Codex_Pixel_Art_Canvas/blob/main/repomix/repomix-output-irahulcse-OpenAI_Codex_Pixel_Art_Canvas.md



https://www.educative.io/verify-certificate/NRNV8SC923

#WrittenByHuman #GrammerCheckedWithGrammarly