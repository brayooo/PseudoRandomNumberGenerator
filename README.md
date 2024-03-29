# Pseudo-random numbers generator

This program generate pseudo-random number by 5 methods: Mean squares, linear congruential method,
multiplicative congruential, uniform and normal distribution methods. 

### For use the program you should follow the next steps:
## Clone the Project

1. Go to your desktop or an empty folder and right-click to display the pop-up 
   menu where you will select the "Open Git Bash here" option. 
    </br>
    </br>

    ![Pop-up](assets/gitBash.png)


2. In the terminal, type the following command:

    `git clone https://github.com/brayooo/PseudoRandomNumberGenerator.git`
    And wait for it to finish cloning the entire project from the repository


3. When you finish cloning, the project folder should appear.

    ![Folder1](assets/folder.png)

## Install required Python Libraries

If you are using windows you better use a **bash** terminal or if
you already have the configuration done of your windows cmd to works
with python, go ahead.

### Let's check that pip is installed
- Open a **bash** into the project and type:

    ![bash2](assets/bash2.png)

      > pip show pip
    
    If you have it installed, you should see general information about this library. Like this:
    
    ![bash3](assets/bash3.png)

    If nothing comes out, you must install pip.

    
- Install requirements:

      > pip -r install requirements.txt
    
    ![bash4](assets/bash4.png)
    
    ### Now you're up to use the project.

## Running the Project

- Open the project with the **IDE** or **Development Environment** you want.
- You'll see the main.py file.
- You can run the file with the command
      
      > python main.py


- Or you can run the file using the run configuration of your IDE.

Perfect, if everything goes well and if you followed the steps you can see the user interface,
you're ready to use the program to generate pseudo-random numbers.

          
![interface](assets/interface.png)

## Important

The program saves the numbers it generates with the parameters that you entered when you click the `Generate` button.

Once you press the button, the program creates `NumberGenerated` folder where the files are saved.

![folders](assets/NumbersFolders.png)

The files are saved with name of the method that generated them. **All the files have a .json extension**

![files](assets/filesG.png)

## Author

- Bryan Lopez

**Simulación de Computadores - Grupo 1**