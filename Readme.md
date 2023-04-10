## create file and import in VS code
1. create project dir
2. create python file --> customner.py
3. open that dir from vs code

## creatng virtual env and run files through VS code.
1. py -m pip install --user virtualenv
2. py -m venv env
above command will create env dir within project directory 
3. open cmd through administrative rights and move to project directory
    in my case D:/work/ner
4. To activate virtual env run below scripts 
    > .\env\Scripts\activate
    once it activated you can see below positions in your cmd console
    (env) D:\work\ner>  
    > where python
    > .\env\Scripts\python.exe
5. install requirements through pip for the files and projects
6. VS code provides run and debug option for the python file by pressing f5 or pressing top right |> icon


References for venv
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/    

create custom NER 
https://github.com/amrrs/custom-ner-with-spacy3.git

