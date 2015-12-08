# Advanced Stylometry Course, Wuerzburg (December 2015)

## Installation instructions
In this section, we will guide through the necessary steps to set up your computer for the course.

### Download course materials
This series of workshops consists of a series of chapters in the form of so-called "notebooks". These materials should be downloaded by clicking on the "download ZIP" button in the right column on this page. Unzip the file and save it somewhere on your computer. Below, we will assume that you unzipped this file on your desktop.

### Install Python 3
Please install the Anaconda distribution of Python, which is a package which comes with most of the functionality etc. which you will need for these workshops. Direct your browser to [http://continuum.io/downloads#py34](http://continuum.io/downloads#py34) and download the graphical installer. Double-click the downloaded file and install the Python distribution **system-wide**. Make sure that you download Python 3.

Once installed, open a terminal (on Linux or Mac OS X) or a command prompt (on Windows) and first `cd` to the directory in which you saved the tutorial. For Mac OS X users:

    cd /Users/your-user-name/Desktop/wuerzb15

For Linux users:

    cd /home/your-user-name/Desktop/wuerzb15

For Windows users:

    cd c:\Users\your-user-name\Desktop\wuerzb15

where you need to replace `your-user-name` with your actual user name on your computer! Next type:

    ipython notebook

If this returns an error message such as "Command not found", please try running with:

    jupyter notebook

This will launch the jupyter notebook in your browser. Click on the appropriate link to open the first chapter etc. 

### Download Sublime Text
For this course, you will need a decent, cross-platform text editor. We recommend installing [Sublime Text 3](http://www.sublimetext.com/3). Just surf to the download tab and install the editor.

### Install additional packages

Install any additional packages you might need using `conda` or `pip`. For `seaborn`, for instance, type in your terminal:

`conda install seaborn`

or

`pip install seaborn`




