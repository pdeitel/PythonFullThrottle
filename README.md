# PythonFullThrottle
Source code and Jupyter Notebooks files for my "Python Full Throttle" live training course.  

I'll keep this repository up-to-date with any changes I make for future presentations. 

**These files are for your personal use and may not be redistributed or reposted.**

If you have any questions, open an issue in the Issues tab or email us: deitel at deitel dot com.

Copyright 2024 by Deitel & Associates, Inc. and Pearson Education, Inc. All Rights Reserved. 

# Setup for Executing the Examples
If you intend to execute code in parallel with me during the live training (which you don't need to do, but can), you'll want to do one of the following:

1. For a **zero-install environment**, you can go to the following mybinder.org link, which will allocate a cloud-based environment and load this repository's Jupyter Notebooks https://mybinder.org/v2/gh/pdeitel/PythonFullThrottle/HEAD?urlpath=lab
2. You can run everything locally on your computer. To do so, install the Anaconda Python Distribution for Python 3.11 at https://anaconda.com/download
3. You can use the Jupyter team's preconfigured jupyter/scipy-notebook Docker container:
> `docker run -p 8888:8888 -it --user root -v fullPathTo/PythonFullThrottle:/home/jovyan/work jupyter/scipy-notebook:latest start.sh jupyter lab`

In #3, **be sure to replace `fullPathTo/PythonFullThrottle` with the actual location where you download my code on your system**.

# Our Books on Which These Examples Are Based
The content of this course is based on our book <a href=https://amzn.to/2Kd8dQk target="_blank">Python for Programmers</a>, which is a subset of our book <a href=https://amzn.to/2KfCptN target="_blank">Intro to Python for Computer Science and Data Science: Learning to Program with AI, Big Data and the Cloud.</a> Both are available to O'Reilly Online Learning subscribers. See all our recent content and webinars on O'Reilly at https://deitel.com/LearnWithDeitel
    
<a href="https://deitel.com/python-for-programmers-book/"><img src="https://deitel.com/wp-content/uploads/2020/01/python-for-programmers.jpg" alt="Cover image for Python for Programmers" width="150px" border="1px"/></a>

<a href="https://deitel.com/intro-to-python-for-computer-science-and-data-science/"><img src="https://deitel.com/wp-content/uploads/2020/01/intro-to-python-for-computer-science-and-data-science.jpg" alt="Cover image for Intro to Python for Computer Science and Data Science" width="150px"/></a>

The authors and publisher of this book have used their best efforts in preparing this book. These efforts include the development, research, and testing of the theories and programs to determine their effectiveness. The authors and publisher make no warranty of any kind, expressed or implied, with regard to these programs or to the documentation contained in this book. The authors and publisher shall not be liable in any event for incidental or consequential damages in connection with, or arising out of, the furnishing, performance, or use of these programs.

