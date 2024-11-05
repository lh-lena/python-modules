## Get started

https://www.djangoproject.com/start/

<details>
    <summary>bash script</summary>
    https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html
    https://linuxcommand.org/

    Learning shell scripting is a great way to automate tasks and better understand how to work with the command line. Here are some of the best resources and paths for learning shell scripting:

### 1. **Online Courses**

   - **[LinuxCommand.org](http://linuxcommand.org/)**:
     - A beginner-friendly site that covers the basics of Linux commands and scripting.
     - Offers a free, structured course on shell scripting from basic commands to advanced scripting techniques.

   - **[Udemy - Shell Scripting: Discover How to Automate Command Line Tasks](https://www.udemy.com/course/command-line-bash-shell-scripting/)**:
     - This is a paid course, but Udemy often has discounts.
     - Covers basic to intermediate concepts, including file manipulation, automating commands, and understanding variables and functions in shell scripts.

   - **[edX - Introduction to Linux by The Linux Foundation](https://www.edx.org/course/introduction-to-linux)**:
     - A free course that offers a general overview of Linux and includes sections on shell scripting.
     - Good for beginners wanting both an introduction to Linux and shell scripting.

   - **[Coursera - Bash for Programmers](https://www.coursera.org/learn/bash-for-programmers)**:
     - Aimed at beginners, this course covers basic shell commands, scripting fundamentals, loops, conditionals, and file manipulation.

### 2. **Books**

   - **"The Linux Command Line" by William E. Shotts**:
     - This is a comprehensive book for beginners and goes from basic command-line usage to complex shell scripting.
     - It's free to download in PDF form and widely recommended in the Linux community.
   
   - **"Shell Scripting: How to Automate Command Line Tasks Using Bash Scripting and Shell Programming" by Jason Cannon**:
     - Great for beginners, this book focuses on practical applications of shell scripting, making it easier to understand real-world usage.

   - **"Learning the bash Shell" by Cameron Newham**:
     - This is an in-depth book that covers a wide range of shell scripting topics and is particularly good if you want to dive deep into bash scripting specifically.

### 3. **Free Tutorials and Documentation**

   - **[Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/)** by The Linux Documentation Project:
     - A comprehensive guide that starts with basic concepts and advances to functions, conditionals, and file handling.
     - Ideal for structured, self-paced learning.

   - **[Advanced Bash-Scripting Guide](https://tldp.org/LDP/abs/html/)**:
     - Also by The Linux Documentation Project, this guide is more advanced and covers complex scripting scenarios.
     - It’s a great reference if you’re looking to understand more detailed aspects of bash scripting.

   - **[Shell Scripting Tutorial on Tutorialspoint](https://www.tutorialspoint.com/unix/shell_scripting.htm)**:
     - Covers a wide range of topics, from beginner to advanced.
     - Each concept is well-explained with examples, making it a good site for reference.

### 4. **Practice Sites**

   - **[OverTheWire: Bandit](https://overthewire.org/wargames/bandit/)**:
     - A popular game designed to teach Linux commands and scripting by solving challenges.
     - Bandit is beginner-friendly and walks you through tasks that build up your understanding of shell commands and scripting progressively.

   - **[Codecademy: Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line)**:
     - Covers shell basics, essential for understanding and creating scripts.
     - It’s an interactive course, which can be a fun way to get comfortable with the command line.

### 5. **YouTube Channels**

   - **[ProgrammingKnowledge](https://www.youtube.com/user/ProgrammingKnowledge)**:
     - This channel has detailed tutorials on Linux, shell scripting, and bash, covering topics from beginner to advanced.

   - **[The Linux Foundation](https://www.youtube.com/user/TheLinuxFoundation)**:
     - Offers many talks, tutorials, and guides on Linux-related topics, including shell scripting.
     - Great if you want to learn about shell scripting in a broader Linux context.

   - **[Derek Banas' Bash Shell Tutorial](https://www.youtube.com/watch?v=9ypTGmAgXko)**:
     - Known for clear, concise tutorials, Derek Banas has a great one-hour overview of bash scripting that covers key concepts quickly.

### 6. **Experimentation and Practice**

   - **Set up a Linux environment** (Ubuntu, Debian, etc.) or use **macOS** Terminal:
     - Practicing on a real environment is key. If you use Windows, you can install [WSL (Windows Subsystem for Linux)](https://docs.microsoft.com/en-us/windows/wsl/) or work with a virtual machine.
   
   - **Write small scripts to automate tasks**:
     - Start with simple scripts, such as automating backups, renaming files, or parsing text files. Real-world practice is the best way to learn and retain scripting knowledge.

---

### Example of a Basic Shell Script Structure

To get started, here’s a simple structure of a shell script that includes a conditional check (like `if [ -z "$1" ]; then ... fi`):

```bash
#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <your_argument>"
  exit 1
fi

# Use the provided argument
echo "Argument provided: $1"
```

This checks if an argument is passed, which is a common pattern in shell scripts. Trying out examples like this will help you build familiarity with shell scripting syntax and flow.

</details>

the HTML code must pass the W3C validation! https://validator.w3.org/

TODO:
Training Python-Django - 0
OOB